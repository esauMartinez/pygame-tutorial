import pygame, sys
from pygame.locals import *
import time

pygame.init()

DISPLAYSURF = pygame.display.set_mode((600, 400))

pygame.display.set_caption('hello world')

WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('JOSE ESAU MARTINEZ CONTRERAS', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (300, 200)

soundObj = pygame.mixer.Sound('beeps.wav')
soundObj.play(-1) # parameter -1 is foor loop sound an you can decide if you want
                # to start te sound in a specific time
time.sleep(3) # wait and let the sound play for 1 second
soundObj.stop()


while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()        
    

