import wave, struct
from wavefunctions import WaveFunctions
from Tkinter import *
from ttk import Frame, Button, Style
import tkMessageBox
import tkFileDialog
import os

from audiofile import AudioFile
class MixWaves:

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

        self.maxlen = max(self.len1,self.len2,self.len3)
        if self.maxlen == self.len1:
            self.name = self.wave1
        elif self.maxlen == self.len2:
            self.name = self.wave2
        else:
            self.name = self.wave3

        self.arr = []
        for i in range(self.maxlen):
            self.arr.append(0)


    def mix(self):
        
        for i in range(self.maxlen):

            if i < self.len1:
                self.arr[i] += self.wave1.new_data[i]
            if i < self.len2:
                self.arr[i] += self.wave2.new_data[i]
            if i < self.len3:
                self.arr[i] += self.wave3.new_data[i]
            if self.arr[i] > 32767:
                self.arr[i] = 32767
            if self.arr[i] < -32767:
                self.arr[i] = -32767


    def write(self, wname):
        final_data=struct.pack(self.name.fmt,*(self.arr))
	nw=wave.open(wname,'w')
	nw.setframerate(self.name.samplerate)
	nw.setnframes(self.name.frames)
	nw.setsampwidth(self.name.samplewidth)
	nw.setnchannels(self.name.channel)
	nw.writeframes(final_data)
	nw.close()

    def play(self):
        self.write("out.wav")
        a = AudioFile("out.wav")
        a.play()
        a.close()
