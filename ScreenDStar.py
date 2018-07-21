from Tkinter import *
import os
import glob

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
        return lastLine        

    def allLine(self, logFile):
        line = []
        line = self.FILE(logFile)
        line = line
        return line        
                
    def findWord(self, Word, logFile):
        line = []
        for liste in self.allLine(logFile):
            if liste.find(Word)>0: line.append(liste)
        return line

    def DateMy(self):
        line = ""
        line = self.lastLine('Headers')
        DateMy    = "Date:  " + line[8:10] + "/" + line[5:7] + "/" + line[0:4] +  " "  + line[10:16]
        return DateMy
    
    def My(self):
        line = ""
        line = self.lastLine('Headers')
        My   = "My:    " + line[int(line.find("My:")+4):int(line.find("My:")+17)]
        return My

    def Your(self):
        line = ""
        line = self.lastLine('Headers')
        Your = "Your:  " + line[int(line.find("Your:")+6):int(line.find("Your:")+15)]
        return Your

    def RPT1(self):
        line = ""
        line = self.lastLine('Headers')
        RPT1 = "Rpt1:  " + line[int(line.find("Rpt1:")+6):int(line.find("Rpt1:")+15)]
        return RPT1

    def RPT2(self):
        line = ""
        line = self.lastLine('Headers')
        RPT2 = "Rpt2:  " + line[int(line.find("Rpt2:")+6):int(line.find("Rpt2:")+15)]
        return RPT2
  
    def reflector(self):
        reflector = ""
        line = self.findWord("established", "ircDDBGateway")
        line = line[len(line)-1]
        reflector = line[line.find("link to")+8:len(line)-12]
        return reflector
    
    def reflector_dt(self):
        reflector_dt = ""
        line = self.findWord("established", "ircDDBGateway")
        line = line[len(line)-1]
        reflector_dt = line[11:13] + "/" + line[8:10] + "/" + line[3:7] +  " "  + line[13:19]
        return reflector_dt


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

#Buttons -----------------------------------------------------------------------------
#Close button
quit_bouton=Button(fenetre, text="Fermer", command=fenetre.quit, anchor = 'w', width = 5, activebackground = "#33B5E5")
quit_button_window = canvas.create_window(400, 1, anchor='nw', window=quit_bouton)    

#Close shutdown
quit_bouton=Button(fenetre, text="Shutdown", command=StopSys, anchor = 'w', width = 5, activebackground = "#33B5E5")
quit_button_window = canvas.create_window(400, 40, anchor='nw', window=quit_bouton)    

#Txt display -----------------------------------------------------------------------------
InfosDStar = InfosDStarInLog()  
#listbox and Scrollbar : Cannot find address for host
hostsError = Frame(fenetre)
hostsError_s1 = Scrollbar(hostsError)
hostsError_l1 = Listbox(hostsError)
i = 0
for lt in InfosDStar.findWord("Cannot find address for host", "ircDDBGateway"):
  hostsError_l1.insert(i, lt[int(lt.find("Cannot find address for host"))+29:len(lt)-1])
  i+=1 
hostsError_s1.config(command = hostsError_l1.yview)
hostsError_l1.config(yscrollcommand = hostsError_s1.set, height=3)
hostsError_l1.pack(side = LEFT, fill = BOTH)
hostsError_s1.pack(side = RIGHT, fill = Y)

#Print txtHeader
txtHeader = InfosDStar.DateMy() + "\n" + InfosDStar.My() + "\n" + InfosDStar.Your() + "\n" + InfosDStar.RPT1() + "\n" + InfosDStar.RPT2()
label_txtHeader = Label(fenetre, text=txtHeader, justify='left')
label_txtHeader_window = canvas.create_window(140, 0, anchor='nw', window=label_txtHeader)    

#Print reflectorC
label_reflectorC = Label(fenetre, text=InfosDStar.reflector()+"\n"+InfosDStar.reflector_dt(), justify='left')
label_reflectorC_window = canvas.create_window(0, 55, anchor='nw', window=label_reflectorC)    

#Print Cannot find address for host
hostsError_window = canvas.create_window(0, 270, anchor='nw', window=hostsError)





fenetre.mainloop()