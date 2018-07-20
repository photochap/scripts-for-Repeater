from Tkinter import *
import os
  
#variable
txt = ""

#System shutdown function
def StopSys():
  os.system('sudo shutdown -h now')
  return


#Open line and rec on FILE variable
theFile = open('/var/log/user.log', 'r')
FILE = theFile.readlines()
theFile.close()

#read File variable and extract inforamtion
for line in FILE:
    txt = txt + line[int(line.find("connected")):int(line.find("connected")+30)]

fenetre = Tk()

#Full windows screen
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
fenetre.overrideredirect(1)
fenetre.geometry("%dx%d+0+0" % (w, h))

#Background picture
canvas = Canvas(fenetre,width=480, height=320)
photo = PhotoImage(file="./img/screen.png")
background_label = Label(fenetre, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.pack()

#Close button
quit_bouton=Button(fenetre, text="Fermer", command=fenetre.quit, anchor = 'w', width = 5, activebackground = "#33B5E5")
quit_button_window = canvas.create_window(410, 1, anchor='nw', window=quit_bouton)    

#Close shutdown
quit_bouton=Button(fenetre, text="Shutdown", command=StopSys, anchor = 'w', width = 5, activebackground = "#33B5E5")
quit_button_window = canvas.create_window(410, 20, anchor='nw', window=quit_bouton)    

#Print txt
label = Label(fenetre, text="Liste des connections : " + txt, bg="#DDDDDD")
txt_label_window = canvas.create_window(10, 100, anchor='nw', window=label)    


fenetre.mainloop()