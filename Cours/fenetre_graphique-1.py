from tkinter import Tk, Label, Button

fen1 = Tk()
tex1 = Label(fen1, text='Bonjour tout le monde !', fg='blue')
tex1.pack()
bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
bou1.pack()
fen1.mainloop()