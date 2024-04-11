import wave
import numpy as np

ad=wave.open("assets/sounds/hit.wav","rb")
sample_rate=ad.getframerate()
no_frames=ad.getnframes()
no_channels=ad.getnchannels()
time_audio=sample_rate/no_frames
print("sample rate:",sample_rate)
print("no of channels:",no_channels)
print("no frames:",no_frames)
print("duration:",time_audio,"s")

ad_numpy=np.frombuffer(ad.readframes(-1),dtype=np.int16)
ad_numpy=np.fft.fft(ad_numpy)
ad_numpy=np.abs(ad_numpy)/np.max(ad_numpy)
#ad_numpy=ad_numpy/np.max(ad_numpy)
print(ad_numpy[0:17])

#numpy value*half of width screen *+half of width = x(in the range of width of screen)
print("start")
for i in range(100):
    height=int(ad_numpy[i]*200)


    