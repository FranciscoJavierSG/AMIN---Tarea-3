import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def generarFitness():
    fitness = precio/peso
    return fitness

if len(sys.argv) == 6: 
    entrada = str(sys.argv[1])
    print("Archivo de entrada: ", entrada)

    semilla = int(sys.argv[2])
    print("Semilla: ", semilla)

    numIteraciones = int(sys.argv[3])
    print("Número de iteraciones: ", numIteraciones)

    tauInicial = float(sys.argv[4])
    print("Tau inicial (τ): ", tauInicial)

    tauFinal = float(sys.argv[5])    
    print("Tau final (τ): ", tauFinal)
else:
    print('Error en la entrada de los parametros')
    sys.exit(0)

np.random.seed(semilla)

tauActual = tauInicial
listTau = []

while (tauActual <= tauFinal):
    solucionTau = []
    iteracionActual = numIteraciones 

    #Inicializacion
    ncz = pd.read_table(entrada, nrows=4, delim_whitespace=True) 
    nombreProblema = ncz.columns[0]
    n=int(ncz[nombreProblema][0])
    c=int(ncz[nombreProblema][1])
    z=int(ncz[nombreProblema][2])

    mochila = pd.read_table(entrada, header=None, sep=',', skiprows = 5, nrows=n).drop(columns=0,axis=1)

    precio = mochila[1].to_numpy()
    peso = mochila[2].to_numpy()
    solucionOptima = mochila[3].to_numpy()

    vectorProbabilidad = np.full(n,np.arange(1,n+1)**(-tauActual),float)
    solInicial = np.random.randint(2, size=n)

    #Algoritmo de Extremal Optimisation
    fitness = generarFitness()
    fitnessNuevo = np.sort(fitness) #fitnessOrdenado

    while iteracionActual > 0: # and np.sum(solInicial*precio) < z
        elegido =  np.random.choice(fitnessNuevo, 1, p=vectorProbabilidad/np.sum(vectorProbabilidad))
        indice = np.where(fitness == elegido)
        indiceRandom = np.random.choice(indice[0], 1)

        if(solInicial[indiceRandom] == 0):
            solInicial[indiceRandom] = 1
            if np.sum(solInicial*peso) > c:
                solInicial[indiceRandom] = 0
        else:
            solInicial[indiceRandom] = 0
            if np.sum(solInicial*peso) > c:
                solInicial[indiceRandom] = 1

        iteracionActual = iteracionActual - 1

        solucionTau.append(np.sum(solInicial*precio))
    
    listTau.append(solucionTau)
    tauActual = tauActual + 0.1

plt.suptitle('Diagrama de caja', fontsize=14, fontweight='bold')
plt.xlabel('Valor de Tau')
plt.boxplot(listTau)
plt.xticks(np.arange(1, len(listTau) + 1), np.arange(tauInicial, tauActual-0.1, 0.1, dtype=float).round(1))
plt.show()