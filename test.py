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
        line.reverse()
        return line

    def My(self):
        My = []
        for line in InfosDStar.findWord("My:", "Header"):
         My.append(line[int(line.find("My:")+4):int(line.find("My:")+11)] + " - " + line[8:10] + "/" + line[5:7] +  " "  + line[10:16] + " " + line[int(line.find("Rpt2:")+6):int(line.find("Rpt2:")+15)])
        return My
  
    def failed2connect(self):
        failed2connect = []
        for line in InfosDStar.findWord("failed to connect", "ircDDBGateway"):
         failed2connect.append(line[3:int(line.find("failed to connect")-4)])
        return failed2connect
    
    def CannotFind(self):
        CannotFind = []
        for line in InfosDStar.findWord("Cannot find address for host", "ircDDBGateway"):
         CannotFind.append(line[int(line.find("Cannot find address for host"))+30:len(line)-1])
        return CannotFind
    
    def Starting_ircDDB(self):
        Starting_ircDDB = []
        for line in InfosDStar.findWord("Starting ircDDB Gateway daemon", "ircDDBGateway"):
         Starting_ircDDB.append(line[3:22])
        return Starting_ircDDB
    
    def reflector(self):
        reflector = []
        line = self.findWord("established", "ircDDBGateway")
        if line:
         reflector = line[line.find("link to")+8:len(line)-12]
        return reflector

    def reflector_dt(self):
        reflector_dt = ""
        line = self.findWord("established", "ircDDBGateway")
        line = line[len(line)-1]
        reflector_dt = line[11:13] + "/" + line[8:10] + "/" + line[3:7] +  " "  + line[13:19]
        return reflector_dt


InfosDStar = InfosDStarInLog()


print InfosDStar.reflector()












