import pygame
import random


pygame.init()

WIDTH=800
HEIGHT=600
Fps=60
clock=pygame.time.Clock()
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency

score = 0
scorefont=pygame.font.SysFont("Arial",30)

screen=pygame.display.set_mode((WIDTH,HEIGHT))

bg=pygame.image.load("Lesson 7/images/bg.png")
ground=pygame.image.load("Lesson 7/images/ground.png")
groundx=0

flying=False
gameover=False

class Bird(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        for i in range(1,4):
            img = pygame.image.load(f'Lesson 7/images/bird{i}.png')
            self.images.append(img)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter=0
        self.velocity=0
        self.clicked=False
    def update(self):
        global gameover, flying
        if gameover == False:
            self.counter+=1
            if self.counter > 5:
                self.index +=1
                if self.index > 2:
                    self.index=0
                self.image = self.images[self.index]
                self.counter=0
        if flying == True and gameover==False:
            self.velocity += 0.3
            self.rect.y += self.velocity
            if self.rect.y > 520:
                self.rect.y = 520
                gameover=True
                flying=False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.velocity = -5
                    self.clicked=True
            if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked=False
            self.image=pygame.transform.rotate(self.images[self.index],self.velocity*-4)
        if gameover==True:
            self.image=pygame.transform.rotate(self.images[self.index],self.velocity*0)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x,y,position):
        pygame.sprite.Sprite.__init__(self)     
        self.image = pygame.image.load("Lesson 7/images/pipe.png")
        self.rect = self.image.get_rect()
        if position==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y]
        if position==-1:
            self.rect.topleft=[x,y]
    def update(self):
        self.rect.x-=5
        if self.rect.right<0:
            self.kill()
birdgroup = pygame.sprite.Group()
fb = Bird(100,250)
birdgroup.add(fb)

pipegroup = pygame.sprite.Group()


run=True
while run:
    clock.tick(Fps) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            flying=True
    screen.blit(bg,(0,0))
    scoretxt=scorefont.render(str(score),True,"white")
    screen.blit(scoretxt,(400,50))
    pipegroup.draw(screen)
    if gameover==False:
        groundx-=2
        if groundx<-100:
            groundx=0
    birdgroup.draw(screen)
    birdgroup.update()
    time_now=pygame.time.get_ticks()
    if gameover==False and flying==True:
        if time_now - last_pipe>pipe_frequency:
            pipegap=random.randint(50,100)
            tp=Pipe(800,300-pipegap,1)
            pipegroup.add(tp)
            bp=Pipe(800,300+pipegap,-1)
            pipegroup.add(bp)
            last_pipe=time_now
    screen.blit(ground,(groundx,550))
    pipegroup.update()
    pygame.display.update()