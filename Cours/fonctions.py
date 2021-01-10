# Démo : utilisation des fonctions du module <math>
 
from math import sqrt, sin, pi
 
nombre = 121
angle = pi/6	   # soit 30°
	  # (la bibliothèque math inclut aussi la définition de pi)
print("racine carrée de", nombre, "=", sqrt(nombre))
print("sinus de", angle, "radians", "=", sin(angle))



def monter():
	global a
	a = a+1
	print(a)

a = 15
monter()
monter()
print(a)



def essai():
   	"Cette fonction est bien documentée mais ne fait presque rien." # Commentaire important qui décrit une fonction
   	print("rien à signaler")

essai()
print(essai.__doc__)



def question(annonce, essais=4, please ='Oui ou non, s.v.p.!'):
	while essais >0:
		reponse = input(annonce)
		if reponse in ('o', 'oui','O','Oui','OUI'):
			return 1
		if reponse in ('n','non','N','Non','NON'):
			return 0

	print(please)
	essais = essais + 1



def oiseau(voltage=100, etat="allumé", action="danser la java"):
	print("Ce perroquet ne pourra pas", action)
	
	print("si vous le branchez sur", voltage, "volts !")
	print("L'auteur de ceci est complètement", etat)

oiseau(etat='givré', voltage=250, action='vous approuver')
oiseau()