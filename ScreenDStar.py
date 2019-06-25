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
#System shutdown function
def StopSys():
  os.system('sudo shutdown -h now')
  return

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




























