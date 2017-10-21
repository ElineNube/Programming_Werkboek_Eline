from tkinter import *
import math

def klik():
    grondtal = int(entry.get())
    kwadraat = grondtal ** 2
    tekst = 'Het kwadraat van {} is {}'
    label['text'] = tekst.format(grondtal, kwadraat)

def klik2():
    grondtal=int(entry.get())
    wortel = math.sqrt(grondtal)
    tekst = 'De wortel van {} is {}'
    label['text'] = tekst.format(grondtal, wortel)

root = Tk()     #Creeër het hoofdscherm

label = Label (master=root,
               text='Geef een getal',
               background='pink',
               foreground='black',
               font =('Verdana', 16, 'bold'),
               width = 50,
               height = 5)
label.pack()

button = Button(master=root,
                text='Reken het kwadraat uit',
                command=klik,
                background='red')
button.pack(pady=10, padx=10, side=BOTTOM)

button2 = Button(master=root,
                 text='Reken de wortel uit',
                 command=klik2,
                 background='red')
button2.pack(pady=10,padx=10, side=BOTTOM)

entry = Entry(master=root)
entry.pack(padx=10,pady=10)

root.mainloop() #Toon het hoofdscherm
