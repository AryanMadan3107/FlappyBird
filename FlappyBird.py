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
    pygame.display.update()