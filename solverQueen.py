import time
import technique
import tracemalloc

EXEC_MOYEN = 100

def printStats(nbExect,nomTech,nomFonction):
    print("\nTechnique",nomTech,":")
    result = []
    print("nb reines|    temps min    |    temps max    |  temps moyen    |      memory      |")
    for n in range(10,13):
        timeAverate = 0
        memoryAverate = 0.0
        min = n**n
        max = 0.0
        for times in range(nbExect):
            tracemalloc.start()
            startTime = time.process_time()
            nomFonction(n)
            endTime = time.process_time()
            memoryAverate += float(tracemalloc.get_traced_memory()[1])
            tracemalloc.stop()
            cpuTime = endTime - startTime
            if cpuTime < min:
                min = cpuTime
            elif cpuTime > max:
                max = cpuTime
            timeAverate += cpuTime
        result = [n,min,max,timeAverate/nbExect,memoryAverate/nbExect]
        for elt in result:
            print("    ",f"{elt:.6f}" if type(elt)==float else elt,"  |",end=" ")
        print()

choix = None
while choix != "Q":
    print("\n----- Resolution Problème des Reines -----")
    print(" - R : technique par aléatoire")
    print(" - I : technique d'incrémentation'")
    print(" - Q : Quitter")
    choix = input("Sélection technique ?").upper()
    if choix == "Q" :
        print("Merci")
    elif choix == "R":
        printStats(EXEC_MOYEN,"aléatoire",technique.solverRandom)
    elif choix == "I":
        printStats(EXEC_MOYEN,"Incrémentation",technique.BruteForce)
    elif choix == "B":
        printStats(EXEC_MOYEN,"Backtracking")
    else :
        print("entrer érronner")