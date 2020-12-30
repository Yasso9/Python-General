# Exercice utilisant la bibliothèque graphique tkinter et le module math
 
from tkinter import Tk, Entry, Label
from math import *

# définition de l'action à effectuer si l'utilisateur actionne
# la touche "enter" alors qu'il édite le champ d'entrée :
 
def evaluer(event):
	chaine.configure(text = "Résultat = " + str(eval(entree.get())))
    
# ----- Programme principal : -----
 
fenetre = Tk()

entree = Entry(fenetre)
entree.bind("<Return>", evaluer)
entree.pack()

chaine = Label(fenetre)
chaine.pack()

fenetre.mainloop()