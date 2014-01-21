from Tkinter import *
from ttk import Frame, Button, Style
import tkMessageBox
import tkFileDialog
import os

from mixwaves import MixWaves
from wavefunctions import WaveFunctions
from mixbutton import MixButton
from modulatebutton import ModulateButton

class WaveOptions(Frame):
    
    
    def __init__(self, parent):
        
        # Object Vriables
        self.name = None
        self.ampval = DoubleVar()
        self.tscaleval = DoubleVar()
        self.tshiftval = DoubleVar()
        self.trevval = DoubleVar()
        self.isrev = IntVar() 
        self.ismodul = IntVar() 
        self.ismix = IntVar() 
        
        # Initialize Frame
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
        
    def initUI(self):
      
        # Select Button
        selectbutton = Button(self.parent, text="Select", command = self.ShowBrowser)
        selectbutton.pack(anchor=CENTER)
    
        # Amp slider
        var = DoubleVar()
        ascale = Scale( self.parent, variable = self.ampval, orient=HORIZONTAL )
        ascale.pack(anchor=CENTER)
        alabel = Label(self.parent,text = "Amplitude")
        alabel.pack()

        # Time Shift slider
        var = DoubleVar()
        tshscale = Scale( self.parent, variable = self.tshiftval, orient=HORIZONTAL )
        tshscale.pack(anchor=CENTER)
        tshlabel = Label(self.parent,text = "Time Shift")
        tshlabel.pack()

        # Time Scaling slider
        var = DoubleVar()
        tscscale = Scale( self.parent, variable = self.tscaleval, orient=HORIZONTAL )
        tscscale.pack(anchor=CENTER)
        tsclabel = Label(self.parent,text = "Time Scaling")
        tsclabel.pack()

	# Time Reversal Check Button
        CheckVar1 = IntVar()
        C1 = Checkbutton(self.parent, text = "Time Reversal", variable = self.isrev, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
        C1.pack()
       
        # Modulation Button
        CheckVar2 = IntVar()
        C2 = Checkbutton(self.parent, text = "Select for Modulation", variable = self.ismodul, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
        C2.pack()
       
        # Mixing Button
        CheckVar3 = IntVar()
        C3 = Checkbutton(self.parent, text = "Select for Mixing", variable = self.ismix, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
        C3.pack()
        
        # Play Button
        playbutton = Button(self.parent, text="Play", command = self.PlayWave)
        playbutton.pack(anchor=CENTER)
        
    def ShowBrowser(self):
        file = tkFileDialog.askopenfile(parent=self.parent,mode='rb',title='Choose a file')
        if file != None:
            data = file.read()
            print "I got %d bytes from this file." % len(data)
            print "and name of file is: %s" % file.name
            self.name = file.name
            file.close()
    
    def PlayWave(self):
        # apply wave operations
        wave = WaveFunctions(self.name)
        wave.amplify(self.ampval.get())
        wave.scale(self.tscaleval.get())
        wave.shift(self.tshiftval.get())
        if int(self.isrev.get()) == 1:
            wave.reverse()
        # more operations when added
        wave.play()

def main():
  
    root = Tk()                      # the main frame for application    
    root.geometry("600x410+300+300") # Specifications for the main frame
    
    # Wave Objects   
    frame_a = LabelFrame(root, text='Wave 1', padx=5, pady=5)
    frame_a.grid(sticky=E,row = 0, column = 0)
    app = WaveOptions(frame_a)
    
    frame_b = LabelFrame(root, text='Wave 2', padx=5, pady=5)
    frame_b.grid(sticky=W, row = 0, column = 1)
    app2 = WaveOptions(frame_b)
    
    frame_c = LabelFrame(root, text='Wave 3', padx=5, pady=5)
    frame_c.grid(sticky=W, row = 0, column = 2)
    app3 = WaveOptions(frame_c)
    
    frame_d = LabelFrame(root, text='Modulate and Play', padx=5, pady=5)
    frame_d.grid(sticky=E+W, row = 1, column = 0)
    obj1 = ModulateButton(frame_d)
    
    frame_e = LabelFrame(root, text='Mix and Play', padx=5, pady=5)
    frame_e.grid(sticky=E+W, row = 1, column = 2)
    obj = MixButton(frame_e)
    root.mainloop()  

if __name__ == '__main__':
    main()  
