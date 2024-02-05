from tkinter import *
import explorationAlgorithmique as exAlgo
import os

#Constante

NAME_FILE = os.path.basename(__file__)
WAY = __file__[:(len(NAME_FILE)+1)*-1]
FONT = "Helvetica"
SIZE = 4

## Couleur
GREY = "#E5E5E5"
WHITE = "#FFFFFF"
BLACK = "#000000"
DARK_GREEN = "#3D9140"

#param 

option_tile = {
    "text": None,
    "relief": "flat",
    "bd": 2,
    "width": 3,
    "height": 1,
    "padx": 20,
    "pady": 20
}

option_button = {
    "foreground": WHITE,
    "background": DARK_GREEN,
    "width": 18,
    "height": 1,
    "font": (FONT, "12"),
    "borderwidth": 4,
    "relief": "ridge"
}

class GridEchiquier:

    def __init__(self,grille = []):
        self.grid = grille
 
    def addEchiquier(self, frame):
        """
        créer un tableau d'échiquier et l'affiche

        paramètres :
        ------------
        frame : tkinter.Frame/tkinter.Canvas
        emplacement de l'échiquier
        """
        for line in range(SIZE):
            tiles_line = {}
            for column in range(SIZE):
                tileColor = WHITE if (line+column)%2 == 0 else BLACK
                tiles_line[f"{chr(line+65)}{column+1}"] = Button(frame,bg = tileColor,command=lambda l=line, c=column: selectStartCavalier(f"{chr(line+65)}{column+1}",self.renvoieGrid()),**option_tile)
            self.grid += [tiles_line]
    
    def removeEchiquier(self, widgets, echiquier):
            """
            Supprime l'échiquier et les widgets qui sont associés au menu

            paramètres :
            ------------
            widgets : list
            liste de widget a supprimé

            echiquier : tkinter.Frame
            frame de l'échiquier
            """
            for column in range(SIZE):
                for key in self.grid[column].keys():
                    self.grid[column][key].grid_forget()
            echiquier.pack_forget()
            for widget in widgets:
                widget.pack_forget()
            # rajoute les boutons du menu
            menuClick()

    def renvoieGrid(self):
        """
        renvoie la grille pour de la manipulation extérieur

        renvoie :
        ---------
        self.grid : list
        ensemble des cases de la grille
        """
        return self.grid

    def afficheEchiquier(self,frame):
        """
        Affiche l'échiquier dans l'interface graphique

        paramètre :
        -----------
        frame : tkinter.Frame
        frame/section où sont rangée les cases de la grille
        """
        for line in range(SIZE):
            for column in range(SIZE):
                self.grid[line][f"{chr(line+65)}{column+1}"].grid(row=line, column=column)
        frame.pack(expand=YES)

def fenetreCavalier():
    """
    création de l'interface graphique pour 
    le problème du cavalier
    """
    echiquier = Canvas(root, bg=DARK_GREEN)
    pbCavalier = Label(root, text="Problème du Cavalier", font=(FONT, "15"), background=DARK_GREEN, foreground=WHITE, pady=15)
    pbCavalier.pack()
    tiles = GridEchiquier()
    tiles.addEchiquier(echiquier)
    tiles.afficheEchiquier(echiquier)
    leave = Button(root,text="EXIT",command=lambda: tiles.removeEchiquier([pbCavalier,leave],echiquier),**option_button)
    leave.pack(expand=YES)

def fenetreQueen():
    pass

def menuClick(function=None):
    """
    Supprime ou rajoute les boutons du menu

    paramètre :
    -----------
    function : function
    fonction 
    """
    # Si les boutons sont présents : True
    if button_cavalier.winfo_ismapped():
        for widget in [button_cavalier,button_queen]:
            widget.pack_forget()
        function() if function is not None else None
    else:
        for widget in [button_cavalier,button_queen]:
            widget.pack()

def selectStartCavalier(depart,grid):
    """
    Lancement du backtracking suivant la case sélectionner comme point de départ

    paramètres :
    ------------
    line : int
    indice de la ligne de la case

    column : int
    indice de la colonne de la case
    """
    exAlgo.main(exAlgo.initGraph(grid),depart)

# Head
root = Tk()
root.title('SAE2.02 - Exploration algorithmique')
root.resizable(height=True, width=True)
root.geometry('1200x700')
root.minsize(700,700)
#root.iconbitmap(f"{WAY}/images/logo_cavalier.ico")

root['bg'] = DARK_GREEN

# Sélection des choix utilisateur
title = Label(root, 
            text="Résolution d'un problème à l'aide d'un graphe", 
            font=(FONT, "20"), 
            background=DARK_GREEN, 
            foreground=WHITE,
            pady=15).pack()


button_cavalier = Button(root,
                        command=lambda : menuClick(fenetreCavalier),
                        text="Problème du Cavalier", 
                        **option_button)
button_cavalier.pack()

button_queen = Button(root,
                      command=lambda : menuClick(fenetreQueen),
                      text="Problème des Reines",
                      **option_button)
button_queen.pack()

root.mainloop()