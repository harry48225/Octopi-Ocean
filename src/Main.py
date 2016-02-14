import pygame
from pygame.locals import *

screen = pygame.display.set_mode((1280,720))

octopus = pygame.image.load('8pi.png').convert()

screen.blit(pygame.image.load('8pi.png').convert(), (100,10))

raw_input()