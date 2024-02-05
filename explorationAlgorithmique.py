from tkinter import *
import time
import mygraph as mg

# Dimension de la taille de l'échiquier
SIZE = 8

def initGraph(grille = []):
    """
    Initialise le graphe de l'échiquier 
    avec l'ensemble des possibilités des arrêtes 
    possibles entre chaque sommet

    renvoie :
    ---------
    graph : mygraph.Graphe2
    graphe de l'échiquier
    """
    graph = mg.Graphe2()
    return graph


def main(graph = initGraph(),depart = "A0"):
    """
    Programme principale du solver
    Utilise l'ensemble des techniques pour mener 
    à la vitesse la plus rapide

    paramètre :
    -----------
    graph : Graph
    Un graphe qui représente l'ensemble
    des cases de l'échiqier
    """
    startTime = time.process_time()
    #ensemble des techniques de résolution
    solver = backtraking(graph, depart)
    endTime = time.process_time()
    cpuTime = endTime - startTime
    print("Temps CPU : ", cpuTime,"secondes")


def backtraking(graph, depart, solver = []) -> list:
    """
    Technique de Backtraking :
    Parcours le graph sommets par sommets
    en cherchant à passer par toutes les cases.
    Si le chemin est bloqué, il retourne en arrière et continue

    Paramètre :
    -----------
    graph : Graphe

    solver : list
    contient le nom des sommets à parcourir dans l'ordre 
    afin de parcourir l'ensemble de case sans repasser
    deux foix par le même sommet

    renvoie :
    ---------
    solver : list
    liste des sommets de solution
    """
    return solver