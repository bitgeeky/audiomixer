from Tkinter import *
from ttk import Frame, Button, Style
import tkMessageBox
import tkFileDialog
import os

from mixwaves import MixWaves
from wavefunctions import WaveFunctions
class MixButton(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        # Select Button
        playbutton = Button(self.parent, text="Mixer", command = self.playmixed)
        playbutton.pack()
    
    def playmixed():
        print "playing"
