#coding:utf-8

chaine = "Bonjour tout le monde"
chaine = chaine.upper()
print(chaine)
chaine = chaine.lower()
print(chaine)
chaine = chaine.capitalize()
print(chaine)
chaine = chaine.title()
print(chaine)

print(chaine.find("tout"))
print(chaine.find("Tout"))
# print(chaine.index("tout")) # Va afficher une erreur
print(chaine.index("Tout"))




chaine2 = "ababababa"
print(chaine2)
chaine2 = chaine2.replace("a", "z")
print(chaine2)



chaine3 = "Salut les gars"
chaine4 = "9875"

print(chaine3.isascii())
print(chaine4.isascii())
print(chaine3.isdigit())
print(chaine4.isdigit())



chaine5 = "class"
print(chaine5.isidentifier())



chaine6 = "Le langage python"
if "langage" in chaine6: # Recherche une chaine dans une chaine
    print("Trouvé")
else:
    print("Non trouvé")

chaine6.split(" ") # On decoupe la chaine par rapport au espace, ça devient une liste
print(chaine6) 