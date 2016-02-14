import pygame

import time
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
backdrop = pygame.image.load('Backdrop.png').convert()
octopus = pygame.image.load('8pi.png')
bubbles = pygame.image.load('bubbles.png')
x = 0
y = 0

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            raise SystemExit
    keypressed = pygame.key.get_pressed()
    
    if keypressed[pygame.K_w] and y > 0:
        
        y -= 1
        
    if keypressed[pygame.K_s] and y < 720:
        
        y += 1
        
    if keypressed[pygame.K_a] and x > 0:
        
        x -= 1
        
    if keypressed[pygame.K_d] and x < 1280:
        
        x += 1
        
        
    screen.blit(backdrop, (0,0))            
    screen.blit(octopus, (x,y))

    if keypressed[pygame.K_SPACE]:
        
        screen.blit(bubbles, (x,y))
    
    pygame.display.flip()
    clock.tick(60)
                
                
                
