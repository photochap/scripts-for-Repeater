from tkinter import * 
from time import sleep

 
a = 0 ##ou 1
 
def ma_fonction():
    if cpw.winfo_ismapped():
        Bout2.pack_forget()
        cpw.pack_forget()
    else:
        Bout2.pack() 
        cpw.pack()
 
 
Fen1 = Tk()
 
Bout1 = Button(Fen1, text="Afficher/Cacher 'Bouton 2'", command = ma_fonction)
Bout2 = Button(Fen1, text="Bouton 2", command = Fen1.destroy)
cpw = PanedWindow(Fen1, orient=HORIZONTAL, bg="red")
Lb = Label(Fen1,text="TEST")
cpw.add(Lb)
cpw.add(Bout2)

Bout1.pack()
Bout2.pack()
cpw.pack()
 
Fen1.mainloop()