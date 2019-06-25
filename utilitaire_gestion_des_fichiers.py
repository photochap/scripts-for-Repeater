#!/usr/bin/python3
##########################################
# ScreenDStar
##########################################

import CONST

import threading
import os
import configparser
import pyinotify
import glob
import socket


#Class declaration ________________________________________
class infoSystem:
    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IP = s.getsockname()[0]
        s.close()
        return IP

#Class utilitaire gestion des fichier
#Class utilitaire gestion des fichier
class Util_File:

    def FILE(self, File):
        #read log file
        theFile = open(File, 'r')
        FILE = theFile.readlines()
        theFile.close()
        return FILE
          
    def lastFILE(self, File):
        list_of_files = sorted(glob.iglob(CONST.LOGDIR+File+'*'), key=os.path.getctime, reverse=True)
        return list_of_files[0]

    def lastLINE(self, logFile):
        #return last line log file
        line = []
        lastLine = ""
        line = self.FILE(logFile)
        if len(line)>0: lastLine = line[len(line)-1]
        return lastLine
                
    def lastFIND(self, File, Find, Begin, End):
        lastFind_T = []
        lastFind = ""
        for Line in self.FILE(File):
            NumFind = int(Line.find(Find))
            if NumFind > 0: 
               lastFind_T.append(Line[NumFind+Begin:NumFind+End])
               lastFind_T.reverse()
               lastFind = lastFind_T[0]
        return lastFind 
        
#Class Read and format D-Star log 
class InfosDStarInLog:

    def __init__(self):
        self.UF = Util_File()
        
    def Dt_Fr(self, Dt):
        Y = str(Dt[0:4])
        M = str(Dt[5:7])
        D = Dt[8:10]
        H = Dt[11:19]
        Date_Fr = D + "/" + M + "/" + Y + " " + H
        return Date_Fr
        
    def My(self, nbrMy):
        i=1
        Line_T = self.UF.FILE(CONST.HEADERSFILE)
        Line_T.reverse()
        My = []
        Your = []
        Rpt1 = []
        Rpt2 = []
        Dt = []
        for Line in Line_T:
            if i>nbrMy: break
            i+=1
            Num_My = int(Line.find("My"))
            Num_Your = int(Line.find("Your"))
            Num_Rpt1 = int(Line.find("Rpt1"))
            Num_Rpt2 = int(Line.find("Rpt2"))
            My.append(Line[Num_My+4:Num_My+18])
            Your.append(Line[Num_Your+6:Num_Your+14])
            Rpt1.append(Line[Num_Rpt1+6:Num_Rpt1+14])
            Rpt2.append(Line[Num_Rpt2+6:Num_Rpt2+14])
            Dt.append(self.Dt_Fr(Line[0:20]))
        return [My, Your, Rpt1, Rpt2, Dt]
        
    def CannotFind(self, File):
        CannotFind = []
        for CF in self.UF.FILE(File):
            Num = CF.find("Cannot find address for host")
            if Num>0: CannotFind.append(CF[Num+29:len(CF)-1])
        return CannotFind

    def Connect_REF(self):
        #variable init
        Refl_Connect = []
        #Cherche le dernier fichier ircDDBGateway à faire régulièrement : changement de date
        ircDDB_File = self.UF.lastFILE("ircDDBGateway")
        #Dernière ligne de links.log
        if len(self.UF.lastLINE(CONST.LINKSFILE))>0:
           #Verifier dans le fichier link que la connection est bien établie avec ircDDB
           Links_REF = self.UF.lastFIND(CONST.LINKSFILE, "Refl:", 6, 14)
           established_REF = self.UF.lastFIND(ircDDB_File, "established", -9, -1)
           if Links_REF == established_REF: Refl_Connect = [True, established_REF]
           else:[False, "Link error"]
        #Si le fichier est vide la GateWay n'est pas connecter
        else: 
           #la gateway n'es pas connecter 2 cas Unlink command or failed to connect
           #1- failed to connect
           failedtoconnect_REF = self.UF.lastFIND(ircDDB_File, "has failed to connect", -9, -1)
           failedtoconnect_REF_dt = self.UF.lastFIND(ircDDB_File, "has failed to connect", -46, -26)
           #2- Unlink command
           Linkcommand_REF = self.UF.lastFIND(ircDDB_File, "Link command", 0, 0)
           Linkcommand_REF_dt = self.UF.lastFIND(ircDDB_File, "Link command", -22, -2)
           Unlinkcommand_REF = self.UF.lastFIND(ircDDB_File, "Unlink command", 0, 0)
           Unlinkcommand_REF_dt = self.UF.lastFIND(ircDDB_File, "Unlink command", -22, -2)
           if Linkcommand_REF_dt<Unlinkcommand_REF_dt: Refl_Connect = [False, "Unlink command"]
           else: 
                if failedtoconnect_REF_dt>Linkcommand_REF_dt: Refl_Connect = [False, Linkcommand_REF]
                else: Refl_Connect = [False, "Error link"]
        return Refl_Connect

    def ircddb_Conf(self):
        VAL={}
        line = self.UF.FILE(CONST.CONFIRCDDB)
        for ln in line:
            Start = int(ln.find("="))
            VAL[ln[0:Start]]=ln[Start+1:len(ln)-1]
        return VAL           
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
