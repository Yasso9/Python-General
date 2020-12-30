age = input("Quel age as-tu ? ")

try:
    age = int(age)
except: # Si il y'a une exception
    print("L'age indiqué est incorrect !")
else: # Si il n'y a pas d'exception
    print("Tu as", age, "ans")
finally: # On l'affiche dans tout les cas a la fin, si il y'a une exeption ou pas
    print("FIN DU PROGRAMME")




nb1 = 150
nb2 = input("Choisir le nombre pour diviser : ")

try:
    nb2 = int(nb2)
    print("Resultat = {}".format(nb1 / nb2))
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par zéro.")
except ValueError:
    print("Vous devez entrer un integer.")  
except: # S'affiche si il y'a un autre type d'erreur que les deux d'avant
    print("Valeur incorrecte.")
else:
    print("Bravo, tu as noté un nombre valide")




nb = input("Donnez un nombre : ")
nb = int(input)

if(nb < 10):
    # On peut lever des exceptions quand on le veut pour après pouvoir les catchs
    # On peut même lever des exceptions que l'on pourra créer
    raise ZeroDivisionError("On leve une exeption")




age = input("Quel âge as-tu ? ")

try:
    age = int(age)

    assert age > 18 # Je veux que l'age soit superieur a 25 ans
except AssertionError:
    print("La personne a pas 18 ans donc on l'a kik")