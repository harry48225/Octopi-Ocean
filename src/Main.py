import pygame


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
backdrop = pygame.image.load('Backdrop.png').convert()

bubbles = pygame.image.load('bubbles.png')
x = 0
y = 0


class player(object):
     
    def __init__(self):
        
        self.x = self.y = 0
        self.pos = self.x, self.y
        self.direction = 'UP'
        self.speed = 1
    def moveup(self):
        
        self.y -= self.speed
        
        self.pos = self.x, self.y
        if self.direction == 'UP': 
            
            self.speed+=1
            
        else:
            
            self.speed = 1
        self.direction = 'UP'
    def movedown(self):
        
        self.y += self.speed
        
        self.pos = self.x, self.y
        if self.direction == 'DOWN': 
            
            self.speed+=1
            
        else:
            
            self.speed = 1 
        self.direction = 'DOWN'
    def moveleft(self):
        
        self.x -= self.speed
        
        self.pos = self.x, self.y
        if self.direction == 'LEFT': 
            
            self.speed+=1
            
        else:
            
            self.speed = 1 
        self.direction = 'LEFT'
    def moveright(self):
        
        self.x += self.speed
        self.pos = self.x, self.y
        if self.direction == 'RIGHT': 
            
            self.speed+=1
            
        else:
            
            self.speed = 1
        self.direction = 'RIGHT'
    def setsprite(self, sprite):
        self.defaultsprite = sprite
        self.sprite = sprite 
        
    def rotatesprite(self):
        
        if self.direction == 'UP':
        
            self.sprite = self.defaultsprite
            
        if self.direction == 'DOWN':
        
            self.sprite = pygame.transform.rotate(self.defaultsprite, 180)
            
        if self.direction == 'LEFT':
        
            self.sprite = pygame.transform.rotate(self.defaultsprite, 90)
            
        if self.direction == 'RIGHT':
        
            self.sprite = pygame.transform.rotate(self.defaultsprite, 270)

octopus = player()

octopus.setsprite(pygame.image.load('8pi.png'))
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            raise SystemExit
    keypressed = pygame.key.get_pressed()
    
    if keypressed[pygame.K_w] and y >= 0:
        
        octopus.moveup()
        print 'up'
    if keypressed[pygame.K_s] and y < 720:
        
        octopus.movedown()
        print 'dwon'
    if keypressed[pygame.K_a] and x >= 0:
        
        octopus.moveleft()
        print 'left'
    if keypressed[pygame.K_d] and x < 1280:
        
        octopus.moveright()
        print 'right'
    octopus.rotatesprite()
    screen.blit(backdrop, (0,0))            
    screen.blit(octopus.sprite, (octopus.pos))

    if keypressed[pygame.K_SPACE]:
        
        screen.blit(bubbles, (x,y))
    
    pygame.display.flip()
    clock.tick(60)
                
                
                
