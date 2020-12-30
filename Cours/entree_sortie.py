print("Bonjour", "à", "tous", sep ="*") 
print("Bonjour", "à", "tous", sep ="") 

n=0
while n<6: 
    print("zut", end ="") 
    n = n+1 
print('\n')

prenom = input("Entrez votre prénom : ")
print("Bonjour,", prenom)

print("Veuillez entrer un nombre positif quelconque : ", end=" ")
ch = input()
nn = int(ch)	     # conversion de la chaîne en un nombre entier
print("Le carré de", nn, "vaut", nn**2)

a = input("Entrez une donnée numérique : ")
type(a)
b = float(a)     # conversion de la chaîne en un nombre réel
type(b)