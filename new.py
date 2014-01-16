from Tkinter import *
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
        selectbutton.pack(anchor=CENTER)
    
        ##work for amp slider
        var = DoubleVar()
        scale = Scale( self.parent, variable = var, orient=HORIZONTAL )
        scale.pack(anchor=CENTER)
        alabel = Label(self.parent,text = "Amplitude")
        alabel.pack()

        ##work for Time Shift slider
        var = DoubleVar()
        scale = Scale( self.parent, variable = var, orient=HORIZONTAL )
        scale.pack(anchor=CENTER)
        alabel = Label(self.parent,text = "Time Shift")
        alabel.pack()

        ##work for Time Scaling slider
        var = DoubleVar()
        scale = Scale( self.parent, variable = var, orient=HORIZONTAL )
        scale.pack(anchor=CENTER)
        alabel = Label(self.parent,text = "Time Scaling")
        alabel.pack()

	CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        C1 = Checkbutton(self.parent, text = "Time Reversal", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
        C2 = Checkbutton(self.parent, text = "Select for Modulation", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
        C3 = Checkbutton(self.parent, text = "Select for Mixing", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
        C1.pack()
        C2.pack()
        C3.pack()

    def ShowBrowser(self):
        file = tkFileDialog.askopenfile(parent=self.parent,mode='rb',title='Choose a file')
        if file != None:
            data = file.read()
            print "I got %d bytes from this file." % len(data)
            print "and name of file is: %s" % file.name
            file.close()

def main():
  
    root = Tk()
    root.geometry("300x400+300+300")
    app = WaveOptions(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
