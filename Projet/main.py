#! /usr/bin/env python3
# coding: utf-8

import sys, getopt
from lecture_fichier import lecture_final
from substitution import substitution
from creation_programme import creation_instruction, creation_fichier
from exception import ErreurLigneDeCommande

def synthax_fichier(nomfichier, extension):
    index = nomfichier.find(".")
    if(index == -1):
        nomfichier + "." + extension
    elif(nomfichier[index+1:-1] != extension):
        nomfichier = nomfichier[0:index] + "." + extension

    return nomfichier


def lecture_ligne_commande():
    fichierEntree = ""
    fichierSortie = ""

    optionsEtValeurs, reste = getopt.getopt(sys.argv[1:], "i:o:")

    # On verifie si les arguments écrit en ligne de commande sont bien écrits
    if(reste != []):
        raise ErreurLigneDeCommande("Arguments sans option en ligne de commande")
    elif(len(optionsEtValeurs) > 2 and len(optionsEtValeurs) < 1):
        raise ErreurLigneDeCommande("Trop d'option en ligne de commande")
    else:
        for optionEtValeur in optionsEtValeurs:
            if(optionEtValeur[0] == "-i"):
                if(fichierEntree != ""):
                    raise ErreurLigneDeCommande("Répétition de l'arguments '-i'")
                fichierEntree = optionEtValeur[1]
            elif(optionEtValeur[0] == "-o"):
                if(fichierSortie != ""):
                    raise ErreurLigneDeCommande("Répétition de l'arguments '-o'")
                fichierSortie = optionEtValeur[1]
            else:
                raise ErreurLigneDeCommande("Option '{}' non prise en compte".format(optionEtValeur[0]))

    if(fichierSortie == ""):
        fichierSortie = "fichier_sortie.py"
    elif(fichierEntree == ""):
        raise ErreurLigneDeCommande("Vous n'avez pas précisé de fichier d'entrée")
    else:
        fichierEntree = synthax_fichier(fichierEntree, "txt")
        fichierSortie = synthax_fichier(fichierSortie, "py")


    
    return fichierEntree, fichierSortie

def main():
    fichierEntree, fichierSortie = lecture_ligne_commande()

    print(fichierEntree)
    print(fichierSortie)


    axiome, regles, angle, taille, niveau = lecture_final(fichierEntree)

    systemFinal = substitution(axiome, regles, niveau)

    instruction = creation_instruction(systemFinal, angle, taille)

    creation_fichier(instruction, fichierSortie)

if __name__ == "__main__":
    main()