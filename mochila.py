import numpy as np
import pandas as pd
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
