import pygame
from threading import Thread # This is really important for separate events
# todo: create a class for screen

pygame.init()
clock = pygame.time.Clock()
screenData = pygame.display.Info() # Creates an info onject on the currents users screen properties
screen = pygame.display.set_mode((screenData.current_w, screenData.current_h)) # Adjusts the game screen to fit the users screen
#screen = pygame.display.set_mode((1280,720)))
pygame.display.toggle_fullscreen() # Doesn't work yet
backdrop = pygame.image.load('Backdrop.png').convert() # what does .convert do?

bubbles = pygame.image.load('bubbles.png')
x = 0
y = 0

class player(object):
     
    def __init__(self):
        self.x = self.y = 0
        self.pos = self.x, self.y
        self.direction = 'UP'
        self.maximumSpeed = 20 # Pixels per frame

        self.speed = 1
    def moveup(self):
        self.y -= self.speed
        self.pos = self.x, self.y

        if self.direction == 'UP' and self.speed <= self.maximumSpeed:
            self.speed+=1

        else:
            self.speed = 1
        self.direction = 'UP'

    def movedown(self):
        self.y += self.speed
        self.pos = self.x, self.y

        if self.direction == 'DOWN' and self.speed <= self.maximumSpeed:
            self.speed+=1
            
        else:
            self.speed = 1 
        self.direction = 'DOWN'

    def moveleft(self):
        self.x -= self.speed
        self.pos = self.x, self.y

        if self.direction == 'LEFT' and self.speed <= self.maximumSpeed:
            self.speed+=1
            
        else:
            self.speed = 1 
        self.direction = 'LEFT'

    def moveright(self):
        self.x += self.speed
        self.pos = self.x, self.y

        if self.direction == 'RIGHT' and self.speed <= self.maximumSpeed:
            self.speed+=1
            
        else:
            self.speed = 1
        self.direction = 'RIGHT'

    def setsprite(self, sprite):
        self.defaultsprite = sprite
        self.sprite = sprite 
        
    def rotatesprite(self, directionGiven = None):
        if self.direction or directionGiven == 'UP':
            self.sprite = self.defaultsprite
            
        if self.direction == 'DOWN':
            self.sprite = pygame.transform.rotate(self.defaultsprite, 180)
            
        if self.direction == 'LEFT':
            self.sprite = pygame.transform.rotate(self.defaultsprite, 90)
            
        if self.direction == 'RIGHT':
            self.sprite = pygame.transform.rotate(self.defaultsprite, 270)

octopus = player()
octopus.setsprite(pygame.image.load('8pi.png'))

def updateScreen(): # Becuase threads still need to update the game | Unless you have it in the main loop | but still... a function for this is easier
    pygame.display.flip()
    clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    keypressed = pygame.key.get_pressed()
    
    if keypressed[pygame.K_w] and y >= 0:
        octopus.moveup()
        print 'up'

    elif keypressed[pygame.K_s] and y < 720:
        octopus.movedown()
        print 'dwon'

    elif keypressed[pygame.K_a] and x >= 0:
        octopus.moveleft()
        print 'left'

    elif keypressed[pygame.K_d] and x < 1280:
        octopus.moveright()
        print 'right'

    octopus.rotatesprite()
    screen.blit(backdrop, (0,0))            
    screen.blit(octopus.sprite, (octopus.pos))

    if keypressed[pygame.K_SPACE]:
        screen.blit(bubbles, (x,y))
    
    pygame.display.flip()
    clock.tick(60)
                
