myList = [4, 7, 9, 3, 5, 4, 1]

# Exercice 1
def exist(l, elem):
    for i in l:
        if(elem == i):
            return True
    return False

# Exercice 2
def occur(l, elem):
    sum = 0
    for i in l:
        if(i == elem):
            sum = sum + 1
    return sum

# Exercice 3
def index(l, elem):
    i = 0
    for integer in l:
        if(integer == elem):
            return i
        else:
            i = i + 1
    return -1

def index_all(l1, elem):
    l2 = []
    for i in l1:
        if(i == elem):
            return i
        else:
            i = i + 1
    return -1

print(index(myList, 7))
print(index(myList, 6))
print(index(myList, 4))