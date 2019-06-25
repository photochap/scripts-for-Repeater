#!/usr/bin/python3
##########################################
# ScreenDStar
##########################################
# Python 3
# if python 2
#    from Tkinter import *
#    import ConfigParser
#
#Import library
from utilitaire_gestion_des_fichiers import *

import CONST
import threading
import os
import configparser
import pyinotify
import glob

 

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        if not event.dir:
            gui.updateGUI(event.pathname)


class WatchFile(threading.Thread):
      def run(self):
          wm = pyinotify.WatchManager()
          mask = pyinotify.IN_MODIFY
          directory = '/var/log/opendv'
          handler = EventHandler()
          notifier = pyinotify.Notifier(wm, handler)
          wdd = wm.add_watch(directory, mask, rec=True, auto_add=True)
          notifier.loop()
          self.notifier = notifier


class Gui(object):
    def __init__(self):
        self.UF = Util_File()       
        self.GF = InfosDStarInLog() 
        self.GF.ircddb_Conf()
        self.init()

    def CONNECT(self):
        print("CONNECT -------------------------------------")
        Etat_Connect = self.GF.Connect_REF()
        print(Etat_Connect)

    def init(self):
        print ("Connect init--------------------------------------")
        print (self.CONNECT())       
        print (self.GF.My(3))

    def updateGUI(self, File):
        print("updateGUI -------------------------------------")
        #All log write in Logs_LB
        print (File)
        print (self.UF.lastLINE(File))        
        #ircDDBGateway-2018-07-25.log
        if File.find("ircDDBGateway")>0:
           print ("Connect --------------------------------------")

        #Headers.log
        if File.find("Headers")>0:
           print (self.GF.My(3))
           
        if File.find("Links")>0:
            print ("File link ---------------------------------")
            print (self.CONNECT())       

        return
    
    
gui = Gui()
WF = WatchFile()
WF.start()






























