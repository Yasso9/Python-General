# .Écrivez un programme qui convertisse en mètres par seconde et en km/h une vitesse fournie par l'utilisateur en miles/heure. (Rappel : 1 mile = 1609 mètres)

vitesse = input("Donnez la vitesse en miles par heure : ")

vitesse = float(vitesse)
vitesse = vitesse * 1.609
print(vitesse)

# .Écrivez un programme qui calcule le périmètre et l'aire d'un triangle quelconque dont l'utilisateur fournit les 3 côtés.

from math import sqrt, pi

print("Donner la valeur des trois coté du triangle")

a = float(input("Côté 1 = "))
b = float(input("Côté 2 = "))
c = float(input("Côté 3 = "))

d = (a + b + c) / 2
aire = sqrt(d * (d-a) * (d-b) * (d-c))

print(d*2, aire)

# .Écrivez un programme qui calcule la période d'un pendule simple de longueur donnée.

l = float(input("Longueur du pendule : "))
g = float(input("Accélération de la pensenteur : "))

T = 2 * pi * sqrt(l/g)
print(T)

# .Écrivez un programme qui permette d'encoder des valeurs dans une liste. Ce programme devrait fonctionner en boucle, l'utilisateur étant invité à entrer sans cesse de nouvelles valeurs, jusqu'à ce qu'il décide de terminer en frappant <Enter> en guise d'entrée. Le programme se terminerait alors par l'affichage de la liste.

liste = []

liste.append(input("Veuillez entrer une valeur : "))

i = 0
while (liste[i] != ""):
    liste.append(input("Veuillez entrer une valeur : "))
    i = i + 1
del(liste[i])
print(liste)