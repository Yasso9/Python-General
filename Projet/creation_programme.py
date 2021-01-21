#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def creation_instruction(axiomeFinal, angle, taille, vitesse, couleur, position, epaisseur):
    """Met dans une chaine de caractère toute les instructions que le programme turtle doit executer"""
    chaine = "#!/usr/bin/env python3\n#-*- coding: utf-8 -*-\n"
    chaine = chaine + "from turtle import *\n"
    # On creer une liste qui va contenir des positions et des angles pour les crochets
    chaine = chaine + "tableauPositionEtAngle = [];\n"

    chaine = chaine + "speed({});\n".format(taille)
    chaine = chaine + "colormode(255); pencolor({});\n".format( (int(couleur[0]), int(couleur[1]), int(couleur[2])) )
    chaine = chaine + "penup(); setposition({}); pendown();\n".format(position)
    chaine = chaine + "pensize({});\n".format(epaisseur)

    # On écrit le programme en fonction de chacun des symboles
    for caractere in axiomeFinal:
        if(caractere == "a"):
            chaine = chaine + "pendown(); forward({});\n".format(taille)
        elif(caractere == "b"):
            chaine = chaine + "penup(); forward({});\n".format(taille)
        elif(caractere=="+"):
            chaine = chaine + "right({});\n".format(angle)
        elif(caractere=="-"):
            chaine = chaine + "left({});\n".format(angle)
        elif(caractere=="*"):
            chaine = chaine + "right(180);\n"
        elif(caractere=="["):
            # On rajoute au tableau la position actuel de la tortue et son angle
            chaine = chaine + "tableauPositionEtAngle.append([position(), heading()]);\n"
        elif(caractere=="]"):
            # On donne la position et l'angle du dernier crochet ouvert
            chaine = chaine + "penup(); setposition(tableauPositionEtAngle[-1][0]); setheading(tableauPositionEtAngle[-1][1]); pendown();\n"
            # On supprime cette élément pour permettre au prochain 
            # crochet de récuperer les derniers éléments de la liste
            chaine = chaine + "tableauPositionEtAngle.pop();\n"
        else:
            raise ValueError("Else de creation_instruction utilisé (n'arrive jamais si 'lecture_fichier' a été fait avant)")

    # Pour pouvoir laisser le dessin final tant que l"utilisateur ne clique pas
    chaine = chaine + "exitonclick();"

    return chaine

def creation_fichier(chaine, nomfichier):
    """Créer ou remplace la chaine d'un fichier par une autre chaine"""
    with open(nomfichier, "w") as fichier:
        fichier.write(chaine)


# Partie qui permet d'utiliser ce scripts séparement si vous voulez verifier sa qualité

if __name__ == "__main__":
    axiome = "---++aa++aa++"
    chaine = creation_instruction(axiome, 60, 5, 0, (0, 0, 0), (100, 100), 2)
    print("Axiome final : {}\n\nChaine d'instruction : \n\n\n{}".format(axiome, chaine))

    axiome = "bbb[b-a]aaa"
    chaine = creation_instruction(axiome, 60, 5, 0, (0, 0, 0), (100, 100), 2)
    print("Axiome final : {}\n\nChaine d'instruction : \n\n\n{}".format(axiome, chaine))

    axiome = "a[b[-]a]"
    chaine = creation_instruction(axiome, 60, 5, 0, (0, 0, 0), (100, 100), 2)
    print("Axiome final : {}\n\nChaine d'instruction : \n\n\n{}".format(axiome, chaine))

    axiome = "a*a*b*b"
    chaine = creation_instruction(axiome, 60, 5, 0, (0, 0, 0), (100, 100), 2)
    print("Axiome final : {}\n\nChaine d'instruction : \n\n\n{}".format(axiome, chaine))