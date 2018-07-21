from Tkinter import *
import os
import glob

os.system('clear')

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
    


InfosDStar = InfosDStarInLog()


for lt in InfosDStar.FILE("STARnet.log"):
  print lt