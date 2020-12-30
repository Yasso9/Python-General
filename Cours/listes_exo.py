# .Soient les listes suivantes :
# t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,
# ' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]
# Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les éléments des deux listes en les alternant, de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant : [ ' Janvier ' ,31, ' Février ' ,28, ' Mars ' ,31, etc...].

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' , ' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]

t3 = []

i = 0
while(i < len(t1)):
    t3.append(t2[i])
    t3.append(t1[i])
    i = i + 1
print(t3)

# .Écrivez un programme qui affiche « proprement » tous les éléments d'une liste. Si on l'appliquait par exemple à la liste t2 de l'exercice ci-dessus, on devrait obtenir :
# Janvier Février Mars Avril Mai Juin Juillet Août Septembre Octobre Novembre Décembre

i = 0
while(i < len(t2)):
    print(t2[i], end = "")
    i = i + 1

# .Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. Par exemple, si on l'appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait afficher :
# le plus grand élément de cette liste a la valeur 75.

liste = [32, 5, 12, 8, 3, 75, 2, 15]
max = liste[0]

i = 1
while(i < len(liste)):
    if(liste[i] > max):
        max = liste[i]
    i = i + 1
print('\n', max)

# .Écrivez un programme qui analyse un par un tous les éléments d'une liste de nombres (par exemple celle de l'exercice précédent) pour générer deux nouvelles listes. L'une contiendra seulement les nombres pairs de la liste initiale, et l'autre les nombres impairs. Par exemple, si la liste initiale est celle de l'exercice précédent, le programme devra construire une liste pairs qui contiendra [32, 12, 8, 2], et une liste impairs qui contiendra [5, 3, 75, 15]. Astuce : pensez à utiliser l'opérateur modulo (%) déjà cité précédemment.

liste_pair = []
liste_impair = []

i = 0
while(i < len(liste)):
    if(liste[i] % 2 == 0):
        liste_pair.append(liste[i])
    else:
        liste_impair.append(liste[i])
    i = i + 1
print(liste_pair, '\n', liste_impair)

# .Écrivez un programme qui analyse un par un tous les éléments d'une liste de mots (par exemple : [ ' Jean ' , ' Maximilien ' , ' Brigitte ' , ' Sonia ' , ' Jean-Pierre ' , ' Sandra ' ] ) pour générer deux nouvelles listes. L'une contiendra les mots comportant moins de 6 caractères, l'autre les mots comportant 6 caractères ou davantage.

words = [ 'Jean' , 'Maximilien' , 'Brigitte' , 'Sonia' , 'Jean-Pierre' , 'Sandra' ]

short_words = []
long_words = []

i = 0
while(i < len(words)):
    if(len(words[i]) < 6):
        short_words.append(words[i])
    else:
        long_words.append(words[i])
    i = i + 1
print(short_words, '\n', long_words)