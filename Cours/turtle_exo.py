from turtle import Turtle, Screen
from math import sqrt, sin, cos, acos, pi

turtle = Turtle()
screen = Screen()

screen.title("Exercice pour le module turtle")

turtle.speed(2)
turtle.pensize(2)

def triangle(base, side, angle = 0, direction = "right"):
    turtle.setheading(angle)

    angle1 = 180 - acos(base / (side*2)) * (180 / pi)
    angle2 = 360 - angle1 * 2

    if(direction == "right"):
        turtle.forward(base)
        turtle.right(angle1)
        turtle.forward(side)
        turtle.right(angle2)
        turtle.forward(side)
        turtle.right(angle1)
    elif(direction == "left"):
        turtle.forward(base)
        turtle.left(angle1)
        turtle.forward(side)
        turtle.left(angle2)
        turtle.forward(side)
        turtle.left(angle1)
    else:
        print("Il y'a un probleme concernant la variable direction")

    turtle.setheading(angle)

def rectangle(horizontalSide, verticalSide):
    for _ in range(0, 2):
        turtle.forward(horizontalSide)
        turtle.right(90)
        turtle.forward(verticalSide)
        turtle.right(90)

def star5(length, angle = 0):
    turtle.setheading(angle)

    for _ in range(0, 5):
        turtle.forward(length)
        turtle.right(144)

    turtle.setheading(angle)

def star6(length, angle = 0):
    distance = sqrt((2/9) * (length**2) * (1 - cos(155)))

    turtle.penup()
    turtle.left(90)
    turtle.forward(distance/2)
    turtle.right(90)
    turtle.pendown()    

    triangle(length, length, angle, "right")

    turtle.right(90)

    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()    

    triangle(length, length, angle, "left")

    turtle.setheading(angle)

    turtle.penup()
    turtle.left(90)
    turtle.forward(distance/2)
    turtle.right(90)
    turtle.pendown()

# INTRODUCTION

turtle.penup()
turtle.setposition(-200, -300)
turtle.pendown()

turtle.setheading(0)
turtle.color("blue")

# SPIRAL (mix des deux d'en bas)

size = 50
coefficient = 1.2
angle = 0
for i in range(0, 9):
    if(i % 4 == 0):
        turtle.color("blue")
        star5(size, angle)
    elif(i % 2 == 0):
        turtle.color("blue")
        star6(size, angle)
    elif((i+1) % 4 == 0):
        turtle.color("red")
        rectangle(size, size)
    else:
        turtle.color("red")
        triangle(size, size)

    turtle.penup()
    turtle.forward(size+10)
    turtle.pendown()

    if(i < 4):
        size = size * coefficient
    else:
        size = size / coefficient

    angle = angle + 36
    turtle.setheading(angle)

longueur = 40
largeur = 20

# SUITE D'ETOILES (5 ou 6)

# size = 50
# coefficient = 1.2
# for i in range(0, 9):
#     star6(size)

#     turtle.penup()
#     turtle.forward(size+10)
#     turtle.pendown()

#     if(i < 4):
#         size = size * coefficient
#     else:
#         size = size / coefficient

# longueur = 40
# largeur = 20

# SUITE CARRE TRIANGLE

# for _ in range(0, 5):
#     turtle.color("red")
#     rectangle(longueur, largeur)

#     turtle.penup()
#     turtle.forward(largeur+5)
#     turtle.pendown()

#     turtle.color("blue")
#     triangle(largeur, longueur)

#     turtle.setheading(0)
#     turtle.penup()
#     turtle.forward(largeur+5)
#     turtle.pendown()

#     longueur = longueur * 1.5
#     largeur = largeur * 1.5

input()