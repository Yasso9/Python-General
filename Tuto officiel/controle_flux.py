print("1ERE PARTIE\n")

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


print("\n2EME PARTIE\n")


words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

print()

# JAI PAS COMPRIS
users = {}
# Code qui modifie une collection

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print()

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


print("\n3EME PARTIE\n")


for i in range(5):
    print(i)

print()

for i in range(5, 10):
    print(i)
    
print()

for i in range(0, 10, 3):
    print(i)
    
print()

for i in range(-10, -100, -30):
    print(i)
    
print()

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
    
print()

print(sum(range(4)))  # 0 + 1 + 2 + 3

print(list(range(4)))