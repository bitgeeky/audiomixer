import wave, struct

from audiofile import AudioFile

class WaveFunctions:

    def __init__(self,wavepath):

        self.path = wavepath
        w=wave.open(self.path,'rb')
	self.channel=w.getnchannels()
	self.samplerate=w.getframerate()
	self.samplewidth=w.getsampwidth()
	self.frames=w.getnframes()
	self.raw_data=w.readframes(self.frames)
	w.close()
	
	self.samples=self.frames*self.channel
	if self.samplewidth==1:
            fmt="%iB" %self.samples
        elif self.samplewidth==2:
            fmt="%ih" %self.samples
            self.new_data=list(struct.unpack(fmt,self.raw_data))

    
    def amplify(self, factor):
        
        qty = factor
        for i in xrange(len(self.new_data)):
            if self.new_data[i]*qty>32767:
                self.new_data[i]=32767
            elif qty*self.new_data[i] < -32768:
                self.new_data[i]=-32768
            else:
                self.new_data[i]=self.new_data[i]*qty
    """
    def shift(self, factor):
    
    def scale(self, factor):
    """
    def write(self, name):
        if self.samplewidth==1:
            fmt="%iB" %self.frames*self.channel
        else:
            fmt="%ih" %self.frames*self.channel
	    final_data=struct.pack(fmt,*(self.new_data))
	    nw=wave.open(name,'w')
	    nw.setframerate(self.samplerate)
	    nw.setnframes(self.frames)
	    nw.setsampwidth(self.samplewidth)
	    nw.setnchannels(self.channel)
	    nw.writeframes(final_data)
	    nw.close()
    
    def play(self):
        a = AudioFile(self.path)
        a.play()
        a.close()
