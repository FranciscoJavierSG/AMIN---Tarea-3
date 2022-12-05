# Algoritmos Metaheurísticos Inspirados en la Naturaleza
*Autores: José Avilán (javilan@ing.ucsc.cl) y Francisco Salazar (fsalazarg@ing.ucsc.cl)*

Desarrollar una aplicación que implemente el Problema de la Mochila a través del método de Extremal Optimisation utilizando el lenguaje de programación Python.

## Instalación
Antes de ejecutar el programa, es necesario:
- Tener instalado Python 3.8.10 en su sistema.
- Para descargar el programa, presione en el siguiente [enlace](https://codeload.github.com/FranciscoJavierSG/AMIN---Tarea-3/zip/refs/heads/main).

## Ejecución 
Para ejecutar el programa, escriba lo siguiente en la consola o terminal de su sistema operativo:

```       
py mochila.py <Archivo> <Seed> <Iteraciones> <Tau>
```

Donde:
- **Archivo** : Archivo de entrada, documento con los elementos de la mochila.
- **Seed**: Valor semilla generador valores randómicos, valor entero.
- **Iteraciones**: Condición de término o número de iteraciones, valor entero.
- **Tau**: Valor de Tau.

## Ejemplo de Ejecución

```
py mochila.py .\Knapsack_Test_Instances\smallcoeff_pisinger\knapPI_1_50_1000.csv 1 100 0.9
```