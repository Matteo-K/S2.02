import time
import random
import technique

EXEC_MOYEN = 200

def afficheStatsRandom(nbExect):
    print("\nTechnique aléatoire :")
    resultat = []
    print("nb reines|    temps min    |    temps max    |  temps moyen    |")
    for n in [4,6,8,10,16,32,64]:
        tempsMoyen = 0
        min = 300000000.0
        max = 0.0
        for times in range(nbExect):
            startTime = time.process_time()
            technique.solverRandom(n)
            endTime = time.process_time()
            cpuTime = endTime - startTime
            if cpuTime < min:
                min = cpuTime
            elif cpuTime > max:
                max = cpuTime
            tempsMoyen += cpuTime
        resultat = [n,min,max,tempsMoyen/nbExect]
        for elt in resultat:
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
        afficheStatsRandom(EXEC_MOYEN)
    elif choix == "B":
        pass
        #afficheStatsBacktracking(EXEC_MOYEN)
    else :
        print("entrer érronner")