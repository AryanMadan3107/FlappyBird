import pygame


pygame.init()

WIDTH=800
HEIGHT=600
Fps=60
clock=pygame.time.Clock()

screen=pygame.display.set_mode((WIDTH,HEIGHT))

bg=pygame.image.load("Lesson 7/images/bg.png")
ground=pygame.image.load("Lesson 7/images/ground.png")
groundx=0

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
    def update(self):
        self.counter+=1
        if self.counter > 5:
            self.index +=1
            if self.index > 2:
                self.index=0
            self.image = self.images[self.index]
            self.counter=0

birdgroup = pygame.sprite.Group()
fb = Bird(100,250)
birdgroup.add(fb)

run=True
while run:
    clock.tick(Fps) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg,(0,0))
    screen.blit(ground,(groundx,550))
    groundx-=2   
    if groundx<-100:
        groundx=0
    birdgroup.draw(screen)
    birdgroup.update()
    pygame.display.update()