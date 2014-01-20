import wave, struct

waveFile = wave.open('wavefiles/test.wav', 'r')

length = waveFile.getnframes()
for i in range(0,length):
    waveData = waveFile.readframes(1)
    data = struct.unpack("<h", waveData)
    print int(data[0])
