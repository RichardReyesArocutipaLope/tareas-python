import math
import numpy
from tabulate import tabulate

pokerr = [0.69440, 0.21910, 0.80040, 0.06400, 0.40960, 0.77720, 0.40390, 0.31350, 0.82820, 0.59150, 0.98720, 0.45630, 0.82090, 0.38760, 0.23300, 0.54280, 0.46310,
          0.44610, 0.90050, 0.09000, 0.81000, 0.61000, 0.21000, 0.41000, 0.81000, 0.61000, 0.21000, 0.41000, 0.81000, 0.61000]

pokerlibro=[
0.06141,
0.81792,
0.52953,
0.04127,
0.27813,
0.72484,
0.48999,
0.50502,
0.67347,
0.62182,
0.94107,
0.18590,
0.30444,
0.28103,
0.82578,
0.56766,
0.06060,
0.70688,
0.99367,
0.85923,
0.14411,
0.11223,
0.25357,
0.44598,
0.51483,
0.87648,
0.64794,
0.31555,
0.73997,
0.09099]


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

poker5(pokerlibro,12.592)