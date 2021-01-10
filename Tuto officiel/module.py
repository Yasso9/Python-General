print("1ERE PARTIE\n")

import fibo

import importlib; importlib.reload(fibo) # Si on veut réimporter le module fibo (si il y'a eu un changement ou quoi)

fibo.fib(1000)
print(fibo.fib2(100))
print(fibo.__name__)

print()

# Si on compte utiliser la fonction plusieurs fois on peut faire ça et lui donner un nom de variables
fib = fibo.fib
fib(500)


print("\n2EME PARTIE\n")


# from fibo import fib, fib2

# fib(500)