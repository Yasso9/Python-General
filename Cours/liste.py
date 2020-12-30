# Creation d'une liste
inventaire = list() # vide
inventaire = [] # vide
inventaire = [9, 8, "voiture"]
inventaire = [0] * 10

# print(inventaire)
print(inventaire[:]) # Afficher toute la liste

inventaire = range(0, 20)

# Première façon d'afficher
# i = 0
# while i < len(inventaire):
#     print(inventaire[i])

# Deuxième façon d'afficher
# for valeur in inventaire:
#     print(valeur)


inventaire = ["arc", "Epée", "bouclier", "potion", "flèche", "tunique"]
print(inventaire[:2]) # On affiche les deux premier element de la liste
print(inventaire[3:]) # On affiche les elements de la liste a partir de l'element 3
print(inventaire[-3]) # Affiche le troisième élement en partant de la fin
print(inventaire[-1]) # On affiche le dernier élément
print(inventaire[2:5]) # Affiche l'element deux jusque'à l'élement 4 inclus

inventaire[2] = "bouclier d'acier" # Modification d'un élement
print(inventaire[:])

inventaire[:] = ["objet"] * len(inventaire) # Modif de pls élement
print(inventaire[:])

if "objet" in inventaire: # Recherche dans une liste
    print("Il y a un objet dans l'inventaire")
else:
    print("Il n'y a pas d'objet dans l'inventaire")

inventaire = []

inventaire.append("arc") # Rajout d'element dans la liste
print(inventaire[:])
inventaire.append("bouclier")

inventaire.insert(1, "manteau") # Insert un element à la position 1
print(inventaire[:])

inventaire.remove("bouclier") # Supprime l'element "bouclier"
print(inventaire[:])

del inventaire[-1] # Supprime le dernier element
print(inventaire[:])



inventaire = [5, 128, 6, 5, 200, -7, -5, 5, 5, 0]
inventaire.sort()
print(inventaire[:])
inventaire.reverse()
print(inventaire[:])

print("Nombre de 5 : ", inventaire.count(5))

inventaire.clear() # Efface la liste
inventaire[:] = [] # Efface la liste




inventaire = ["Bonjour", "à", "tous"]
phrase = " ".join(inventaire) # On rejoins la liste en mettant des espaces entre chaque membre
print(phrase)




import copy

liste1 = ["arc", "bouclier", "tunique"]
liste2 = liste1 # Ne fais pas de copy, c'est une reference
liste2 = copy.deepcopy(liste1)

print("Liste 1 : ", liste1[:])
print("Liste 2 : ", liste2[:])

liste2.append("potion")

print("Liste 1 : ", liste1[:])
print("Liste 2 : ", liste2[:])