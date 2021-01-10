# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

print()

i = 256*256
print('The value of i is', i)

print()

a, b = 0, 1
while a < 1000:
    print(a, end=',') # On peut changer ce qu'on va faire à la fin du print
    a, b = b, a+b
