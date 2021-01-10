print("1ERE PARTIE\n")

# Not good
# print('C:\some\name')  # here \n means newline!
# Chaine brute
print(r'C:\some\name')  # note the r before the quote

print()

print(3 * 'un' + 'ium')

print('Py' 'thon')
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
prefix = 'Py'
# prefix 'thon'  # can't concatenate a variable and a string literal
print(prefix + 'thon')

print()


print("2EME PARTIE\n")

word = "Python"

print(word[0])  # character in position 0
print(word[5])  # character in position 5

print()

print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])

print()

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)

print()

print(word[:2] + word[2:])
print(word[:4] + word[4:])

print()

print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end

print()

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# print(word[42])  # the word only has 6 characters
print(word[4:42])
print(word[42:])

print()

# Erreur
# print(word[0]) = 'J'
# print(word[2:]) = 'py'

print('J' + word[1:])
print(word[:2] + 'py')

print()

s = 'supercalifragilisticexpialidocious'
print(len(s))