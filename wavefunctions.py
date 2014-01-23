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
        self.fmt = fmt
        
        self.new_data=list(struct.unpack(fmt,self.raw_data))

    
    def amplify(self, factor):
        
        qty = factor
        for i in xrange(len(self.new_data)):
            if self.new_data[i]*qty > 32767:
                self.new_data[i] = 32767
            elif qty*self.new_data[i] < -32768:
                self.new_data[i] = -32768
            else:
                self.new_data[i]=self.new_data[i]*qty
    
    def shift(self, factor):
        new = []
        ftoshift = factor * self.samplerate
        ftoshift = abs(ftoshift)
        if factor < 0:
            if self.channel == 1:
                self.new_data = self.new_data[ftoshift::1]
            else:
                self.new_data = self.new_data[2*ftoshift::1]
        
        else:
            if self.channel == 1:
                for i in range(int(ftoshift)):
                    new.append(0)
            else:
                for i in range(2*int(ftoshift)):
                    new.append(0)
            self.new_data = new + self.new_data

        self.frames = len(self.new_data)/self.channel
    
    def scale(self, factor):
        if factor == 0:
            return
        new = []
        new1 = []
        new2 = []
        if self.channel == 1:
            for i in range(int(len(self.new_data)/factor)):
                new.append(self.new_data[int(factor*i)])
        else:
            for i in range(len(self.new_data)):
                if i%2 == 0:
                    new2.append(self.new_data[i])
                else:
                    new1.append(self.new_data[i])
            for i in range(int(len(new2)/factor)):
                new.append(new2[int(factor*i)])
                new.append(new1[int(factor*i)])
        self.new_data = new
        self.frames = len(self.new_data)/self.channel
    
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

    def reverse(self):
        self.new_data.reverse()
    
    def play(self):
            self.write("out.wav")
            a = AudioFile("out.wav")
            a.play()
            a.close()
