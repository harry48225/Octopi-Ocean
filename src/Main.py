import pygame

import time
pygame.init()

screen = pygame.display.set_mode((1280,720))

octopus = pygame.image.load('8pi.png').convert()
x = 0
y = 0
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            raise SystemExit
    keypressed = pygame.key.get_pressed()
    
    if keypressed[pygame.K_w] and y > 0:
        
        y -= 0.1
        
    if keypressed[pygame.K_s] and y < 720:
        
        y += 0.1
        
    if keypressed[pygame.K_a] and x > 0:
        
        x -= 0.1
        
    if keypressed[pygame.K_d] and x < 1280:
        
        x += 0.1    
    screen.fill((0,0,0))            
    screen.blit(octopus, (x,y))
    pygame.display.flip()
                
                
                
