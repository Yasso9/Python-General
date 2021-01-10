def creation_instruction(systemFinal, angle, taille):
    chaine = "from turtle import *\n"
    # On creer un tableau qui va contenir des positions pour les crochets
    chaine = chaine + "tableau_position = [];\n"
    # On met d'autres instructions utile
    chaine = chaine + "speed(0);\n"
    chaine = chaine + "color('black');\n"
    for caractere in systemFinal:
        if(caractere == 'a'):
            chaine = chaine + 'pendown(); forward({});\n'.format(taille)
        elif(caractere == 'b'):
            chaine = chaine + 'penup(); forward({});\n'.format(taille)
        elif(caractere=='+'):
            chaine = chaine + 'right({});\n'.format(angle)
        elif(caractere=='-'):
            chaine = chaine + 'left({});\n'.format(angle)
        elif(caractere=='*'):
            chaine = chaine + 'right(180);\n'
        elif(caractere=='['):
            # On rajoute au tableau la position actuel de la tortue
            chaine = chaine + 'tableau_position.append(position());\n'
        elif(caractere==']'):
            # On donne la position du dernier crochet ouvert
            chaine = chaine + 'setposition(tableau_position[-1]);\n'
            # On supprime cette élément pour permettre au prochain 
            # crochet de récuperer le denrier caractère de la liste
            chaine = chaine + 'tableau_position.pop();\n'
        else:
            print("Ce message ne devrait jamais arrivé")
            raise ValueError

    chaine = chaine + "exitonclick();"

    return chaine

def creation_fichier(chaine, fichier):
    with open("fichier", "w") as fichier:
        fichier.write(chaine)

if __name__ == "__main__":
    chaine = creation_instruction("---++aa++aa++", 60, 5)
    print(chaine)

    chaine = creation_instruction("bbb[b-a]aaa", 60, 5)
    print(chaine)

    chaine = creation_instruction("a[b[-]a]", 60, 5)
    print(chaine)