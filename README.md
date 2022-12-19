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
py mochila.py <Archivo> <SemFinal> <NumIteraciones> <TauIni> <TauFin>
```

Donde:
- **Archivo**: Archivo de entrada, documento con los elementos de la mochila.
- **SemFinal**: Valor que tomará la última semilla a evaluar (desde el 1 hasta SemFinal). Valor entero.
- **NumIteraciones**: Condición de término o número de iteraciones. Valor entero.
- **TauIni**: Valor inicial de Tau.
- **TauFin**: Valor final de Tau.

## Ejemplo de Ejecución

```
py mochila.py .\Knapsack_Test_Instances\hardinstances_pisinger\knapPI_11_20_1000.csv 30 10000 1.4 1.9
```