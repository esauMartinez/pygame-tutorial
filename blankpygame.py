import sys
import pygame
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('HELLO WORLD')


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
    spamRect = pygame.Rect(10, 20, 200, 300)
    
    