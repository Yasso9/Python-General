fichier = open("lsystem.txt", "r")
line = fichier.readline()

motAxiome = line[0:6]

egalite = line[7]

axiome = line[10:-2]

print(motAxiome)
print(egalite)
print(axiome)


try:
    assert motAxiome == "axiome"
    assert egalite == "="
    assert axiome == "---a"
except AssertionError:
    print("Erreur dans la ligne 1")

fichier.close()