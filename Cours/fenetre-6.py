from tkinter import *
 
fen1 = Tk()

Label(fen1, text = 'Premier champ :').grid(row =1, sticky =E)
Label(fen1, text = 'Second :').grid(row =2, sticky =E)
Label(fen1, text ='Troisième :').grid(row =3, sticky =E)

Entry(fen1).grid(row =1, column =2)
Entry(fen1).grid(row =2, column =2)
Entry(fen1).grid(row =3, column =2)

# création d'un widget 'Canvas' contenant une image bitmap :
photo = PhotoImage(file ='annexe/risitas.gif')

can1 = Canvas(fen1, width =160, height =160, bg ='grey')

can1.create_image(80, 80, image =photo)
can1.grid(row =1, column =3, rowspan =3, padx =10, pady =5)
 
fen1.mainloop()