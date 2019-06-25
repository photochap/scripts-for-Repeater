<<<<<<< HEAD
#!/usr/bin/python3
##########################################
# ScreenDStar
##########################################
# Python 3
# if python 2
#    from Tkinter import *
#    import ConfigParser
#

from tkinter import *
from utilitaire_gestion_des_fichiers import *

import CONST
import threading
import os
import configparser
import pyinotify
import glob
import socket

#Commande system pour l'interface graphique
=======
from Tkinter import *
import os
import glob
import time, threading
from time import sleep
from Tkinter import *


#function -----------------------------------------------------------------------------
>>>>>>> 19a17936590375feb8c9dd6eb115023c66ac81c9
#System shutdown function
def StopSys():
  os.system('sudo shutdown -h now')
  return

<<<<<<< HEAD
#System reboot function
def RebootSys():
  os.system('sudo reboot')
  return

#Class declaration ________________________________________
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        if not event.dir:
            gui.updateGUI(event.pathname)

class WatchFile(threading.Thread):
    def run(self):
        wm = pyinotify.WatchManager()
        mask = pyinotify.IN_MODIFY
        handler = EventHandler()
        notifier = pyinotify.Notifier(wm, handler)
        wdd = wm.add_watch(CONST.LOGDIR, mask, rec=True, auto_add=True)
        notifier.loop()
        self.notifier = notifier

#Partie Graphique -----------------------------------------------------------     
class Window_Element:
    def __init__(self, Fenetre):
        self.Fenetre = Fenetre

    def Creat_PW(self, Fenetre, Orient, HW, Side, BG):
        cpw = PanedWindow(Fenetre, orient=Orient, bg=BG)
        if Orient == "horizontal": cpw.config(height=HW)
        if Orient == "vertical": cpw.config(width=HW)
        cpw.pack(side=Side, fill=BOTH, pady=0, padx=0)
        return cpw
                    
    def Bouton(self, PW, Img, Command):
        bouton = Button(PW,
                        command=Command, 
                        borderwidth=0,
                        relief=FLAT,
                        image=Img,
                        bg=CONST.BGCOLOR,
                        padx=0, pady=0,
                        highlightbackground=CONST.BGCOLOR
                )
        return bouton

    def Image(self, PW, Img, Width, Height):
        img = Canvas(PW,
                width=Width, 
                height=Height, 
                         borderwidth=0,
                         bg=CONST.BGCOLOR,
                         highlightbackground=CONST.BGCOLOR
                         )
        img.create_image(0, 0, anchor=NW, image=Img)
        return img

    def Listb(self, PW, nbrItmListe, nbrColListe):     
        frm = Frame(PW)
        scrollbar = Scrollbar(frm)
        listb = Listbox(frm)
        scrollbar.config(command=listb.yview)
        listb.config(yscrollcommand = scrollbar.set, height=nbrItmListe, width=nbrColListe)
        listb.pack(side = LEFT, fill = Y)
        scrollbar.pack(side=RIGHT, fill=Y)
        return [frm, listb]

class Gestion_Pages:
    def __init__(self, Fenetre):
        self.Fenetre = Fenetre
    
    def Page(self, Name):
        print("Page----------------------------------")
        print(Name.winfo_ismapped())
        if Name.winfo_ismapped():
            print("True")
            Name.pack_forget()
        else:
           print("False")
           Name.pack()
        return
    

 
class Gui(object):
    def __init__(self):
        self.root = Tk()
        self.UF = Util_File()       
        self.GF = InfosDStarInLog()
        self.IS = infoSystem()       
        self.GP = Gestion_Pages(self.root)       
        
        #Full windows screen
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.overrideredirect(1)
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root['bg']=CONST.BGCOLOR

        Panel_init = Window_Element(self.root)

        #Images --------------------------------------------------------
        self.Im_IMGQTFILE = PhotoImage(file=CONST.IMGQTFILE)
        self.Im_IMGSDFILE = PhotoImage(file=CONST.IMGSDFILE)
        self.Im_IMGRBFILE = PhotoImage(file=CONST.IMGRBFILE)
        self.Im_IMGLGFILE = PhotoImage(file=CONST.IMGLGFILE)
        self.Im_IMGPRFILE = PhotoImage(file=CONST.IMGPRFILE)

        #PanedWindow --------------------------------------------------------
        WTop = Panel_init.Creat_PW(self.root, HORIZONTAL, "40p", TOP, CONST.BGCOLOR)
        WLeft = Panel_init.Creat_PW(self.root, VERTICAL, "80p", LEFT, CONST.BGCOLOR)
        self.WCenter = Panel_init.Creat_PW(self.root, VERTICAL, "320p", LEFT, "green")


        self.WRight = Panel_init.Creat_PW(self.root, VERTICAL, "80p", LEFT, CONST.BGCOLOR)

        #Image --------------------------------------------------------
        Logo_Image = Panel_init.Image(WTop, self.Im_IMGLGFILE, 100, 50)

        #Label --------------------------------------------------------
        Title_Label = Label(WTop, text=CONST.TXTTITLE + " " + CONST.CALL, fg=CONST.FGCOLOR, bg=CONST.BGCOLOR, font=(CONST.FONTTXT, 15, "bold"), width=28)
        self.Rrefl_Label    = Label(WLeft,      text=CONST.NOCONNECT, fg=CONST.FGCOLOR, bg="orange", font=(CONST.FONTTXT, 12, "bold"), width=10)
        self.IP_Label       = Label(WLeft,      text=CONST.WAIT, fg="white", bg="green", font=(CONST.FONTTXT, 12, "bold"), width=10)
        self.Dt_Label       = Label(WLeft,      text="Dt", fg="white", bg="grey", font=(CONST.FONTTXT, 8, "bold"), width=10)
        self.My_Label       = Label(WLeft,      text="My", fg="white", bg="grey", font=(CONST.FONTTXT, 10, "bold"), width=10)
        self.Your_Label     = Label(WLeft,      text="Your", fg="white", bg="grey", font=(CONST.FONTTXT, 10, "bold"), width=10)
        self.RPT1_Label     = Label(WLeft,      text="RTP1", fg="white", bg="grey", font=(CONST.FONTTXT, 10, "bold"), width=10)
        self.RPT2_Label     = Label(WLeft,      text="RPT2", fg="white", bg="grey", font=(CONST.FONTTXT, 10, "bold"), width=10)
        self.APRS_Label     = Label(self.WRight, text="APRS-Host", fg="white", bg="green", font=(CONST.FONTTXT, 9, "bold"), width=10)
        self.DCS_Label      = Label(self.WRight, text="DCS-Host", fg="white", bg="green", font=(CONST.FONTTXT, 9, "bold"), width=10)
        self.DExtra_Label   = Label(self.WRight, text="DExtra", fg="white", bg="green", font=(CONST.FONTTXT, 9, "bold"), width=10)
        self.DPlus_Label    = Label(self.WRight, text="DPlus", fg="white", bg="green", font=(CONST.FONTTXT, 9, "bold"), width=10)
        self.DRats_Label    = Label(self.WRight, text="D-Rats", fg="white", bg="green", font=(CONST.FONTTXT, 9, "bold"), width=10)
        self.Info_Label     = Label(self.WRight, text="Info", fg="white", bg="green", font=(CONST.FONTTXT, 9, "bold"), width=10)
        self.Echo_Label     = Label(self.WRight, text="Echo", fg="white", bg="green", font=(CONST.FONTTXT, 9, "bold"), width=10)

        #Label Grille ---------------------------------------------------
        Label(self.WCenter, text='Date :', borderwidth=1, width=20, justify=LEFT, compound=LEFT).grid(row=0, column=0)
        Label(self.WCenter, text='My :', borderwidth=1, width=13, justify=LEFT, compound=LEFT).grid(row=0, column=1)

        #Button --------------------------------------------------------
        Quit_Bouton = Panel_init.Bouton(WTop, self.Im_IMGQTFILE, self.root.destroy)
        Stop_Bouton = Panel_init.Bouton(WLeft, self.Im_IMGSDFILE, StopSys)
        Reboot_Bouton = Panel_init.Bouton(WLeft, self.Im_IMGRBFILE, RebootSys)
        Param_Bouton = Panel_init.Bouton(self.WRight, self.Im_IMGPRFILE, self.GP.Page(self.WCenter))

        #Mise en place des Widgets --------------------------------------------------------
        #TOP
        WTop.add(Logo_Image)
        WTop.add(Title_Label)
        WTop.add(Quit_Bouton)
        #LEFT
        WLeft.add(self.Rrefl_Label)
        WLeft.add(self.Dt_Label)
        WLeft.add(self.My_Label)
        WLeft.add(self.Your_Label)
        WLeft.add(self.RPT1_Label)
        WLeft.add(self.RPT2_Label)       
        WLeft.add(self.IP_Label)
        WLeft.add(Stop_Bouton)
        #RIGHT
        self.WRight.add(self.APRS_Label)
        self.WRight.add(self.DCS_Label)
        self.WRight.add(self.DExtra_Label)
        self.WRight.add(self.DPlus_Label)
        self.WRight.add(self.DRats_Label)
        self.WRight.add(self.Info_Label)
        self.WRight.add(self.Echo_Label)        
        self.WRight.add(Param_Bouton)
         
        self.init()

    def Aff_Call(self, Nbr_Call):
        #initialise la liste des réflecteurs non trouvés
        call = self.GF.My(Nbr_Call)
        r=1
        for Tcall in call[0]:
            Label(self.WCenter, text=call[4][r-1], borderwidth=1, width=20, justify=LEFT, compound=LEFT).grid(row=r, column=0)
            Label(self.WCenter, text=Tcall, borderwidth=1, width=13, justify=LEFT, compound=LEFT).grid(row=r, column=1)
            r+=1 

    
    def CONNECT(self):
        #Change le Label de connection en fonction du statut        
        Etat_Connect = self.GF.Connect_REF()
        if Etat_Connect[0]: BG = "green" 
        else: BG = "red"
        self.Rrefl_Label.configure(text=Etat_Connect[1], bg=BG, fg="white")

    def init(self):
        #initialise le Label de connection 
        self.CONNECT()       
        IP_Adr = self.IS.get_ip_address()
        self.IP_Label.configure(text=IP_Adr)
        #initialise la liste des réflecteurs non trouvés
        self.Aff_Call(15)
        
        self.Dt_Label.config(text=self.GF.My(1)[4][0])
        self.My_Label.config(text=self.GF.My(1)[0][0])
        self.Your_Label.config(text=self.GF.My(1)[1][0])
        self.RPT1_Label.config(text=self.GF.My(1)[2][0])
        self.RPT2_Label.config(text=self.GF.My(1)[3][0])
        
        #Affiche la conf de la Gateway
        GFircddb_Conf = self.GF.ircddb_Conf()        
        if GFircddb_Conf['aprsEnabled']!="1": self.APRS_Label.config(bg="red")
        if GFircddb_Conf['dcsEnabled']!="1": self.DCS_Label.config(bg="red")
        if GFircddb_Conf['dextraEnabled']!="1": self.DExtra_Label.config(bg="red")
        if GFircddb_Conf['dplusEnabled']!="1": self.DPlus_Label.config(bg="red")
        if GFircddb_Conf['dratsEnabled']!="1": self.DRats_Label.config(bg="red")
        if GFircddb_Conf['infoEnabled']!="1": self.Info_Label.config(bg="red")
        if GFircddb_Conf['echoEnabled']!="1": self.Echo_Label.config(bg="red")
        
        self.root.update()

    def updateGUI(self, File):
        if File.find("Headers")>0: 
           self.Aff_Call(15)
           self.Dt_Label.config(text=self.GF.My(1)[4][0])
           self.My_Label.config(text=self.GF.My(1)[0][0])
           self.Your_Label.config(text=self.GF.My(1)[1][0])
           self.RPT1_Label.config(text=self.GF.My(1)[2][0])
           self.RPT2_Label.config(text=self.GF.My(1)[3][0])
           
        #Links.log
        if File.find("Links")>0:
            self.CONNECT()
        #STARnet.log
        self.root.update()

gui = Gui()
WF = WatchFile()
WF.start()
gui.root.mainloop()
























=======
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
>>>>>>> 19a17936590375feb8c9dd6eb115023c66ac81c9




<<<<<<< HEAD
=======
fenetre.mainloop()
>>>>>>> 19a17936590375feb8c9dd6eb115023c66ac81c9
