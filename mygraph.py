#import networkx
#import graphviz

# coding: utf-8
""" 
Une classe Python pour creer et manipuler des graphes
"""


class Graphe(object):

    def __init__(self, graphe_dict=None):
        """ initialise un objet graphe.
	    Si aucun dictionnaire n'est
	    créé ou donné, on en utilisera un 
	    vide
        """
        if graphe_dict == None:
            graphe_dict = dict()
        self._graphe_dict = graphe_dict

    def aretes(self, sommet):
        """ retourne une liste de toutes les aretes d'un sommet"""
        liste = []
        for i in self._graphe_dict[sommet]:
            liste += [[sommet,i]]
        return liste

    def all_sommets(self):
        """ retourne tous les sommets du graphe """
        return list(self._graphe_dict.keys())

    def all_aretes(self):
        """ retourne toutes les aretes du graphe """
        liste = []
        for i in self.all_sommets():
            liste += self.aretes(i)
        return liste

    def add_sommet(self, sommet):
        """ Si le "sommet" n'set pas déjà présent
	dans le graphe, on rajoute au dictionnaire 
	une clé "sommet" avec une liste vide pour valeur. 
	Sinon on ne fait rien.
        """
        self._graphe_dict[sommet] = {}

    def add_arete(self, arete):
        """ l'arete est de type set, tuple ou list;
            Entre deux sommets il peut y avoir plus
	    d'une arete (multi-graphe)
        """
        for i in range(2):
            ajout = True
            for j in self._graphe_dict[arete[i%2]]:
                if (j == arete[(i+1)%2]):
                    ajout = False
            if (ajout == True):
                self._graphe_dict[arete[i%2]].add(arete[(i+1)%2])

    def trouve_chaine(self, sommet_dep, sommet_arr, chain=[]):
        """cherche toutes les chaines élémentaires des deux sommets"""
        chain.append(sommet_dep)
        if (sommet_arr in self._graphe_dict[sommet_dep]):
            chain += [sommet_arr]
            return chain
        
        elif (sommet_dep in chain[:-1]):
                return chain[:-1]
        
        else:
            for sommet in self._graphe_dict[sommet_dep]:
                if (sommet not in chain):
                    return self.trouve_chaine(sommet, sommet_arr, chain)
        
    def trouve_tous_chemins(self, sommet_dep, sommet_arr, chem=[]):
        """Cherche tous les chemins élémentaires d'un graphe"""

    def __list_aretes(self):
        """ Methode privée pour récupérer les aretes. 
	    Une arete est un ensemble (set)
            avec un (boucle) ou deux sommets.
        """

    def __iter__(self):
        self._iter_obj = iter(self._graphe_dict)
        return self._iter_obj

    def __next__(self):
        """ Pour itérer sur les sommets du graphe """
        return next(self._iter_obj)

    def __str__(self):
        res = "sommets: "
        for k in self._graphe_dict.keys():
            res += str(k) + " "
        res += "\naretes: "
        for arete in self.__list_aretes():
            res += str(arete) + " "
        return res
    
class Graphe2 (Graphe):

    def sommet_degre(self, sommet):
        """renvoie le degré du sommet"""
        return len(self._graphe_dict[sommet])
    
    def trouve_sommet_isole(self):
        """renvoie la liste des sommets isoles"""
        isoles = []
        for i in self.all_sommets():
            if (self.sommet_degre(i) == 0):
                isoles += [i]
        return isoles
    
    def Delta(self):
        """le degre maximum"""
        max = 0
        for i in self.all_sommets():
            if (self.sommet_degre(i) > max):
                max = self.sommet_degre(i)
        return max
    
    def list_degres(self):
        """ calcule tous les degres et renvoie un
        tuple de degres decroissant
        """
        degres = []
        # recherche des degrés
        for i in self.all_sommets():
            degres += [self.sommet_degre(i)]
        # Rangement dans l'ordre décroissant
        for cursor in range(len(degres)):
            for j in range(cursor,len(degres)):
                if (degres[cursor] < degres[j]):
                    temp = degres[j]
                    degres[j] = degres[cursor]
                    degres[cursor] = temp
        return degres
    
    def BFS(self,sommet) -> list:
        res = File()
        file = File([sommet])
        while not file.estVide():
            element = file.defiler()
            res.enfiler(element)
            for voisins in self._graphe_dict[element]:
                if voisins not in res:
                    file.enfiler(voisins)

    
class File:

    def __init__(self,liste = []):
        """Système de File : First in First out"""
        self.elements = liste

    def affiche(self):
        taille = self.longueur()
        for i in range(taille):
            print(self.elements[i],end=" ")
        print()

    def longueur(self) -> int:
        return len(self.elements)

    def estVide(self):
        return self.longueur() == 0

    def enfiler(self,element):
        liste = [element]
        for i in self.elements:
            liste += [i]
        self.elements = liste
        
    def defiler(self):
        return self.elements.pop() if not self.estVide() else print("File vide")