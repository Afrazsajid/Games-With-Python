import pygame
import sys
import time
import random
import time
pygame.init()

scrn=pygame.display.set_mode((500,750))

width,height=scrn.get_size()

clock=pygame.time.Clock()

class Road:
    def __init__(self):
        self.image=pygame.transform.scale(pygame.image.load('assets/sprites/road.png'),(400,750))
        self.x=50
        self.y1=0
        self.y2=-750

        
        scrn.blit(self.image,(self.x,self.y1))
        
    def update(self,gameVel):
        self.y2+=gameVel
        self.y1+=gameVel
        if self.y1>=height:
            self.y1=-750
        if self.y2>=height:
            self.y2=-750  
    def draw(self):
        scrn.blit(self.image,(self.x,self.y1))
        scrn.blit(self.image,(self.x,self.y2))

class objects:
    def __init__(self):
        self.moveX=25
        self.moveY=20
        self.image=pygame.image.load('assets/sprites/cars/4.png').convert_alpha()
        self.height=self.image.get_height()
        self.width=self.image.get_width()
        self.x=width/2
        self.y=int(height-self.height)
                
    def draw(self):
        scrn.blit(self.image,(self.x,self.y))

    def updtae(self,right,left,up,down):
        if right==True:
            if self.x+self.width>=width-70:
                pass
            else:
                self.x+=self.moveX
        if left==True:
            if self.x<=76:
                pass
            else:
                self.x-=self.moveX            
        if up==True:
            if self.y<=0:
                pass
            else:
                self.y-=self.moveY            
        if down==True:
            if self.y+self.height>=height:
                pass
            else:
                self.y+=self.moveY
            
class enemy:
    def __init__(self):
    
        self.enemies_images=(
        # pygame.transform.rotate(pygame.image.load('assets/sprites/cars/1.png').convert_alpha(),180),
        pygame.transform.rotate(pygame.image.load('assets/sprites/cars/2.png').convert_alpha(),180),
        pygame.transform.rotate(pygame.image.load('assets/sprites/cars/3.png').convert_alpha(),180),
        pygame.transform.rotate(pygame.image.load('assets/sprites/cars/4.png').convert_alpha(),180),
        pygame.transform.rotate(pygame.image.load('assets/sprites/cars/5.png').convert_alpha(),180),
        pygame.transform.rotate(pygame.image.load('assets/sprites/cars/6.png').convert_alpha(),180),
        pygame.transform.rotate(pygame.image.load('assets/sprites/cars/7.png').convert_alpha(),180),
        pygame.transform.rotate(pygame.image.load('assets/sprites/cars/8.png').convert_alpha(),180),


        pygame.image.load('assets/sprites/barrel.png').convert_alpha(),
        pygame.image.load('assets/sprites/roadblock.png').convert_alpha()
        )

        self.Xrange=(55,350)
        self.offset=int(height*0.60)
        self.enemies=[
            {'image':self.enemies_images[2],"x":200,'y':-100}
        ]



    def add(self):
        for enemy in self.enemies:
            img_indx=random.randint(0,len(self.enemies_images)-1)
            x=random.randint(self.Xrange[0],self.Xrange[1])
            y=-100
            
            if enemy['y']>=self.offset and enemy['y']<=self.offset+2:
                dic={
                    'image':self.enemies_images[img_indx],'x':x,'y':y
                }
                self.enemies.append(dic)

    def update(self,gameVel):
        for enemy in self.enemies:
            enemy['y']+=gameVel
            if self.enemies[0]['y']>height and len(self.enemies)>1:
                 self.enemies.pop(0)
                

    def draw(self):
        
        for enemyy in self.enemies:
            image=enemyy['image']
            x=enemyy['x']
            y=enemyy['y']
            scrn.blit(image,(x,y))          
                        




        


        
        


blast_w=width*0.06
blast_h=height*0.06

images={}
sounds={}

images['bg']=pygame.image.load('assets/sprites/bg.png').convert_alpha()
images['bg']=pygame.transform.scale(images['bg'],(width,height))


path='/numbers'
images['numbers']=(
pygame.image.load(f'assets/sprites{path}/0.png').convert_alpha(), 
pygame.image.load(f'assets/sprites{path}/1.png').convert_alpha(), 
pygame.image.load(f'assets/sprites{path}/2.png').convert_alpha(), 
pygame.transform.scale(pygame.image.load(f'assets/sprites{path}/3.png').convert_alpha(),(width*0.1,height*0.05)), 
pygame.image.load(f'assets/sprites{path}/4.png').convert_alpha(), 
pygame.image.load(f'assets/sprites{path}/5.png').convert_alpha(), 
pygame.image.load(f'assets/sprites{path}/6.png').convert_alpha(),
pygame.transform.scale(pygame.image.load(f'assets/sprites{path}/7.png').convert_alpha(),(width*0.1,height*0.05)), 
pygame.image.load(f'assets/sprites{path}/8.png').convert_alpha(), 
pygame.image.load(f'assets/sprites{path}/9.png').convert_alpha())

images['blast']=pygame.image.load('assets/sprites/blast.png').convert_alpha()
images['blast']=pygame.transform.scale(images['blast'],(blast_w,blast_h))

images['coin']=pygame.image.load('assets/sprites/coin.png').convert_alpha()
images['coin']=pygame.transform.scale(images['coin'],(blast_w+30,blast_h+30))


images['home']=pygame.image.load('assets/sprites/home.png').convert_alpha()
images['home']=pygame.transform.scale(images['home'],(width,height))

images['gameover']=pygame.image.load('assets/sprites/gameover.png').convert_alpha()
images['gameover']=pygame.transform.scale(images['gameover'],(300,300))


images['enter']=pygame.image.load('assets/sprites/enter.png').convert_alpha()
images['enter']=pygame.transform.scale(images['enter'],(400,200))


tpe='.mp3'

sounds['music']=pygame.mixer.Sound('assets/sounds/car_game_music' + tpe)
sounds['click']=pygame.mixer.Sound('assets/sounds/click' + tpe)
sounds['coin']=pygame.mixer.Sound('assets/sounds/coin' + tpe)
sounds['crash']=pygame.mixer.Sound('assets/sounds/crash' + tpe)



#initalizing all components road,cae,enemies



def home():
    times=time.time()
    
    while True:

        if time.time()-times>=1:
            return (9)
        scrn.blit(images['home'],(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
        pygame.display.update()

def main():
    fps=36
    max_fps=120
    gameVel=5
    i=0
    sounds['music'].play()
    vel=5
    bgX=0
    bgY1=0
    bgY2=-height
    st_time=time.time()
    score=0
    level_check=5

    while True:
        if score>level_check:
            if fps<max_fps:
                fps+=6
            if enemeY.offset>200:
                sounds['click'].play()
                enemeY.offset-=5
            level_check+=3         

        if crashTest(player,enemeY):
            sounds['music'].stop()
            sounds['crash'].play()
            return 'gameover'
        if time.time()-st_time>2:
            score+=1

            st_time=time.time()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    player.updtae(True,False,False,False)

                if event.key==pygame.K_LEFT:
                    player.updtae(False,True,False,False)

                if event.key==pygame.K_UP:
                    player.updtae(False,False,True,False)

                if event.key==pygame.K_DOWN:
                    player.updtae(False,False,False,True)


        bgY1+=vel
        bgY2+=vel
        if bgY1>=height:
            bgY1=-height

        if bgY2>=height:
            bgY2=-height

        scrn.blit(images['bg'],(bgX,bgY1))
        scrn.blit(images['bg'],(bgX,bgY2))
        road.draw()
        road.update(gameVel)
        player.draw()

        enemeY.draw()
        enemeY.add()
        enemeY.update(gameVel)
        showScore(score)


        clock.tick(fps)
        pygame.display.update()

def crashTest(player,enemY):
    
    player_rect=pygame.Rect(player.x+11,player.y+11,player.image.get_width()-11,player.image.get_height()-11)
    
    for enemy in enemY.enemies:
        enemy_rect=pygame.Rect(enemy['x'],enemy['y'],enemy['image'].get_width(),enemy['image'].get_height())
        if pygame.Rect.colliderect(player_rect,enemy_rect):
            print("truetruettttttttt")
            return True
        else:
            return False


def showScore(score):
    """displays score in center of screen"""
    scoreDigits = [int(x) for x in list(str(score))]
    totalWidth = 0  # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += images['numbers'][digit].get_width()

    Xoffset = (width - totalWidth)*0.97

    for digit in scoreDigits:
        scrn.blit(images['numbers'][digit], (Xoffset, height * 0.04))
        Xoffset += images['numbers'][digit].get_width()                


def showGameover():
    scrn.blit(images['gameover'],(100,height*0.1))
    scrn.blit(images['enter'],(50,height*0.5))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                print(event.key)
                if event.key==pygame.K_KP_ENTER or event.key==13:
                    return 9


                    
                



    

if __name__=='__main__':
    home()

    while True:
        road=Road()
        player=objects()
        enemeY=enemy()
        main()
        showGameover()
        






