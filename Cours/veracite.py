ch = input('Entrez un nombre entier quelconque')
n =int(ch)
if n:
    print("vrai")
else:
    print("faux")

a, b = 3, 8
c = (a < b)
d = (a > b)
print(c)
print(d)

accord = ["non", "oui"]
print(accord[d])
print(accord[c])

ch = input("Entrez une chaîne de caractères quelconque")
if ch: # if ch !="":
    print("vrai")
else:
    print("faux")