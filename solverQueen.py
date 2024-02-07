import time
import random
import technique

EXEC_MOYEN = 200

def printStats(nbExect,nomTech,nomFonction):
    print("\nTechnique",nomTech,":")
    result = []
    print("nb reines|    temps min    |    temps max    |  temps moyen    |")
    for n in range(4,12):
        timeAverate = 0
        min = n**n
        max = 0.0
        for times in range(nbExect):
            startTime = time.process_time()
            nomFonction(n)
            endTime = time.process_time()
            cpuTime = endTime - startTime
            if cpuTime < min:
                min = cpuTime
            elif cpuTime > max:
                max = cpuTime
            timeAverate += cpuTime
        result = [n,min,max,timeAverate/nbExect]
        for elt in result:
            print("    ",f"{elt:.6f}" if type(elt)==float else elt,"  |",end=" ")
        print()

choix = None
while choix != "Q":
    print("\n----- Resolution Problème des Reines -----")
    print(" - R : technique par aléatoire")
    print(" - B : technique Backtracking")
    print(" - Q : Quitter")
    choix = input("Sélection technique ?").upper()
    if choix == "Q" :
        print("Merci")
    elif choix == "R":
        printStats(EXEC_MOYEN,"aléatoire",technique.solverRandom)
    elif choix == "B":
        printStats(EXEC_MOYEN,"forcing",technique.forcing)
        #afficheStatsBacktracking(EXEC_MOYEN)
    else :
        print("entrer érronner")