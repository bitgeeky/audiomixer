import wave, struct
from wavefunctions import WaveFunctions
from Tkinter import *
from ttk import Frame, Button, Style
import tkMessageBox
import tkFileDialog
import os

class ModulateWaves:

    def __init__(self, name1=None, name2=None, name3=None):
        
	if name1 is None:
            self.wave1 = None
            self.len1 = 0
        else:
            self.wave1 = WaveFunctions(name1)
            self.len1 = len(self.wave1.new_data)

        if name2 is None:
            self.wave2 = None
            self.len2 = 0
        else:
            self.wave2 = WaveFunctions(name2)
            self.len2 = len(self.wave2.new_data)
        
        if name3 is None:
            self.wave3 = None
            self.len3 = 0
        else:
            self.wave3 = WaveFunctions(name3)
            self.len3 = len(self.wave3.new_data)

        if self.len1 == 0:
            newlen1 = self.len1 + 100000000
        if self.len2 == 0:
            newlen2 = self.len2 + 100000000
        if self.len3 == 0:
            newlen1 = self.len3 + 100000000
        
        self.maxlen = max(self.len1,self.len2,self.len3)
        self.minlen = min(newlen1, newlen2, newlen3)
        for i in range(self.maxlen):
            arr.append(1)

    def modulate(self):
        
        for i in range(self.maxlen):
            if self.len1 is not 0 and i < self.minlen:
                arr[i] *= self.wave1.new_data[i]
            if self.len2 is not 0 and i < self.minlen:
                arr[i] *= self.wave2.new_data[i]
            if self.len3 is not 0 and i < self.minlen:
                arr[i] *= self.wave3.new_data[i]
            if i >= self.minlen:
                arr[i] = 0;

    def write(self, name):
        # fmt to be defined
        final_data=struct.pack(fmt,*(self.arr))
	nw=wave.open(name,'w')
	nw.setframerate(self.samplerate)
	nw.setnframes(self.frames)
	nw.setsampwidth(self.samplewidth)
	nw.setnchannels(self.channel)
	nw.writeframes(final_data)
	nw.close()
