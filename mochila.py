import numpy as np
import pandas as pd
import time
import sys

def factibilidad(mochila):
    if np.sum(sol_inicial*mochila[:, 1]) <= ncz[1]:
        return True
    else:
        return False

def generarFitness(mochila):
    fitness = mochila[:, 0]/mochila[:, 1]
    return fitness

if len(sys.argv) == 5:  # py.exe mochila.py .\Knapsack_Test_Instances\smallcoeff_pisinger\knapPI_1_50_1000.csv 1 100 0.9
    archivo = str(sys.argv[1])
    semilla = int(sys.argv[2])
    numIt = int(sys.argv[3])
    tau = float(sys.argv[4])
    print("Archivo de entrada: ", archivo)
    print("Semilla: ", semilla)
    print("Número de iteraciones: ", numIt)
    print("Tau (τ): ", tau)
else:
    print('Error en la entrada de los parametros')
    print('Los paramentros a ingresar son: semila, archivo de entrada, numero de interaciones y Tau (τ)')
    sys.exit(0)
    
np.random.seed(semilla)

ncz = np.genfromtxt(archivo, delimiter=' ', skip_header = 1 , usecols=(1) , skip_footer=2596, dtype = int) # primer n=nodos c=capacidad z=mejor_solucion en el archivo
mochila = np.genfromtxt(archivo, delimiter=',', skip_header = 5 , usecols=(1, 2, 3) , skip_footer=2575, dtype = int) # valor, peso, asignacion
while True: # Solucion inicial factible, mejorable para capacidades pequeñas
    sol_inicial = np.random.randint(2, size=int(ncz[0]))
    if factibilidad():
        break
probabilidad = (np.arange(int(ncz[0])) + 1)**-tau
# np.random.choice(np.arange(int(ncz[0])), 1, p=probabilities/np.sum(probabilities)) # AUN SIN USAR, elegir por metodo de la ruleta
fitness = generarFitness()
