#TODO Add powerUPs!!!
import pygame
from random import randint
import math
from math import degrees
stopwatch = {'m': 0, 's': 0, 'mils':0}
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
backdrop = pygame.image.load('Backdrop1.png').convert()
pygame.font.init()

class highscore(object):
    
    def __init__(self):
        
        with open('highscore.txt') as highscores:
            highestscore = highscores.readline().rstrip()
            savedhighscore = 'High score: {0}'.format(highestscore)
            self.highestscore = int(highestscore)

            highscores.close()
        
        font = pygame.font.Font(None, 60)
        self.highscoredisplay = font.render(savedhighscore, 0, (255,255,255))
        
        
    def renderscore(self):
        
        screen.blit(self.highscoredisplay, (875, 0))
        
    
#Gameover function.

def gameover():

    #Draws the game over image.
    screen.blit(pygame.image.load('GAMEOVER.png'), (0,0)) 
    #.flip() need to be called for the screen to show the changes.
    pygame.display.flip()
    #FOREVER!
    
    currenthightotal = int(octopus.score)
    print currenthightotal
    highestscore = thehighscore.highestscore
    print highestscore
        
    if currenthightotal > highestscore:
        print 'New highscore'
        with open('highscore.txt', 'w') as highscores:
            
            highscores.write(str(currenthightotal))
            highscores.close()    
    while True:
        #JK XD. 
        for event in pygame.event.get():
            #Checks if the close button has been pressed.
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
#Player Class
class player(object):

    def __init__(self, sprite):
        self.sprite = self.currentsprite = self.defaultsprite = sprite
        self.rect = self.sprite.get_rect()
        self.damagedsprite = pygame.image.load('8pi1-damg.png')
        #How many hits it can take
        self.health = 3
        #Coordinates of image and hitbox
        self.x = self.y = self.rect.x = self.rect.y = 100
        self.pos = self.x, self.y
        self.speed = 1
        #Angle that it is facing. (Angles go anti-clockwise
        self.angle = 0    
        self.inkamount = 10
        self.score = 0
      
        
    def move(self):
        #Inital acceleration is fast
        if self.speed <= 8:

            self.speed += 3
        #It then slows down
        else:

            self.speed += 0.2
        #Python works in radians so the angle that is in degrees needs to be converted
        radians = math.radians(self.angle + 90)
        self.x += math.cos(radians) * self.speed
        self.y -= math.sin(radians) * self.speed
        
        #Moving off screen logic,
        if self.x > 1280:

            self.x = 0

        if self.x < 0:

            self.x = 1280

        if self.y < 0:

            self.y = 720

        if self.y > 720:

            self.y = 0
        
        #Refreshing the pos variable
        self.pos = self.x, self.y
        self.rect.x = self.x
        self.rect.y = self.y


    def rotatesprite(self):
        #Rotating the sprite over the same centre
        oldrect = self.sprite.get_rect()
        rotatedsprite = pygame.transform.rotate(self.currentsprite, self.angle)
        rotatedrect = oldrect.copy()
        rotatedrect.center = rotatedsprite.get_rect().center
        self.sprite = rotatedsprite.subsurface(rotatedrect).copy()


    def damaged(self):
        #This is only called when the octopus has been hit so we must subtract the damage
        self.health -= 1
        if self.health == 1:
            #Setting the sprite to the damaged one
            self.currentsprite = self.damagedsprite
        #No health so the game over function is called.
        if self.health == 0:
            gameover()
    #This is called at the end of the clock cycle it checks if anything has hit the octopus.
    #It also rotates the sprite so it is facing the direction specified by the angle.
    def refresh(self):

        for bally in baddieweapons:


            if self.rect.colliderect(bally.rect):
                print
                print 'HIT'
                print
                #Damage the octopus
                self.damaged()
                #Get rid of the ball so that it does not hit next frame
                bally.die()
                #Stop that ball from being updated again
                baddieweapons.remove(bally)
                
        #Make sprite face the right directions
        self.rotatesprite()
        font = pygame.font.Font(None, 60)
        INKamountdisplay = font.render('INK amount: {0}'.format(self.inkamount), 0, (255,255,255))
        screen.blit(INKamountdisplay, (0, 660))
        scoreamountdisplay = font.render('Score: {0}'.format(int(self.score)), 0, (255,255,255))
        screen.blit(scoreamountdisplay, (0, 0))
    pass


class enemy(object):    #Enemy class
    # Initialisation
    def __init__(self,x, y):
        self.id = len(baddies)
        self.defaultsprite = self.sprite = pygame.image.load('baddie.png')
        self.rect = self.sprite.get_rect()
        self.x = x
        self.y = y
        self.pos = self.x, self.y
        self.angle = 0
        self.speed = 3
        self.shoot = 0
        self.shouldshoot = 0
        self.shouldmove = True
        
    def move(self):
        #This is called to move the enemy.
        print octopus.pos
        #Pythagoras to find out how far away from the octopus the enemy is.
        #This is so that all of the enemies do not target the octopus.
        #They only target it when it gets close-ish
        distancetoplayer = math.sqrt(((self.x - octopus.x) * (self.x - octopus.x)) + ((self.y - octopus.y) * (self.y - octopus.y)))
        if distancetoplayer < 500:
            
            if octopus.y > self.y:
                #Octopus is below enemy
                if octopus.x < self.x:
                    print 'BELOW LEFT'
                    #Octopus is left of the enemy therefore the angle is 360 - x
                    #                           atan is tan to the -1
                    angletoplayer= 90 - degrees(math.atan((octopus.y - self.y) / (octopus.x - self.x)))
                else:
                    print 'BELOW RIGHT'
                    #Octopus is right of the enemy
                    angletoplayer= 180 + degrees(math.atan((octopus.x - self.x) / (octopus.y - self.y)))
    
            if octopus.y < self.y:
    
                #Octopus is above enemy
                if octopus.x < self.x:
    
                    #octopus is left.
                    print 'UPLEFT'
                    angletoplayer = 0 + degrees(math.atan((self.x - octopus.x)/ (self.y - octopus.y)))
    
                if octopus.x > self.x:
                    print 'UPRIGHT'
                    #octopus is right
                    angletoplayer = 270 - degrees(math.atan((self.y - octopus.y)/ (self.x - octopus.x)))
            
            #This tells the enemy that it should shoot because it is pointing and the octopus.        
            self.shouldshoot = 1
            self.shouldmove = True
            if distancetoplayer < 100:
                self.shouldmove = False
        
        #Octopus not close enough for the other movement
        else:
            #It will now travel in a cicle.
            angletoplayer = self.angle + randint(0,3)
            if angletoplayer > 360:
                angletoplayer -= 360
                
            if angletoplayer < 0:
                angletoplayer = 360 + angletoplayer
            #Tells itself that it shouldn't shoot because it is not pointing at the player.
            self.shouldshoot = 0
            self.shouldmove = True
        #Rotation around the center.
        oldrect = self.sprite.get_rect()
        rotatedsprite = pygame.transform.rotate(self.defaultsprite, angletoplayer)
        rotatedrect = oldrect.copy()
        rotatedrect.center = rotatedsprite.get_rect().center
        self.sprite = rotatedsprite.subsurface(rotatedrect).copy()
        
        print angletoplayer
        #Traveling along the angle.
        radians = (angletoplayer + 90) * (math.pi / 180)
        
        if self.shouldmove:
            self.x += math.cos(radians) * self.speed
            self.y -= math.sin(radians) * self.speed
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = self.x, self.y
        self.angle = angletoplayer
    def refresh(self):
        #Called when at the end of each cycle.
        #Adding 1 to the shoot timer.
        self.shoot += 1
        #Moving
        self.move()
        #If 200 cycles (3 and a bit seconds) have passed from the last shoot
        #AND!! It is pointing at the octopus
        if self.shoot == 200 and self.shouldshoot == 1:
            #SHOOT!!!!
            baddieweapons.append(ball(self.angle, self.speed-10, self.rect, pygame.image.load('Harpoon.png')))
            #We have shot so the timer is reset
            self.shoot = 0
        #Checking if any of the players shots have hit it.
        for bally in playerweapons:
            if self.rect.colliderect(bally.rect):
                bally.die()
                playerweapons.remove(bally)
                #If they have...
                #My life is now a zero.
                #*cries*
                #The system will soon delete me.
                return False
        # Nothing hit me!!!
        return True


class ball(object):        #Weapon class

    def __init__(self, angle, speed, firerrect, sprite):
        #Making it face away from the firer
        self.sprite = pygame.transform.rotate(sprite, angle+270)
        self.x = firerrect.centerx 
        self.y = firerrect.centery
        self.angle = angle
        #Making it faster than the firer
        self.speed = speed + 20
        self.dead = False
      
        radians = math.radians(angle+90)
        self.x += math.cos(radians) * self.speed
        self.y -= math.sin(radians) * self.speed
        self.rect = self.sprite.get_rect()
        
        
        #Moving away from the firer before hits are detected.
        #This is so you cannot kill yourself.
        self.move()
        
        pass

    def move(self):
        #Movement
        if not self.dead:
                
            radians = math.radians(self.angle + 90)
            self.x += math.cos(radians) * self.speed
            self.y -= math.sin(radians) * self.speed
            self.rect.x = self.x
            self.rect.y = self.y
            
        if self.x > 1280 or self.x < 0:
            self.die()
        if self.y > 720 or self.y < 0:
            self.die()
    def die(self):
        #I know this is a pretty bad way of getting rid of the balls
        #But I don't really know what else to do with them
        self.x = self.y = 4000
        self.speed = 0
        self.dead = True
        
class inksac(object):
    def __init__(self):
        self.sprite = pygame.image.load('INKpot.png')
        self.rect = self.sprite.get_rect()
        self.x = randint(200,1000)
        self.y = randint(100,620)
        self.pos = self.x, self.y
        self.rect.x = self.x
        self.rect.y = self.y
    def refresh(self):
        
        if self.rect.colliderect(octopus.rect):
            return True
        return False
    def die(self):
        
        self.x = self.y = 4000
        self.pos = self.x, self.y   

class coin(object):
    def __init__(self):
        self.sprite = pygame.image.load('coin.png')
        self.rect = self.sprite.get_rect()
        self.x = randint(200,1000)
        self.y = randint(100,620)
        self.pos = self.x, self.y
        self.rect.x = self.x
        self.rect.y = self.y
    def refresh(self):
        
        if self.rect.colliderect(octopus.rect):
            return True
        return False
    def die(self):
        
        self.x = self.y = 4000
        self.pos = self.x, self.y   


def incrementtime(stopwatch):
    font = pygame.font.Font(None, 60)
    stopwatch['mils'] += 1000/60
    
    if stopwatch['mils'] >= 1000:
        stopwatch['mils'] = 0
        stopwatch['s'] += 1
        
    if stopwatch['s'] == 60:
        stopwatch['s'] = 0
        stopwatch['m'] += 1
    
    stopwatchdisplay = font.render('Current score: {0}:{1}.{2}'.format(stopwatch['m'], stopwatch['s'], stopwatch['mils']), 0, (255,255,255))
    
    octopus.score += 0.0167 
    return stopwatch

thehighscore = highscore()
octopus = player(pygame.image.load('8pi1.png')) #Initialising the player as the octopus variable. With the image '8pi1.png'
playerweapons = [] #Contains all of the shots that the player has fired
balltimer = 0 #Player firing limit

baddies = [] #Contains all of the enemies
baddieweapons = [] #Contains all of the shots that the enemy has fired.
baddietimer = 0 # Baddie spawn timer

INKsacs = [inksac()]
coins = [coin()]
balls = [playerweapons, baddieweapons]

#Game LOOP!!!!
#WHOOP WHOOP
while True:
    
    screen.blit(backdrop, (0,0))    #Draw the background at the bottom
    #Check if the close button has been pressed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
    #Get the keypresses.
    keypressed = pygame.key.get_pressed()
    
    #Turn Right
    if keypressed[pygame.K_d]:

        if octopus.angle == 0:

            octopus.angle = 360 - 5

        else:

            octopus.angle -= 5
        
        if octopus.speed >= 3.002:
                #Apply the speed penalty for turning
            octopus.speed -= 3.002
    
    #Turn Left
    if keypressed[pygame.K_a]:

        if octopus.angle == 360:

            octopus.angle = 0 + 5

        else:

            octopus.angle += 5

        if octopus.speed >= 3.002:
                #Speed penalty!!
            octopus.speed -= 3.002
    
    #Go forwards
    if keypressed[pygame.K_w]:

        octopus.move()

    #Fire but only if allowed.
    if keypressed[pygame.K_SPACE] and balltimer <= 0 and octopus.inkamount > 0:
        #Add new ball with sprite ink
        playerweapons.append(ball(octopus.angle, octopus.speed, octopus.rect, pygame.image.load('INK.png')))
        balltimer = 10
        octopus.inkamount -= 1
    balltimer -= 1
    #m8 5 seconds are up so spawn a new baddie!
    if baddietimer == 300:
                                # At a random location
        baddies.append(enemy(randint(0,1280), randint(0,720)))
        baddietimer = 0
    #Increment timer
    baddietimer += 1
        
    #Refresh all of the baddies.    
    for baddie in baddies:
        #Remember how if the baddie gets hit it returns false?
        if not baddie.refresh():
            
            baddies.remove(baddie)
        #Put the guy on the screen!
        screen.blit(baddie.sprite, (baddie.pos))
    


    #Refresh the player
    octopus.refresh()
    #Draw it
    screen.blit(octopus.sprite, (octopus.pos))

    #Finally move all of the balls.
    for balllist in balls:
        for bally in balllist:
                
            bally.move()
            screen.blit(bally.sprite, (bally.x, bally.y))
    
    for inksacy in INKsacs:
        
        
        
        if inksacy.refresh():
            
            octopus.inkamount += 5
            inksacy.die()
            INKsacs.remove(inksacy)
            INKsacs.append(inksac())
        screen.blit(inksacy.sprite, (inksacy.pos))
    
    for coiny in coins:
        
        if coiny.refresh():
            
            octopus.score += 10
            coiny.die()
            coins.remove(coiny)
            coins.append(coin())
        screen.blit(coiny.sprite, (coiny.pos))
    
    
    stopwatch = incrementtime(stopwatch)
    thehighscore.renderscore()
    #Show all of that to the user.
    pygame.display.flip()
    #Game is locked at 60fps
    
    
    clock.tick(60)
