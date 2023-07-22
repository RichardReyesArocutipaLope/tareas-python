import math
import numpy
from tabulate import tabulate
lista2=[0.0449,
0.6015,
0.63,
0.5514,
0.0207,
0.1733,
0.6694,
0.2531,
0.0316,
0.1067,
0.5746,
0.3972,
0.8297,
0.3587,
0.3857,
0.049,
0.7025,
0.6483,
0.7041,
0.1746,
0.8406,
0.1055,
0.6972,
0.5915,
0.3362,
0.8349,
0.1247,
0.9582,
0.2523,
0.1589,
0.92,
0.1977,
0.9085,
0.2545,
0.3727,
0.2564,
0.0125,
0.8524,
0.3044,
0.4145]
lista=[0.0449, 0.6015, 0.63, 0.5514, 0.0207, 0.1733, 0.6694, 0.2531, 0.0316, 0.1067, 0.5746, 0.3972, 0.8297, 0.3587,0.3857, 0.049, 0.7025,0.6483, 0.7041, 0.1746, 0.8406,
          0.1055, 0.6972, 0.5915, 0.3362, 0.8349, 0.1247, 0.9582, 0.2523, 0.1589, 0.92,0.1977, 0.9085, 0.2545, 0.3727,0.2564, 0.0125, 0.8524, 0.3044, 0.4145]

def promVar(valores):
    tamaño=len(valores)
    promedio= sum(valores) / len(valores)
    suma=0
    for i in range(tamaño):
        suma+=(valores[i]-promedio)**2
    varianza=suma/(tamaño-1)
    print(f"El total de numeros es: {tamaño}")
    print(f"El promedio es: {promedio}")
    print(f"La varianza es: {varianza}")
    '''
    #para prueba de medias
    Z=1.96#Zalfa/medios
    limiteInferior= (1 / 2) - (Z * (1 / math.sqrt(12 * tamaño)))
    limiteSuperior= (1 / 2) + (Z * (1 / math.sqrt(12 * tamaño)))
    print(f"limite inferior : {limiteInferior}")
    print(f"limite inferior : {limiteSuperior}")
    #seconcluye que no se puede rechazar que el conjunto de 40 números
    # tiene un valor esperado de 0.5, con un nivel de aceptación de 95 por 
    # ciento
    '''
    #para prueba de varianza
    chialfamedios=58.1200541
    chiunoMenosAlfamedios=23.6543003
    limiteInferiorV = chiunoMenosAlfamedios/ (12 * (tamaño - 1))
    limiteSuperiorV = chialfamedios / (12 * (tamaño - 1))

    print(f"limite inferior : {limiteInferiorV}")
    print(f"limite superior : {limiteSuperiorV}")
    #que no se puede rechazar que el conjunto de 40 núm eros r,
    # tiene unavarianza de 1 /12

promVar(lista)



corridAA = [0.34, 0.83, 0.96, 0.47, 0.79, 0.99, 0.37, 0.72, 0.06, 0.18, 0.67, 0.62, 0.05, 0.49, 0.59, 0.42, 0.05, 0.02, 0.74, 0.67, 0.46, 0.22, 0.99, 0.78, 0.39,
         0.18, 0.75, 0.73, 0.79, 0.29, 0.11, 0.19, 0.58, 0.34, 0.42, 0.37, 0.31, 0.73, 0.74, 0.21, ]
def corridasCAA(lista,ZalfaM):
    tamañoCAA=len(lista)
    secuencia=[]
    for i in range(1,tamañoCAA):
        if lista[i]>lista[i-1]:
            secuencia.append(1)
        else:
            secuencia.append(0)

    tamSecuencia=len(secuencia)

    print(f"la secuencia obtenida es: {secuencia}")
    corridas=[]

    for i in range(1,tamSecuencia):
        if secuencia[i]==secuencia[i-1]:
            corridas.append(0)
        else:
            corridas.append(1)
    corridas.insert(0,1)
    print(f" corridas es: {corridas}")
    numCorridas = corridas.count(1)
    print(f"El numero de corridas : {numCorridas}")
    valorEsperado = (2 * tamañoCAA - 1) / 3
    varianza = (16 * tamañoCAA - 29) / 90
    Z0 = abs((numCorridas - valorEsperado) / math.sqrt(varianza))

    dataCAA = [['NUMERO DE CORRIDAS: ', numCorridas],
              ['VALOR ESPERADO: ', valorEsperado],
              ['VARIANZA: ', varianza],
              ['ESTADÍSTICO Z0: ', Z0]]
    print('\n--RESULTADO--')
    print(tabulate(dataCAA, tablefmt="fancy_grid"))

    if Z0 < ZalfaM:
        print("\nno se puede rechazar que el conjunto de r. sea independiente.")
    else:
        print("\nLos números del conjunto Ri no son independientes")
corridasCAA(corridAA,1.96)

corridAAM=[0.809,0.042,0.432,0.538,0.225,0.88,0.688,0.772,0.036,0.854,0.397,0.268,0.821,0.897,0.07,0.721,0.087,0.35,0.779,0.482,
0.136,0.855,0.453,0.197,0.444,0.799,0.809,0.691,0.545,0.857,0.692,0.055,0.348,0.373,0.436,0.29,0.015,0.834,0.599,0.724,
0.564,0.709,0.946,0.754,0.677,0.128,0.012,0.498,0.6,0.913]
print("================================================================")
def corridasAAM(valoresAAM,ZalfaAAM):
    tamañoAAM = len(valoresAAM)
    secuencia = []
    for i in range(tamañoAAM):
        if valoresAAM[i] > 0.5:
            secuencia.append(1)
        else:
            secuencia.append(0)
    print(secuencia)
    tamSecuencia = len(secuencia)
    cantidadCeros=secuencia.count(0)
    cantidadUnos=tamSecuencia-cantidadCeros
    print(f"Cantidad de ceros: {cantidadCeros}")
    print(f"Cantidad de unos: {cantidadUnos}")
    corridas = []
    for i in range(1, tamSecuencia):
        if secuencia[i] == secuencia[i - 1]:
            corridas.append(0)
        else:
            corridas.append(1)
    corridas.insert(0, 1)
    numCorridasAMM = corridas.count(1)
    print(f"Numero de corridas: {numCorridasAMM}")
    valorEsperadoAAM = ((2 * cantidadCeros*cantidadUnos ) / tamañoAAM)+(1/2)
    varianzaAAM = ((2 * cantidadCeros*cantidadUnos)*((2*cantidadCeros*cantidadUnos)-tamañoAAM)) / ((tamañoAAM**2)*(tamañoAAM-1))
    Z0AAM = (numCorridasAMM - valorEsperadoAAM) / math.sqrt(varianzaAAM)

    dataCAA = [['NÚMEROS 0: ', cantidadCeros],
               ['NÚMEROS 1: ', cantidadUnos],
               ['NUMERO DE CORRIDAS: ', numCorridasAMM],
                ['VALOR ESPERADO: ', valorEsperadoAAM],
                ['VARIANZA: ', varianzaAAM],
                ['ESTADÍSTICO Z0: ', Z0AAM]]
    print('\n--RESULTADO--')
    print(tabulate(dataCAA, tablefmt="fancy_grid"))

    if -ZalfaAAM < Z0AAM < ZalfaAAM:
        print("\n no se puede rechazar que el conjunto de r. es independiente.")
    else:
        print("\nLos números del conjunto Ri no son independientes")

corridasAAM(corridAAM,1.96)