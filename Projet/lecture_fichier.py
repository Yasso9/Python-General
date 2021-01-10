#! /usr/bin/env python3
# coding: utf-8
import sys
from exception import ErreurDefinition, DefinitionMultiple, DefinitionManquante, ErreurValeur, ValeurManquante

def isLsystem(caractere):
    if(caractere == 'a' or caractere == 'b' or caractere == '+' or caractere == '-' or 
    caractere == '*' or caractere == '[' or caractere == ']'):
        return True
    else:
        return False

def isRules(caractere):
    if(isLsystem(caractere) or caractere == '='):
        return True
    else:
        return False

def lecture_axiome(chaine, pos_actuel):
    while(chaine[pos_actuel].isspace()):
        if(chaine[pos_actuel] == chaine[-1]):
            raise ErreurValeur("Il n'y a pas de valeur associé à l'axiome")
        pos_actuel += 1

    if(chaine[pos_actuel] != '\"'):
        raise ErreurValeur("La chaine associé à l'axiome doit commencer par des guillemets")
    pos_actuel += 1

    pos_debut = pos_actuel
    while(chaine[pos_actuel] != '\"'):
        if(chaine[pos_actuel] == chaine[-1]):
            raise ErreurValeur("La chaine associé à l'axiome doit se finir par des guillemets")
        if(not(isLsystem(chaine[pos_actuel]))):
            raise ErreurValeur("La chaine associé à l'axiome comporte des caractères non pris en charge")
        pos_actuel += 1
    pos_actuel += 1
    return chaine[pos_debut:pos_actuel-1].strip(), pos_actuel

def lecture_regle(chaine, pos_actuel, regles):
    while(pos_actuel < len(chaine)):
        while(chaine[pos_actuel].isspace()):
            if(chaine[pos_actuel] == chaine[-1]):
                if(len(regles) == 0):
                    raise ErreurValeur("Il n'y a pas de valeur associé à la regle")
                else:
                    return regles , pos_actuel
            pos_actuel += 1

        if(chaine[pos_actuel] != '\"'):
            if(len(regles) == 0):
                raise ErreurValeur("La chaine associé à la règle doit commencer par des guillemets")
            else:
                return regles , pos_actuel
        pos_actuel += 1

        pos_debut = pos_actuel
        while(chaine[pos_actuel] != '\"'):
            if(chaine[pos_actuel] == chaine[-1]):
                raise ErreurValeur("La chaine associé à la règle doit se fermer par des guillemets")
            if(not(isRules(chaine[pos_actuel]))):
                raise ErreurValeur("La chaine associé à la règle comporte des caractères non pris en charge")
            pos_actuel += 1

        regle = chaine[pos_debut:pos_actuel]
        if(not(len(regle) >= 3 and (regle[0] == "a" or regle[0] == "b") and regle[1] == "=")):
            raise ErreurValeur("La synthaxe de la chaine associé à la règle est fausse")
        regles.append(regle)

        # Le caractere actuel est '\"', on passe au carctère suivant
        pos_actuel += 1

    return regles, pos_actuel

def lecture_nombre(definition, chaine, pos_actuel):
    nombre = ""
    while(chaine[pos_actuel].isdigit() or chaine[pos_actuel].isspace()):
        nombre += chaine[pos_actuel]
        if(chaine[pos_actuel] == chaine[-1]):
            pos_actuel += 1
            break # On sort de la boucle pour voir ce qu'on va faire
        pos_actuel += 1
    # Si nombre ne contient de des "space" alors il y'a une erreur (venant du break forcé ou pas)
    if(nombre.isspace()):
        raise ErreurValeur("La valeur associé à {} n'est pas un entier ou est vide".format(definition))
    # On enlève tout les espace du nombre et on le transforme en entier
    return int(nombre.strip()), pos_actuel

def lecture_definition(chaine, pos_actuel):
    # Lecture du premier mot de la ligne (d'une des definitions)
    pos_debut = pos_actuel
    # Dès qu'on arrive a la fin du mot on doit normalement avoir le caractère "="
    while(chaine[pos_actuel] != "="):
        # Le mot de la definition ne doit pas contenir d'autre caractère que 
        # les alphanumeric ou des espaces
        if(not(chaine[pos_actuel].isalpha() or chaine[pos_actuel].isspace())):
            print("valeur", chaine[pos_actuel])
            raise ErreurDefinition("Une définition n'est pas valide, elle contient des caractères qui ne sont pas des lettres : '{}'".format(chaine[pos_debut:pos_actuel]))
        elif(chaine[pos_actuel] == chaine[-1]):
            print(chaine[pos_debut:pos_actuel])
            raise ValeurManquante("Signe '=' manquant, une définition n'est pas valide")
        pos_actuel += 1

    # La position actuel est '=', on passe a celle d'après
    pos_actuel += 1

    # strip nous permet d'enlever tout les caractères inutile 
    # comme les espace, tabulation, saut à la ligne
    # et on met aussi la définition en caractère bas pour pouvoir lire 
    # tout type de casses concernant la police
    return chaine[pos_debut:pos_actuel-1].strip().lower(), pos_actuel

def verif_multiple(nbApparition, apparitionMax = 1):
    if(nbApparition >= apparitionMax):
        raise DefinitionMultiple("Une definition est apparu {} fois alors quelle devrais apparatre que {} fois".format(nbApparition+1, apparitionMax))
    else:
        return nbApparition + 1

def lecture_fichier(chaine):
    # Variables du Lsystem
    axiome = "" # Numero 0 de verif
    regles = [] # Numero 1 de verif
    angle = 0 # Numero 2 de verif
    taille = 0 # Numero 3 de verif
    niveau = 0 # Numero 4 de verif

    # Liste qui permet de verifier le nombre de fois que chaque définition va être appeler
    verif = [0, 0, 0, 0, 0]

    # Position du "curseur" dans lequel on est dans le fichier
    pos_actuel = 0 

    # Les caractères vide au début et à la fin ne nous intérèsse pas
    chaine = chaine.strip()

    # On lit le fichier jusqua la fin
    while pos_actuel < len(chaine):
        definition, pos_actuel = lecture_definition(chaine, pos_actuel) 

        # On effectue les affectations de variables demandé en fonction de la définition
        # Et on vérifie que les definitions ne soit pas déclarer plusieurs fois
        if(definition == "axiome"):
            axiome, pos_actuel = lecture_axiome(chaine, pos_actuel)
            verif[0] = verif_multiple(verif[0])
        elif(definition == "regle" or definition == "regles"):
            regles, pos_actuel = lecture_regle(chaine, pos_actuel, regles)
            verif[1] = verif_multiple(verif[1], 2) # On peut avoir max 2 règles
        elif(definition == "angle"):
            angle, pos_actuel = lecture_nombre(definition, chaine, pos_actuel)
            verif[2] = verif_multiple(verif[2])
        elif(definition == "taille"):
            taille, pos_actuel = lecture_nombre(definition, chaine, pos_actuel)
            verif[3] = verif_multiple(verif[3])
        elif(definition == "niveau"):
            niveau, pos_actuel = lecture_nombre(definition, chaine, pos_actuel)
            verif[4] = verif_multiple(verif[4])
        else:
            raise ErreurDefinition("La définition '{}' n'est pas prise en compte : ".format(definition))

    # Si une des définitions important a été oublié
    if(verif[0] == 0 or verif[2] == 0 or verif[4] == 0):
        raise DefinitionManquante("Il manque une définition essentiel au l-system")

    return axiome, regles, angle, taille, niveau
    
def lecture_final(nomfichier):
    # try:
    with open(nomfichier, "r") as fichier:
        chaine = fichier.read()
        return lecture_fichier(chaine)
    # except ErreurDefinition:
    #     print("Exception lancé : ", sys.exc_info()[1])
    # except DefinitionMultiple:
    #     print("Exception lancé : ", sys.exc_info()[1])
    # except DefinitionManquante:
    #     print("Exception lancé : ", sys.exc_info()[1])
    # except ErreurValeur:
    #     print("Exception lancé : ", sys.exc_info()[1])
    # except ValeurManquante:
    #     print("Exception lancé : ", sys.exc_info()[1])
    # except:
    #     print("Exception lancé : ", sys.exc_info()[1])
    return "", [], 0, 0, 0

if __name__ == "__main__":
    axiome = ""
    regles = [] 
    angle = 0
    taille = 0
    niveau = 0

    axiome, regles, angle, taille, niveau = lecture_final("lsystem.txt")

    print("axiome : \"{}\"".format(axiome))
    for regle in regles:
        print("regle : \"{}\"".format(regle))
    print("angle : \"{}\"".format(angle))
    print("taille : \"{}\"".format(taille))
    print("niveau : \"{}\"".format(niveau))