# -*- coding:Utf8 -*-

########################################
# Programme Python type                #
# Auteur : I.Turki, Courdimanche, 2020 #
# licence : Hydra                      #
########################################

########################################
# Importation de fonctions externes    #

from math import sqrt

########################################
# Définition locale de fonctions       #

def occurrences(car, ch):
    "Cette fonction renvoie le \
    nombre de caractères <car> \
    contenus dans la chaîne <ch>"

    nc = 0

    i = 0

    while i < len(ch):

        if ch[i] == car:
            nc = nc + 1
        
        i = i + 1
    
    return nc

########################################
# Corps principal du programme         #

print("Veuillez entrer un nombre :")
nbr = eval(input())

print("Veuillez entrer une phrase : ")
phr = input()
print("Entrez le character à compter : ")
cch = input()

no = occurrences(cch, phr)
rc = sqrt(nbr**3)

print("La racine carré du cube", end = ' ')
print("du nombre fourni vaut", end = ' ')
print(rc)

print("La phrase contient", end = ' ')
print(no, "caractères", cch)