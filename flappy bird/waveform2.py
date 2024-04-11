import pygame as pg
import numpy as np
import wave as wv

pg.init()
size=(300,200)
scrn=pg.display.set_mode(size)

audio=wv.open('assets/sounds/wing.wav','rb')
audio=audio.readframes(-1)

auData=np.frombuffer(audio,dtype=np.int16)

auData=auData/2**15
length=len(auData)
for i in range(length-1):
    y1=auData[i]*size[1]/2+size[1]/2
    y2=auData[i+1]*size[1]/2+size[1]/2
    x1=(size[0]/length)*i
    x2=(size[0]/length)*i+1
    pg.draw.line(scrn,(125,125,125),(x1,y1),(x2,y2))
    pg.display.update()
    



