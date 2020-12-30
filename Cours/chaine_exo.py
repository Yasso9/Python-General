# .Écrivez un script qui compte le nombre d'occurrences du caractère « e » dans une chaîne.

chaine1 = "Ouech les amise"

i = 0 
compteur = 0
while(i < len(chaine1)):
    if (chaine1[i] == 'e'):
        compteur = compteur + 1
    i = i + 1
print(compteur)

# .Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des astérisques 
# entre les caractères. Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »

chaine2 = "bonjour"

i = 0
asterisques = ""
while(i < len(chaine2)):
    asterisques = asterisques + chaine2[i]
    if(i != len(chaine2)-1):
        asterisques = asterisques + '*'
    i = i + 1
print(asterisques)

# .Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l'inversant.
# Ainsi par exemple, « zorglub » deviendra « bulgroz ».

chaine3 = "radar"
inverse = ""

i = len(chaine3)-1
while(i >= 0):
        inverse = inverse + chaine3[i]
        i = i - 1
print(chaine3)

# .En partant de l'exercice précédent, écrivez un script qui détermine si une chaîne de caractères 
# donnée est un palindrome (c'est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), 
# comme par exemple « radar » ou « s.o.s ».

if(chaine3 == inverse):
    print("Le mot", chaine3, "est un palindrome")