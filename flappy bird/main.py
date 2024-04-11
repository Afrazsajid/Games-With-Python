import pygame

import random
import time
import sys

pygame.init()
scrn=pygame.display.set_mode((550,900))
clock=pygame.time.Clock()

width,height=scrn.get_size()



FPS=5

gamex=int(width*0.15)
gamey=int(height*0.3)
images={}
sound={}


images['numbers']=(
pygame.image.load('assets/sprites/0.png').convert_alpha(), 
pygame.image.load('assets/sprites/1.png').convert_alpha(), 
pygame.image.load('assets/sprites/2.png').convert_alpha(), 
pygame.image.load('assets/sprites/3.png').convert_alpha(), 
pygame.image.load('assets/sprites/4.png').convert_alpha(), 
pygame.image.load('assets/sprites/5.png').convert_alpha(), 
pygame.image.load('assets/sprites/6.png').convert_alpha(),
pygame.image.load('assets/sprites/7.png').convert_alpha(), 
pygame.image.load('assets/sprites/8.png').convert_alpha(), 
pygame.image.load('assets/sprites/9.png').convert_alpha()
)


images['gameover']=pygame.image.load('assets/sprites/gameover.png').convert_alpha()

images['players']=pygame.transform.scale(pygame.image.load('assets/sprites/flappy.png').convert_alpha(),(15*width/100,17*width/100))

images['pipe1']=pygame.transform.scale(pygame.image.load('assets/sprites/pipe1.png').convert_alpha(),(400,height))
images['pipe2']=pygame.transform.scale(pygame.image.load('assets/sprites/pipe2.png').convert_alpha(),(400,height))

images['background']=pygame.transform.scale(pygame.image.load('assets/sprites/background.png').convert(),(width,height))

images['base']=pygame.transform.scale(pygame.image.load('assets/sprites/base.png').convert_alpha(),(width+10,int(height*0.5)))

soundExt='.wav'


sound['hit'] = pygame.mixer.Sound('assets/sounds/hit' + soundExt)

sound['point'] = pygame.mixer.Sound('assets/sounds/point' + soundExt)
 
sound['wing'] = pygame.mixer.Sound('assets/sounds/wing' + soundExt)

def bird(playery,playerx,birdrot):
    image=pygame.transform.rotate(images['players'],birdrot)
    scrn.blit(image, (playerx,playery))
    
def base(basey):
    scrn.blit(images['base'], (0-5,basey))
def background():
    scrn.blit(images['background'], (0,0))    

def gameover():
     scrn.blit(images['gameover'],(gamex,gamey))
     pygame.display.update()
        
    
    

def welcomescreen():
    scrn.fill((0,0,0))
    time.sleep(1)
    birdrot=0
    basey = height*0.67
    playery=height*0.4
    playerx=width*0.3
    bird(playery,playerx,birdrot)
    base(basey)
    pygame.display.update()
    while True:
        #scrn.blit(images['pipe1'],(pipe[0]['x'],pipe[0]['y']))
        #pygame.display.update()
        #clock.tick(32)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                sound['wing'].play()
                return(9)
                        
def main(timet):
    birdrot=0
    score=0
    basey = height*0.67
    playery=height*0.4
    playerx=width*0.3
    
    playervel=-10
    playermaxvel=20
    playeraccy=2
    playeraccv=-12
    
    
    playerflapped=False
    
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # list of upper pipes
    upperPipes = [
        {
            'x': width + 200,
            'y': newPipe1[0]['y']
        },
        {
            'x': width + 200 + (width / 2),
            'y': newPipe2[0]['y']
        },
    ]

    # list of lowerpipe
    lowerPipes = [
        {
            'x': width + 200,
            'y': newPipe1[1]['y']
        },
        {
            'x': width + 200 + (width / 2),
            'y': newPipe2[1]['y']
        },
    ]

    pipeVelX = -6
    
    while True:
        if int(time.time()-timet)>2:
            score += 1
            sound['point'].play()

            timet=time.time()                                


                                                                         
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()            
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                playervel=playeraccv
                playerflapped=True
                sound['wing'].play()
                birdrot=23
        if playervel<playermaxvel and not playerflapped:
            playervel+=playeraccy
        if playerflapped:
            playerflapped=False
            
        
        
        birdrot-=2

                
                
        
            # player move
        if crashtest(upperPipes,lowerPipes,playerx,playery):
            sound['hit'].play()
            gameover()
            time.sleep(1)
            return 'gameover'
            
            
  
        
        
              
            
        playerHeight = images['players'].get_height()
        playery += playervel
        background()
        base(basey)
        bird(playery,playerx,birdrot)
        showScore
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            uPipe['x'] += pipeVelX
            lPipe['x'] += pipeVelX
   
       

            
            
            
            
            
                   #remove pipe             
        if len(upperPipes) > 0 and upperPipes[0]['x'] < -images['pipe1'].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])          
             
            
            
            
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            scrn.blit(images['pipe1'], (uPipe['x'], uPipe['y']))
            scrn.blit(images['pipe2'] , (lPipe['x'], lPipe['y']))            
                        
        showScore(score)
        clock.tick(32)
        pygame.display.update()          
            
            
def getRandomPipe():
    basey=int(height*0.67)
    pipex=width-200
    gap=100
    offset=int(height*0.3)
    pipe1y=random.randint(offset,basey-10)
    pipe2y=int(pipe1y-gap-images['pipe1'].get_height())
    
    return [
    {'x':pipex , 'y':pipe2y},
    {'x':pipex , 'y':pipe1y+gap}
    ]


def crashtest(upperpipes,lowerpipes,playerx,playery):
    basey=int(height*0.67)
    if playery-85>=basey:
        return True
    for Upipe,Lpipe in zip(upperpipes,lowerpipes):
        if Upipe['x']>0:
            if (playerx+12)>Upipe['x']+47:
                if playery>Lpipe['y']-50 or playery<Upipe['y']+images['pipe1'].get_height()-50:
                    return True
def showScore(score):
    """displays score in center of screen"""
    scoreDigits = [int(x) for x in list(str(score))]
    totalWidth = 0  # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += images['numbers'][digit].get_width()

    Xoffset = (width - totalWidth) / 2

    for digit in scoreDigits:
        scrn.blit(images['numbers'][digit], (Xoffset, height * 0.1))
        Xoffset += images['numbers'][digit].get_width()
        
                                        
while True:
    welcomescreen()
    start=time.time()
    main(start)
    

