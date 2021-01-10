def substitution(axiome, regles, niveau):
    finalSystem = axiome

    # Si il n'y a pas de règle, alors la ligne final de substitution sera un axiome
    if regles != []:
        for _ in range(0, niveau):
            for regle in regles:
                finalSystem = finalSystem.replace(regle[0], regle[2:])     

    return finalSystem

if __name__ == "__main__":
    chaine = substitution("aa++", "a=b-b", 5)
    print(chaine)