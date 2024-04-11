import numpy as np
import pygame
import wave
import sys
pygame.init()

# Open the audio file
audio_file = wave.open("assets/sounds/wing.wav", "r")

# Get the audio data and sample rate
audio_data = np.frombuffer(audio_file.readframes(-1), dtype=np.int16)
sample_rate = audio_file.getframerate()

# Initialize pygame


# Set the window size
window_size = (677, 200)

scrn = pygame.display.set_mode(window_size)

for i in range(len(audio_data) - 1):
    x1=int(i* window_size[0]/len(audio_data))
    width=int((i+1)* window_size[0]/len(audio_data))-x1
    y1=int((audio_data[i]/2**15)*window_size[1]/2+window_size[1]/2)
    height=int((audio_data[i+1]/2**15)*window_size[1]/2+window_size[1]/2)-y1
    pygame.draw.rect(scrn,(192,192,192),(x1,y1,width,height))
    pygame.display.update()
running = True


    # Clear the screen
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the waveform
    


        # pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2))

    # Update the display


# Close the audio file and pygame
audio_file.close()

