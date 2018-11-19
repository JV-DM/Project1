import sys, pygame, random
from pygame.locals import *


# Window width and weight
WINDOW_WIDTH = 600
WINDOW_WEIGHT = 400
#
TEXTCOLOUR = (255,255,255)
BACKGROUND_COLOUR = (0, 0, 0)
#
FPS = 60
#

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: #QUIT WITH SCAPE KEY
                    terminate()
                return

def playerHasHitObject():
    for b in objects:
        if playerRect.colliderect(b['rect'])
            return True
    return False

def drawText(text,font, x, y):
    textobj = font.render(text,1 ,TEXTCOLOUR)
    textrect =textobj.get_rect()
    textrect.topleft =(x,y)
    surface.blit(textobj,textrect)

#start game,timer ,window and cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_model((WINDOW_WIDTH,WINDOW_WEIGHT))
pygame.display.set_caption("Dodger")
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(none,48)

#setup images
playerImg = pygame.image.load('')
playerRect = playerImage.get_rect()
objectImg = pygame.image.load('')

#START SCREEN

drawText('Carlos hijo de puta',font, windowSurface,(WINDOW_WIDTH/2), (WINDOW_WEIGHT/2))
drawText('Pulsa algo pa que vaya esta wea',font, windowSurface,(WINDOW_WIDTH/2)-50, (WINDOW_WEIGHT/2) -50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0

while True:
    objects = []
    score = 0
    playerRect.topleft = (WINDOW_WIDTH/2, WINDOW_WEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False

    while True:
        score += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == ord('+'):
                    reverseCheat = True

                if event.key == ord('-'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if even.key == K_RIGHT or event.key == ord('d'):
                    moveRight = True
                    moveLeft = False
                if even.key == K_UP or event.key == ord('w'):
                    moveUp = True
                    moveDown = False
                if event.key == K_DOWN or event.key == ord('s'):
