# Mode d'ouverture : r, w, a, x, r+

fichier = open("texte.txt", "r")

# Récupère tout le fichier
content = fichier.read()
print(content)

# Recuperer une ligne du fichier
line = fichier.readline()
print(line)

# Recupere le reste des lignes
lines = fichier.readlines()
print(lines)

fichier.close()



# Autre methode pour ouvrir ou lire un fichier
with open("texte.txt", "w") as fichier:
    number = 15
    fichier.read(str(number))
    fichier.write("\nBonjour\n")
    fichier.write("Bonjour\n")
    fichier.write("Cercle\n")
    fichier.write("Demain\n")
    fichier.write("Balancoire\n")
    fichier.write("Jouet\n")
    # Pas besoin de close

