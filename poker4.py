import math
import numpy
from tabulate import tabulate

pokerlibro=[


def poker5(listnum, chiAlfaMenos):
    tamañoPoker5=len(listnum)
    diferente=0
    par=0
    dosPar=0
    tercia=0
    poker=0
    for i in range(tamañoPoker5):
        probar=f'{listnum[i]:.4f}'
        eval=list(str(probar))
        eval.pop(0)
        eval.pop(0)
        if len(eval)==len(set(eval)):
            diferente+=1
        elif len(set(eval))==1:
            poker+= 1
        elif len(set(eval)) == 2:
            seet=list(set(eval))
            if eval.count(seet[0])>2 or eval.count(seet[1])>2:
                tercia +=1
            else:
                dosPar+= 1

    probDiferente = tamañoPoker5 * 0.5040
    probPar = tamañoPoker5 * 0.4320
    probDosPar = tamañoPoker5 * 0.0270
    probTercia = tamañoPoker5 * 0.0360
    probPoker = tamañoPoker5 * 0.0010

    chiDiferente = ((probDiferente - diferente) ** 2) / probDiferente
    chiPar = ((probPar - par) ** 2) / probPar
    chiDosPar = ((probDosPar - dosPar) ** 2) / probDosPar
    chiTercia = ((probTercia - tercia) ** 2) / probTercia
    chiPoker = ((probPoker - poker) ** 2) / probPoker
    #estadistico de prueb
    chi = chiDiferente + chiPar + chiDosPar +chiTercia + chiPoker

    data = [['Todos diferentes (TD)', diferente, 0.5040, probDiferente, chiDiferente],
            ['1 par(1P)', par, 0.4320, probPar, chiPar],
            ['2 par (2P)', dosPar, 0.0270, probDosPar, chiDosPar],
            ['Tercia (T)', tercia, 0.0360, probTercia, chiTercia],
            ['Poker (P)', poker, 0.0010, probPoker, chiPoker],
            ['TOTAL', tamañoPoker5, '', 'X^2(0)', chi]]

    print(tabulate(data, headers=['CATEGORIA', 'O(i)', 'PROBABILIDAD', 'E(i)', 'X^2(0)'], tablefmt="fancy_grid"))
    if chi < chiAlfaMenos:#
        print("\nNo se puede rechazar la independencia de los números del conjunto")
    else:
        print("\nSe rechaza la independencia de los números del conjunto")

poker5(pokerlibro,12.592)