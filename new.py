from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style
import tkMessageBox
import tkFileDialog
import os

class WaveOptions(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Wave Mixer")
        selectbutton = Button(self.parent, text="Select", command = self.ShowBrowser)
        selectbutton.pack(side = RIGHT)
        

    def ShowBrowser(self):
        file = tkFileDialog.askopenfile(parent=self.parent,mode='rb',title='Choose a file')
        if file != None:
            data = file.read()
            print "I got %d bytes from this file." % len(data)
            print "and name of file is: %s" % file.name
            file.close()

def main():
  
    root = Tk()
    root.geometry("200x300+300+300")
    app = WaveOptions(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
