class Erreur(Exception):
    """Classe de base pour les exceptions de lecture de fichiers."""
    pass

# EXCEPTION D'ARGUMENTS DE LIGNE DE COMMANDE

class ErreurLigneDeCommande(Erreur):
    """Erreur qui est levé lorsque les arguments en ligne de commandes ne sont pas bon"""

# EXCEPTION DE LECTURE DE FICHIERS

class ErreurDefinition(Erreur):
    """Erreur qui est levé lorsque la définition d'une des lignes
    fichier est incorrect."""

class DefinitionMultiple(Erreur):
    """Erreur qui est levé lorsque une définition est répétée plusieurs fois."""

class DefinitionManquante(Erreur):
    """Erreur qui est levé lorsque une définition essentiel manque."""

class SynthaxeRegleErreur(Erreur):
    """Erreur qui est levé lorsque la valeur d'une règle est mal réalisé."""

class ErreurValeur(Erreur):
    """Erreur qui est levé lorsque la valeur d'un des mots du 
    fichier n'est pas pris en charge ou incorrect."""

class ValeurManquante(Erreur):
    """Erreur qui est levé lorsque une valeur manque."""