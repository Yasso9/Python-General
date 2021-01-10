print("1ERE PARTIE\n")

squares = [1, 4, 9, 16, 25]
print(squares)

print()

print(squares[0])  # indexing returns the item
print(squares[-1])
print(squares[-3:])  # slicing returns a new list
print(squares[:])

print()

print(squares + [36, 49, 64, 81, 100])


print("\n2EME PARTIE\n")


cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(4 ** 3)  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print(cubes)

print()

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)


print("\n3EME PARTIE\n")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = [] # On aurait pu faire "letters = []"
print(letters)
# Taille
print(len(letters)) 


print("\n4EME PARTIE\n")


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
print(x[1][1])