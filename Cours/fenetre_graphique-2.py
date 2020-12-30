# Petit exercice utilisant la bibliothèque graphique tkinter

from tkinter import Tk, Canvas, Button, LEFT, RIGHT, TOP, BOTTOM
from random import randrange

# les variables suivantes seront utilisées de manière globale :
canvasHeight, canvasWidth = 650, 500
x1, y1, x2, y2 = 10, 10, canvasWidth-10, 10      # coordonnées de la ligne
color = 'dark green'	      # couleur de la ligne

# --- définition des fonctions gestionnaires d'événements : ---
def draw_line():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, color
    can1.create_line(x1, y1, x2, y2, width=2, fill=color)

    # modification des coordonnées pour la ligne suivante :
    y1, y2 = y1+10, y2+10

def draw_rectangle():
    can1.create_oval(50, 50, 200, 200, width=2, outline='black')

def draw_cross():
    "Tracé d'une croix au milieu du canevas can1"
    global canvasHeight, canvasWidth

    can1.create_line((canvasWidth/2)-10, canvasHeight/2, (canvasWidth/2)+10, canvasHeight/2, width=2, fill='red')
    can1.create_line(canvasWidth/2, (canvasHeight/2)-10, canvasWidth/2, (canvasHeight/2)+10, width=2, fill='red')

def change_color():
    "Changement aléatoire de la couleur du tracé"
    global color
    gradient=['purple','green','red','blue','orange','yellow']
    randColor = randrange(6)      # => génère un nombre aléatoire de 0 à 5
    color = gradient[randColor]

#------ Programme principal -------
  
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, background='dark grey', height=canvasHeight, width=canvasWidth)
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Tracer une ligne', command=draw_line)
bou2.pack(side=TOP)
bou3 = Button(fen1, text='Tracer un Rectangle', command=draw_rectangle)
bou3.pack(side=TOP)
bou4 = Button(fen1, text='Viseur', command=draw_cross)
bou4.pack(side=TOP)
bou5 = Button(fen1, text='Autre couleur', command=change_color)
bou5.pack(side=TOP)
 
fen1.mainloop()        # démarrage du réceptionnaire d'événements
 
fen1.destroy()	       # destruction (fermeture) de la fenêtre