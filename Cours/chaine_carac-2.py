phrase1 = 'les oeufs durs.'
phrase2 = '"Oui", répondit-il,'
phrase3 = "j'aime bien"

print(phrase2, phrase3, phrase1)


txt3 = '"N\'est-ce pas ?" répondit-elle.'
print(txt3)


Salut = "Ceci est une chaîne plutôt longue\n contenant plusieurs lignes \
de texte (Ceci fonctionne\n de la même façon en C/C++.\n \
    Notez que les blancs en début\n de ligne sont significatifs.\n"

print(Salut)


a1 = """
Usage: trucmuche[OPTIONS]
{ -h
  -H hôte
}"""
 
print(a1)


ch = "Christine"
print(ch[0], ch[3], ch[5])


a = ' Petit poisson '
b = ' deviendra grand '
c = a + b
print(c)
print(len(c)) # Taille de la chaine


ch = '8647'
# print(ch + 45) # → *** erreur *** : on ne peut pas additionner une chaîne et un nombre
n = int(ch)
print(n + 65)
