from turtle import Turtle

# reset() : On efface tout et on recommence
# setposition(x, y) : Aller à l'endroit de coordonnées x, y
# forward(distance) : Avancer d'une distance donnée
# backward(distance) : Reculer
# up() : Relever le crayon (pour pouvoir avancer sans dessiner)
# down() : Abaisser le crayon (pour recommencer à dessiner)
# color(couleur) : couleur peut être une chaîne prédéfinie ('red', 'blue', etc.)
# left(angle) : Tourner à gauche d'un angle donné (exprimé en degrés)
# right(angle) : Tourner à droite
# width(épaisseur) : Choisir l'épaisseur du tracé
# fill(1) : Remplir un contour fermé à l'aide de la couleur sélectionnée
# write(texte) : texte doit être une chaîne de caractères

turtle = Turtle()

def initialisation(posx, posy, colors = "black"):
    turtle.penup()

    turtle.color(colors)
    turtle.speed(3)
    turtle.pensize(2)
    turtle.setposition(posx, posy)

    turtle.pendown()

def triangle(side, angle = 0):
    turtle.penup()

    turtle.setheading(angle)
    turtle.forward(0.75*side)
    turtle.left(120)

    turtle.pendown()
    i = 0
    while (i < 3):
        turtle.forward(side)
        turtle.left(120)
        i = i + 1


def rectangle(coteVertical, coteHorizontal):
    turtle.setheading(0)

    for _ in range(0, 2):
        turtle.forward(coteVertical)
        turtle.right(90)
        turtle.forward(coteHorizontal)
        turtle.right(90)

# Partie principale du programme

initialisation(-200, -200, "red")
for _ in range(0, 10):
    rectangle(20, 50)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()

input()


