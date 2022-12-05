import numpy as np
import sys

def factibilidad(mochila):
    if np.sum(sol_inicial*mochila[:, 1]) <= NCS[1]:
        return True
    else:
        return False

def generarFitness(mochila):
    fitness = mochila[:, 0]/mochila[:, 1]
    return fitness

if len(sys.argv) == 5: 
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

NCS = np.genfromtxt(archivo, delimiter=' ', skip_header = 1 , usecols=(1) , skip_footer=2596, dtype = int)
mochila = np.genfromtxt(archivo, delimiter=',', skip_header = 5 , usecols=(1, 2, 3) , skip_footer=2575, dtype = int) 
while True:    
    sol_inicial = np.random.randint(2, size=int(NCS[0]))     
    if factibilidad():         
        break 
probabilidad = (np.arange(int(NCS[0])) + 1)**-tau
fitness = generarFitness()