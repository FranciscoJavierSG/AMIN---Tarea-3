import numpy as np
import pandas as pd
import sys

def generarFitness(mochila):
    fitness = mochila[:, 0]/mochila[:, 1]
    return fitness

if len(sys.argv) == 5: 
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
iteracionMax = numIteraciones
iteracionActual = 0

while (tauActual < tauFinal):
    #Inicializacion
    ncz = pd.read_table(entrada, nrows=4, delim_whitespace=True) 
    nombre_problema = ncz.columns[0]
    n=int(ncz[nombre_problema][0])
    c=int(ncz[nombre_problema][0])
    z=int(ncz[nombre_problema][0])

    mochila = pd.read_table(entrada, header=None, sep=',', skiprows = 5, nrows=n).drop(columns=0,axis=1)

    precio = mochila[1].to_numpy()
    peso = mochila[2].to_numpy()
    solucionOptima = mochila[3].to_numpy()

    vectorProbabilidad = np.full(n,np.arange(1,n+1)**(-tauActual),float)
    sol = np.random.randint(2, size=n)

    #Algoritmo de Extremal Optimisation
    fitness = generarFitness()
    fitness = np.sort(fitness) #fitnessOrdenado