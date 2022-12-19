import numpy as np
import pandas as pd
import sys

def generarFitness():
    fitness = precio/peso
    return fitness

if len(sys.argv) == 6: 
    entrada = str(sys.argv[1])
    semilla = int(sys.argv[2])
    numIteraciones = int(sys.argv[3])
    tauInicial = float(sys.argv[4])
    tauFinal = float(sys.argv[5])
    print("Archivo de entrada: ", entrada)
    print("Semilla: ", semilla)
    print("Número de iteraciones: ", numIteraciones)
    print("Tau inicial (τ): ", tauInicial)
    print("Tau final (τ): ", tauFinal)
else:
    print('Error en la entrada de los parametros')
    sys.exit(0)

np.random.seed(semilla)

tauActual = tauInicial
iteracionActual = numIteraciones #Va al reves (de numIteraciones al 0)
tauList = []

while (tauActual < tauFinal):
    list = []
    #Inicializacion
    ncz = pd.read_table(entrada, nrows=4, delim_whitespace=True) 
    nombre_problema = ncz.columns[0]
    n=int(ncz[nombre_problema][0])
    c=int(ncz[nombre_problema][1])
    z=int(ncz[nombre_problema][2])
    print("n = ", n)
    print("c = ", c)
    print("z = ", z)

    mochila = pd.read_table(entrada, header=None, sep=',', skiprows = 5, nrows=n).drop(columns=0,axis=1)

    precio = mochila[1].to_numpy()
    peso = mochila[2].to_numpy()
    solucionOptima = mochila[3].to_numpy()

    print("precio = ", precio)
    print("peso = ", peso)
    print("solucionOptima = ", solucionOptima)

    vectorProbabilidad = np.full(n,np.arange(1,n+1)**(-tauActual),float)
    solInicial = np.random.randint(2, size=n)

    print("solInicial = ", solInicial)

    #Algoritmo de Extremal Optimisation
    fitness = generarFitness()
    fitnessNuevo = np.sort(fitness) #fitnessOrdenado
    print("Antes del while")
    while iteracionActual > 0 and np.sum(solInicial*precio) < z:
        print("Dentro del while")
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
        print("Iteracion ",iteracionActual)
        list.append(np.sum(solInicial*mochila[:, 0]))
    
    tauList.append(list)
    tauActual = tauActual + 0.1