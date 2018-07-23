import time, threading
from time import sleep
from Tkinter import *


import os
import glob
class InfosDStarInLog:

    def FILE(self, File):
        list_of_files = glob.glob('/var/log/opendv/'+File+'*')
        theFile = open(max(list_of_files, key=os.path.getctime), 'r')
        FILE = theFile.readlines()
        theFile.close()
        return FILE

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
  
    def failed2connect(self):
        failed2connect = []
        for line in self.findWord("failed to connect", "ircDDBGateway"):
         failed2connect.append(line[3:int(line.find("failed to connect")-4)])
        return failed2connect
    

global listb

class App(object):
    def __init__(self, root):
        frm = Frame(root, borderwidth=2, relief=GROOVE)

        frm.pack(side=LEFT)
        # Ajout de labels
        Label(frm, text="Frame 1").pack()
        
        
        scrollbar = Scrollbar(frm, orient=VERTICAL)
        global listb
        listb = Listbox(frm, yscrollcommand=scrollbar.set)

        scrollbar.config(command=listb.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        listb.pack(fill=BOTH, expand=YES)




def InfiniteProcess():
    global listb
    sleep(0.1)
    for i in range(2):
        sleep(1)
        listb.insert(0, InfosDStar.failed2connect()[0])
    listb.insert(0, "Stop")

def callback():
    global listb
    listb.insert(0, "Stop")


InfosDStar = InfosDStarInLog() 



finish = False



Process = threading.Thread(target=InfiniteProcess)
Process.start()

fenetre = Tk()
fenetre['bg']='blue'


canvas = Canvas(fenetre, width=300, height=300, background='white')
canvas.pack()

label_failed_connect = Label(canvas, text="Failed to connect", justify='left')
label_failed_connect_window = canvas.create_window(0, 0, anchor='nw', window=label_failed_connect)    

label2 = Label(canvas, text="Hello World")
label_failed_connect_window = canvas.create_window(0, 20, anchor='nw', window=label2)    


app01 = App(canvas)
app02 = App(canvas)



fenetre.mainloop()

finish = True
Process.join()

