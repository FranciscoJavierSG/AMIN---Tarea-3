#El programa no solicita al usuario que ingrese una semilla, pues evalúa las semillas del 1 al 30
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def generarFitness():
    fitness = precio/peso
    return fitness

def solFactible():
    if np.sum(solInicial*precio) <= c:
        return True
    else:
        return False

if len(sys.argv) == 6: 
    entrada = str(sys.argv[1])
    print("Archivo de entrada:", entrada)

    semFinal = int(sys.argv[2])
    print("Semilla:", semFinal)
    
    numIteraciones = int(sys.argv[3])
    print("Número de iteraciones:", numIteraciones)

    tauInicial = float(sys.argv[4])
    print("Tau inicial:", tauInicial)

    tauFinal = float(sys.argv[5])    
    print("Tau final:", tauFinal)
else:
    print('Error en la entrada de los parametros')
    sys.exit(0)

tauActual = tauInicial
listaTau = []

while (tauActual <= tauFinal):
    solucionTau = []
    semActual = 0
    
    #Cambiar por un for x in range(1,30)
    while semActual < semFinal:
        np.random.seed(semActual)
        
        iteracionActual = numIteraciones 
        #Inicializacion
        ncz = pd.read_table(entrada, nrows=4, delim_whitespace=True) 
        nombreProblema = ncz.columns[0]
        n=int(ncz[nombreProblema][0])
        c=int(ncz[nombreProblema][1])
        z=int(ncz[nombreProblema][2])

        mochila = pd.read_table(entrada, header=None, sep=',', skiprows = 5, nrows=n).drop(columns=0, axis=1)

        precio = mochila[1].to_numpy()
        peso = mochila[2].to_numpy()
        solucionOptima = mochila[3].to_numpy()
        
        solInicial = np.random.randint(2, size=n)
        while True: 
            if not solFactible():
                solInicial[np.random.randint(int(n), size=1)] = 0
            else:
                break
            
        vectorProbabilidad = np.full(n,np.arange(1,n+1)**(-tauActual),float)

        fitness = generarFitness()
        fitnessNuevo = np.sort(fitness) #fitnessOrdenado
        
        #Algoritmo de Extremal Optimisation
        while iteracionActual > 0: # and np.sum(solInicial*precio) < z
            elegido =  np.random.choice(fitnessNuevo, 1, p=vectorProbabilidad/np.sum(vectorProbabilidad))
            indice = np.where(fitness == elegido)
            indiceRandom = np.random.choice(indice[0], 1)

            if(solInicial[indiceRandom] == 0):
                solInicial[indiceRandom] = 1
                if np.sum(solInicial*peso) > c:
                    solInicial[indiceRandom] = 0
            else: #(solInicial[indiceRandom] == 1)
                solInicial[indiceRandom] = 0
                if np.sum(solInicial*peso) > c:
                    solInicial[indiceRandom] = 1

            iteracionActual = iteracionActual - 1
         
        solucionTau.append(np.sum(solInicial*precio))
        semActual = semActual + 1
        
    listaTau.append(solucionTau)
    tauActual = tauActual + 0.1

fig = plt.figure(figsize=(10,7))
plt.boxplot(listaTau)
plt.xlabel('Valor de Tau')
plt.xticks([1, 2, 3, 4, 5], [1.4, 1.5, 1.6, 1.7, 1.8])
plt.show()