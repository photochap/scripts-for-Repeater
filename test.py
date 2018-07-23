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
        def onselect(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            detail.delete('1.0', END)
            detail.insert(END,str(value*value))
        lbl1 = Label(root, text="Result:", fg='black',
                    font=("Helvetica", 16, "bold"))
        lbl2 = Label(root, text="Detail:", fg='black',
                        font=("Helvetica", 16, "bold"))
        lbl1.grid(row=0, column=0,  sticky=W)
        lbl2.grid(row=2, column=0,  sticky=W)

        frm = Frame(root)
        frm.grid(row=1, columnspan=2, sticky=N + S + W + E)


        scrollbar = Scrollbar(frm, orient=VERTICAL)
        global listb
        listb = Listbox(frm, yscrollcommand=scrollbar.set, width=50)
        scrollbar.config(command=listb.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        listb.pack(fill=BOTH, expand=YES)

        detail = Text(root, height=10, font=("Helvetica", 12))
        detail.grid(row=6, columnspan=2, sticky=E + W + N)
        listb.bind('<<ListboxSelect>>', onselect)

InfosDStar = InfosDStarInLog() 

def InfiniteProcess():
    global listb
    sleep(0.1)
    for i in range(10000):
        sleep(1)
        vw = listb.yview()
        listb.insert(0, InfosDStar.failed2connect()[0])
        listb.yview_moveto(vw[-1])
        #print(i)

finish = False
Process = threading.Thread(target=InfiniteProcess)
Process.start()

mainWindow = Tk()
app = App(mainWindow)
mainWindow.mainloop()
finish = True
Process.join()