print("1ERE PARTIE\n")


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print(fib(2000))

print()

print(fib)
F = fib
print(F(100))
# Fonction qui va afficher seulement None car il n'ya pas de return
print(fib(0))


print("\n2EME PARTIE\n")


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
print(f100)


print("\n3EME PARTIE\n")


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# Plusieurs façon d'appeler cette fonction
# print(ask_ok('Do you really want to quit?'))
# print()
# ask_ok('OK to overwrite the file?', 2)
# print()
# print(ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!'))

# print()

i = 5
def f1(arg=i):
    print(arg)
i = 6
f1()

print()

def f2(a, L=[]):
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))

print()

def f3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f3(1))
print(f3(2))
print(f3(3))


print("\n4EME PARTIE\n")


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# CORRECT
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# INCORRECT
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


print("\n5EME PARTIE\n")


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


print("\n6EME PARTIE\n")


def standard_arg(arg): # Pourrait être équivalent à standard_arg(/, arg, *)
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# Peut tout avoir
standard_arg(2)
standard_arg(arg=2)

pos_only_arg(1)
# pos_only_arg(arg=1) # Erreur

# kwd_only_arg(3) # Erreur
kwd_only_arg(arg=3)

# combined_example(1, 2, 3) # Erreur pour le dernier argument
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # Erreur pour le premier argument

print()

# def foo1(name, **kwds):
#     return 'name' in kwds
# foo1(1, **{'name': 2}) # Erreur

def foo2(name, /, **kwds):
    return 'name' in kwds
# foo2(1, **{'name': 2}) # Pas d'erreur

# Récapitulatif
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass


print("\n7EME PARTIE\n") # Listes d'arguments arbitraires


def print_multiple_items(separator, *args):
    print(separator.join(args))

print_multiple_items("-", "earth", "mars", "venus")
print_multiple_items(" () ", "earth", "mars", "venus")

print()

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))
print(concat("earth", "mars", "venus", ".")) # il faut préciser sep="." si ça marche mal


print("\n8EME PARTIE\n") # Séparation des listes d'arguments


print(list(range(3, 6))) # normal call with separate arguments
args = [3, 6]
print(list(range(*args))) # call with arguments unpacked from a list

def parrot2(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot2(**d)


print("\n9EME PARTIE\n") # Fonctions anonymes ou lambdas


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))

print()

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


print("\n10EME PARTIE\n") # Annotations et documentations


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

print()

def fonc_annotation(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

fonc_annotation('spam')