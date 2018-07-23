from Tkinter import *
import os
import glob
import time, threading
from time import sleep
from Tkinter import *


#function -----------------------------------------------------------------------------
#System shutdown function
def StopSys():
  os.system('sudo shutdown -h now')
  return

class InfosDStarInLog:

    def FILE(self, File):
        list_of_files = glob.glob('/var/log/opendv/'+File+'*')
        theFile = open(max(list_of_files, key=os.path.getctime), 'r')
        FILE = theFile.readlines()
        theFile.close()
        return FILE

    def lastLine(self, logFile):
        line = []
        lastLine = ""
        line = self.FILE(logFile)
        lastLine = line[len(line)-1]
        return lastLine[0]

    def allLine(self, logFile):
        line = []
        line = self.FILE(logFile)
        line = line
        return line        
                
    def findWord(self, Word, logFile):
        line = []
        for liste in self.allLine(logFile):
            if liste.find(Word)>0: line.append(liste)
        line.reverse()
        return line

    def My(self):
        My = []
        for line in self.findWord("My:", "Header"):
         My.append(line[int(line.find("My:")+4):int(line.find("My:")+11)] + " - " + line[8:10] + "/" + line[5:7] +  " "  + line[10:16] + " " + line[int(line.find("Rpt2:")+6):int(line.find("Rpt2:")+15)])
        return My
  
    def failed2connect(self):
        failed2connect = []
        for line in self.findWord("failed to connect", "ircDDBGateway"):
         failed2connect.append(line[3:int(line.find("failed to connect")-4)])
        return failed2connect
    
    def CannotFind(self):
        CannotFind = []
        for line in self.findWord("Cannot find address for host", "ircDDBGateway"):
         CannotFind.append(line[int(line.find("Cannot find address for host"))+30:len(line)-1])
        return CannotFind
    
    def Starting_ircDDB(self):
        Starting_ircDDB = []
        for line in self.findWord("Starting ircDDB Gateway daemon", "ircDDBGateway"):
         Starting_ircDDB.append(line[3:22])
        return Starting_ircDDB
    
    def reflector(self):
        reflector = ""
        line = self.findWord("established", "ircDDBGateway")
        if line:
         line = line[len(line)-1]
         reflector = line[line.find("link to")+8:len(line)-12]
        else:
          reflector = "not connected"
        return reflector

    def reflector_dt(self):
        reflector_dt = ""
        line = self.findWord("established", "ircDDBGateway")
        if line:
         line = line[len(line)-1]
         reflector_dt = line[11:13] + "/" + line[8:10] + "/" + line[3:7] +  " "  + line[13:19]
        return reflector_dt

class listboxScrolling:

    def listbox(self, liste, nbrItmListe, nbrColListe):
        listbox = Frame(fenetre)
        listbox_s1 = Scrollbar(listbox)
        listbox_l1 = Listbox(listbox)
        i = 0
        for lt in liste:
            listbox_l1.insert(i, lt)
            i+=1
        listbox_s1.config(command = listbox_l1.yview)
        listbox_l1.config(yscrollcommand = listbox_s1.set, height=nbrItmListe, width=nbrColListe)
        listbox_l1.pack(side = LEFT, fill = BOTH)
        listbox_s1.pack(side = RIGHT, fill = Y)
        
        return listbox


#Graphique -----------------------------------------------------------------------------
fenetre = Tk()
#Full windows screen
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
fenetre.overrideredirect(1)
fenetre.geometry("%dx%d+0+0" % (w, h))
#Background picture
canvas = Canvas(fenetre,width=480, height=320)
photo = PhotoImage(file="~/scripts-for-Repeater/img/screen.png")
background_label = Label(fenetre, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.pack()

InfosDStar = InfosDStarInLog() 
listboxScroll = listboxScrolling()



label_log_connect = Label(fenetre, text="ircDDB Log", justify='left')
label_log_connect_window = canvas.create_window(0, 140, anchor='nw', window=label_log_connect)    
log_connect_window = canvas.create_window(0, 170, anchor='nw', window=listboxScroll.listbox([InfosDStar.lastLine("ircDDBGateway")], 2, 37))    


#Buttons -----------------------------------------------------------------------------
#Close button
quit_bouton=Button(fenetre, text="Close", command=fenetre.destroy, anchor = 'w', width = 5, height = 5, activebackground = "#33B5E5")
quit_button_window = canvas.create_window(400, 1, anchor='nw', window=quit_bouton)    

#Close shutdown
quit_bouton=Button(fenetre, text="Stop", command=StopSys, anchor = 'w', width = 5, height = 5, activebackground = "#33B5E5")
quit_button_window = canvas.create_window(400, 90, anchor='nw', window=quit_bouton)    

#Txt display -----------------------------------------------------------------------------


My_window = canvas.create_window(130, 5, anchor='nw', window=listboxScroll.listbox(InfosDStar.My(), 8, 28))
#label_unknown_hosts_window = canvas.create_window(0, 220, anchor='nw', window=listboxScroll.listbox  (InfosDStar.findWord("unknown", "ircDDBGateway"), 2, 220))    

label_failed_connect = Label(fenetre, text="Failed to connect", justify='left')
label_failed_connect_window = canvas.create_window(0, 200, anchor='nw', window=label_failed_connect)    
failed_connect_window = canvas.create_window(0, 220, anchor='nw', window=listboxScroll.listbox  (InfosDStar.failed2connect(), 2, 37))    


label_Starting_ircDDB = Label(fenetre, text="Starting ircDDB Gateway daemon", justify='left')
label_Starting_ircDDB_window = canvas.create_window(0, 250, anchor='nw', window=label_Starting_ircDDB)    
Starting_ircDDB_window = canvas.create_window(0, 270, anchor='nw', window=listboxScroll.listbox(InfosDStar.Starting_ircDDB(), 2, 17))

label_CannotFind = Label(fenetre, text="Cannot find address", justify='left')
label_CannotFind_window = canvas.create_window(320, 200, anchor='nw', window=label_CannotFind)    
CannotFind_window = canvas.create_window(320, 220, anchor='nw', window=listboxScroll.listbox(InfosDStar.CannotFind(), 6, 17))



#Print reflectorC
label_reflectorC = Label(fenetre, text=InfosDStar.reflector()+"\n"+InfosDStar.reflector_dt(), justify='left')
label_reflectorC_window = canvas.create_window(0, 55, anchor='nw', window=label_reflectorC)    




fenetre.mainloop()