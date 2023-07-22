import math
import numpy
from tabulate import tabulate
def pruebaDeMedias(valoresDM,ZDM):
    tamañoPruMed=len(valoresDM)
    promedioPruMed=sum(valoresDM)/len(valoresDM)
    limiteInferiorDM=(1/2)-(ZDM*(1/math.sqrt(12*tamañoPruMed)))
    limiteSuperiorDM=(1/2)+(ZDM*(1/math.sqrt(12*tamañoPruMed)))
    dataDM=[['PROMEDIO: ',promedioPruMed],
            ['LIMITE INFERIOR',limiteInferiorDM],
            ['LIMITE SUPERIOR',limiteSuperiorDM]]
    print('\n--RESULTADO--')
    print(tabulate(dataDM,tablefmt="fancy_grid"))

    if limiteInferiorDM<promedioPruMed<limiteSuperiorDM:
        print("\nNo se puede rechazar que el conjunto de datos tiene un valor esperado de 0.5")
    else:
        print("\nSe rechaza que el conjunto de datos tenga un valor esperado de 0.5")

def pruebaDeVarianza(valoresPV,chiAlfaM,chiUnomenosAlfaM):
    tamañoPV=len(valoresPV)
    varianzaPV=numpy.var(valoresPV)
    limiteInferiorPV = chiUnomenosAlfaM / (12 * (tamañoPV - 1))
    limiteSuperiorPV = chiAlfaM/(12*(tamañoPV-1))


    dataPV=[['VARIANZA: ',varianzaPV],
            ['LIMITE INFERIOR',limiteInferiorPV],
            ['LIMITE SUPERIOR',limiteSuperiorPV]]
    print('\n--RESULTADO--')
    print(tabulate(dataPV,tablefmt="fancy_grid"))

    if limiteInferiorPV < varianzaPV < limiteSuperiorPV:
        print("\nNo se puede rechazar que el conjunto de datos tiene un valor esperado de 1/12")
    else:
        print("\nSe rechaza que el conjunto de datos tenga un valor esperado de 1/12")

def algoritmoLineal(cantidad,semilla,a,c,m):
    numaleatorios = []
    for i in range(cantidad):
        semilla = (a * semilla + c) % m
        r1 = f'{(semilla / (m - 1)):.4f}'
        r2 = float(r1)
        numaleatorios.append(r2)
    imprimir(numaleatorios)
    return numaleatorios

def algoritmoLineal5(cantidad5,semilla5,a5,c5,m5):
    numaleatorios5 = []
    for i in range(cantidad5):
        semilla5 = (a5 * semilla5 + c5) % m5
        r15 = f'{(semilla5 / (m5 - 1)):.5f}'
        r25 = float(r15)
        numaleatorios5.append(r25)
    imprimir(numaleatorios5)
    return numaleatorios5

def corridasCAA(lista,ZalfaM):
    tamañoCAA=len(lista)
    secuencia=[]
    for i in range(1,tamañoCAA):
        if lista[i]>lista[i-1]:
            secuencia.append(1)
        else:
            secuencia.append(0)

    tamSecuencia=len(secuencia)
    corridas=[]

    for i in range(1,tamSecuencia):
        if secuencia[i]==secuencia[i-1]:
            corridas.append(0)
        else:
            corridas.append(1)
    corridas.insert(0,1)
    numCorridas = corridas.count(1)
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
        print("\nLos números del conjunto Ri son independientes")
    else:
        print("\nLos números del conjunto Ri no son independientes")

def poker5(listnum, chiAlfaMenos):
    tamañoPoker5=len(listnum)
    diferente=0
    par=0
    dosPar=0
    terciaPar=0
    tercia=0
    poker=0
    quintilla=0
    for i in range(tamañoPoker5):
        probar=f'{listnum[i]:.5f}'
        eval=list(str(probar))
        eval.pop(0)
        eval.pop(0)
        if len(eval)==len(set(eval)):
            diferente+=1
        elif len(set(eval))==1:
            quintilla+=1
        elif len(set(eval))==2:
            seet = list(set(eval))
            if eval.count(seet[0]) > 3 or eval.count(seet[1]) >3:
                poker+= 1
            else:
                terciaPar+=1
        elif len(set(eval)) == 3:
            seet=list(set(eval))
            if eval.count(seet[0])>2 or eval.count(seet[1])>2 or eval.count(seet[2])>2:
                tercia +=1
            else:
                dosPar+= 1
        elif len(set(eval)) == 4:
            par+= 1

    probDiferente = tamañoPoker5 * 0.3024
    probPar = tamañoPoker5 * 0.5040
    probDosPar = tamañoPoker5 * 0.1080
    probTerciaPar = tamañoPoker5 * 0.0090
    probTercia = tamañoPoker5 * 0.0720
    probPoker = tamañoPoker5 * 0.0045
    probQuintilla = tamañoPoker5 * 0.0001

    chiDiferente = ((probDiferente - diferente) ** 2) / probDiferente
    chiPar = ((probPar - par) ** 2) / probPar
    chiDosPar = ((probDosPar - dosPar) ** 2) / probDosPar
    chiTerciaPar = ((probTerciaPar - terciaPar) ** 2) / probTerciaPar
    chiTercia = ((probTercia - tercia) ** 2) / probTercia
    chiPoker = ((probPoker - poker) ** 2) / probPoker
    chiQuintilla = ((probQuintilla - quintilla) ** 2) / probQuintilla
    #estadistico de prueb
    chi = chiDiferente + chiPar + chiDosPar + chiTerciaPar + chiTercia + chiPoker + chiQuintilla

    data = [['Todos diferentes (TD)', diferente, 0.3024, probDiferente, chiDiferente],
            ['1 par(1P)', par, 0.5040, probPar, chiPar],
            ['2 par (2P)', dosPar, 0.1080, probDosPar, chiDosPar],
            ['1 tercia 1 par(TP)', terciaPar, 0.009, probTerciaPar, chiTerciaPar],
            ['Tercia (T)', tercia, 0.0720, probTercia, chiTercia],
            ['Poker (P)', poker, 0.0045, probPoker, chiPoker],
            ['Quintilla (Q)', quintilla, 0.0001, probQuintilla, chiQuintilla],
            ['TOTAL', tamañoPoker5, '', 'X^2(0)', chi]]

    print(tabulate(data, headers=['CATEGORIA', 'O(i)', 'PROBABILIDAD', 'E(i)', 'X^2(0)'], tablefmt="fancy_grid"))
    if chi < chiAlfaMenos:#
        print("\nNo se puede rechazar la independencia de los números del conjunto")
    else:
        print("\nSe rechaza la independencia de los números del conjunto")
def chiCudrada(valoresCC):
    pass
def KS(valoresKS):
    pass
def corridasAAM(valoresAAM,ZalfaAAM):
    tamañoAAM = len(valoresAAM)
    secuencia = []
    for i in range(tamañoAAM):
        if valoresAAM[i] > 0.5:
            secuencia.append(1)
        else:
            secuencia.append(0)

    tamSecuencia = len(secuencia)
    cantidadCeros=secuencia.count(0)
    cantidadUnos=tamSecuencia-cantidadCeros
    corridas = []
    for i in range(1, tamSecuencia):
        if secuencia[i] == secuencia[i - 1]:
            corridas.append(0)
        else:
            corridas.append(1)
    corridas.insert(0, 1)
    numCorridasAMM = corridas.count(1)

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
        print("\nLos números del conjunto Ri son independientes")
    else:
        print("\nLos números del conjunto Ri no son independientes")

def elegir(nombre):

    print(f'''--------------------------------------------------
                Prueba {nombre}

    1--Generar numeros
    2--Insertar numeros manualmente
    3--Probar con numeros ya definidos
    ''')
    ele= input('Elija una opción: ')
    print('\n')
    return ele

def imprimir(lista):
    contador=0
    for i in range(len(lista)):
        print(lista[i],end='   ')
        contador+=1
        if contador==10:
            print('\n')
            contador=0

def crear():
    cantid=int(input("Ingrese la cantidad de numeros: "))
    listNew = []
    for i in range(cantid):
        dat = float(input("-"))
        listNew.append(dat)
    imprimir(listNew)
    return listNew


prueba = [0.0449, 0.6015, 0.63, 0.5514, 0.0207, 0.1733, 0.6694, 0.2531, 0.0316, 0.1067, 0.5746, 0.3972, 0.8297, 0.3587,0.3857, 0.049, 0.7025,0.6483, 0.7041, 0.1746, 0.8406,
          0.1055, 0.6972, 0.5915, 0.3362, 0.8349, 0.1247, 0.9582, 0.2523, 0.1589, 0.92,0.1977, 0.9085, 0.2545, 0.3727,0.2564, 0.0125, 0.8524, 0.3044, 0.4145]

pokerr = [0.69440, 0.21910, 0.80040, 0.06400, 0.40960, 0.77720, 0.40390, 0.31350, 0.82820, 0.59150, 0.98720, 0.45630, 0.82090, 0.38760, 0.23300, 0.54280, 0.46310,
          0.44610, 0.90050, 0.09000, 0.81000, 0.61000, 0.21000, 0.41000, 0.81000, 0.61000, 0.21000, 0.41000, 0.81000, 0.61000]

datos = [0.34, 0.83, 0.96, 0.47, 0.79, 0.99, 0.37, 0.72, 0.06, 0.18, 0.67, 0.62, 0.05, 0.49, 0.59, 0.42, 0.05, 0.02, 0.74, 0.67, 0.46, 0.22, 0.99, 0.78, 0.39,
         0.18, 0.75, 0.73, 0.79, 0.29, 0.11, 0.19, 0.58, 0.34, 0.42, 0.37, 0.31, 0.73, 0.74, 0.21, ]

AAAM=[0.809,0.042,0.432,0.538,0.225,0.88,0.688,0.772,0.036,0.854,0.397,0.268,0.821,0.897,0.07,0.721,0.087,0.35,0.779,0.482,
0.136,0.855,0.453,0.197,0.444,0.799,0.809,0.691,0.545,0.857,0.692,0.055,0.348,0.373,0.436,0.29,0.015,0.834,0.599,0.724,
0.564,0.709,0.946,0.754,0.677,0.128,0.012,0.498,0.6,0.913]

print(
f'''
--------------------------------------------------
                PRUEBAS DE ALEATORIEDAD
    1--Prueba de las medias.
    2--Prueba de varianza.
    3--Prueba Chi-cuadrada.
    4--Prueba K-S.
    5--Prueba de corridas arriba y abajo.
    6--Prueba de corridas arriba y abajo de la media.
    7--Prueba de Poker.
''')
opcion=input('Elija una opción: ')
print('--------------------------------------------------')
if opcion == '1':
    nombre='de las medias'
    a=elegir(nombre)
    if a=='1':
        ZDM=float(input("Digite Z α/2: "))
        cantidad=int(input("Digite la cantidad de numeros: "))#50
        semilla=float(input("Digite la semilla: "))#37
        pruebaDeMedias(algoritmoLineal(cantidad,semilla, 19, 33, 80),ZDM)
    elif a=='2':
        ZDM = float(input("Digite Z α/2: "))
        pruebaDeMedias(crear(),ZDM)
    elif a=='3':
        ZDM = float(input("Digite Z α/2: "))
        imprimir(prueba)
        pruebaDeMedias(prueba,ZDM)

elif opcion == '2':
    nombre = 'de varianza'
    b=elegir(nombre)
    if b=='1':
        chiAlfaM= float(input("Digite X^2 (α/2,n-1): "))
        chiUnomenosAlfaM= float(input("Digite X^2 (1-α/2,n-1): "))
        cantidad=int(input("Digite la cantidad de numeros: "))#50
        semilla=float(input("Digite la semilla: "))#37
        pruebaDeVarianza(algoritmoLineal(cantidad,semilla, 19, 33, 80),chiAlfaM,chiUnomenosAlfaM)
    elif b=='2':
        chiAlfaM = float(input("Digite X^2 (α/2,n-1): "))
        chiUnomenosAlfaM = float(input("Digite X^2 (1-α/2,n-1): "))
        pruebaDeVarianza(crear(),chiAlfaM, chiUnomenosAlfaM)
    elif b=='3':
        chiAlfaM = float(input("Digite X^2 (α/2,n-1): "))
        chiUnomenosAlfaM = float(input("Digite X^2 (1-α/2,n-1): "))
        imprimir(prueba)
        pruebaDeVarianza(prueba,chiAlfaM, chiUnomenosAlfaM)

elif opcion == '3':
    nombre = 'Chi-cuadrada'
    c = elegir(nombre)
    if c == '1':
        cantidad = int(input("Digite la cantidad de numeros: "))  # 50
        semilla = float(input("Digite la semilla: "))  # 37
        chiCudrada(algoritmoLineal(cantidad, semilla, 19, 33, 80))
    elif c == '2':
        chiCudrada(crear())
    elif c == '3':
        imprimir(prueba)
        chiCudrada(prueba)

elif opcion == '4':
    nombre = 'K-S'
    d = elegir(nombre)
    if d == '1':
        cantidad = int(input("Digite la cantidad de numeros: "))  # 50
        semilla = float(input("Digite la semilla: "))  # 37
        KS(algoritmoLineal(cantidad, semilla, 19, 33, 80))
    elif d == '2':
        KS(crear())
    elif d == '3':
        imprimir(prueba)
        KS(prueba)
elif opcion == '5':
    nombre = 'corridas arriba y abajo'
    e = elegir(nombre)
    if e == '1':
        ZalfaM = float(input("Digite Z α/2: "))
        cantidad = int(input("Digite la cantidad de numeros: "))  # 50
        semilla = float(input("Digite la semilla: "))  # 37
        corridasCAA(algoritmoLineal(cantidad, semilla, 19, 33, 80),ZalfaM)
    elif e == '2':
        ZalfaM = float(input("Digite Z α/2: "))
        corridasCAA(crear(),ZalfaM)
    elif e == '3':
        ZalfaM = float(input("Digite Z α/2: "))
        imprimir(datos)
        corridasCAA(datos,ZalfaM)

elif opcion == '6':
    nombre = 'de corridas arriba y abajo de la media'
    f = elegir(nombre)
    if f == '1':
        ZalfaAAM = float(input("Digite Z α/2: "))
        cantidad = int(input("Digite la cantidad de numeros: "))  # 50
        semilla = float(input("Digite la semilla: "))  # 37
        corridasAAM(algoritmoLineal(cantidad, semilla, 19, 33, 80),ZalfaAAM)
    elif f == '2':
        ZalfaAAM = float(input("Digite Z α/2: "))
        corridasAAM(crear(),ZalfaAAM)
    elif f == '3':
        ZalfaAAM = float(input("Digite Z α/2: "))
        imprimir(AAAM)
        corridasAAM(AAAM,ZalfaAAM)
elif opcion == '7':
    nombre = 'de Poker'
    g = elegir(nombre)
    if g == '1':
        chiAlfaMenos = float(input("Digite X α,m-1: "))
        cantidad5 = int(input("Digite la cantidad de numeros: "))  # 50
        semilla5 = float(input("Digite la semilla: "))  # 37
        poker5(algoritmoLineal5(cantidad5, semilla5, 19, 33, 80), chiAlfaMenos)
    elif g == '2':
        chiAlfaMenos = float(input("Digite X α,m-1: "))
        poker5(crear(), chiAlfaMenos)
    elif g == '3':
        chiAlfaMenos = float(input("Digite X α,m-1: "))#
        imprimir(pokerr)
        poker5(pokerr, chiAlfaMenos)














