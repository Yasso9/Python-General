from tkinter import Tk, Canvas, Button, ALL, LEFT, RIGHT, TOP, BOTTOM
from random import randrange
 
def draw_square(x, y, color):
  	can.create_rectangle(x, y, x+20, y+20, fill=color, outline=color)

def draw_circle(x, y):
	can.create_oval(x+3, y+3, x+17, y+17, fill='red')

def checkerboard():
	can.delete()

	i = 0
	while i < 10:
		j = 0
		while j < 10:
			# Case de même parité
			if((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)):
				draw_square(i*20, j*20, 'black')	

			else:
				draw_square(i*20, j*20, 'white')
			j = j + 1
		i = i + 1

def piece():
	i, j = 0, 0
	i, j = randrange(9), randrange(9)
	draw_circle(i*20, j*20)
 
##### Programme principal : ############
 
fen = Tk()

can = Canvas(fen, width=200, height=200, bg ='ivory')
can.pack(side =RIGHT, padx =5, pady =5)

bou1 = Button(fen, text='Quitter', command=fen.quit)
bou1.pack(side=BOTTOM)

b1 = Button(fen, text ='Damier', command=checkerboard)
b1.pack(side =TOP)
b3 = Button(fen, text ='Pions', command=piece)
b3.pack(side =TOP)

fen.mainloop()

fen.destroy()