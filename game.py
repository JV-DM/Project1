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
ADDNEWOBJECTRATE = 10
MAX_SIZE = 40
MIN_SIZE = 10

OBJECT_MAX_SPEED = 7
OBJECT_MIN_SPEED = 1
PLAYERMOVERATE = 50

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: #QUIT WITH SCAPE KEY
                    terminate()
                return

def playerHasHitObject(playerRect,objects):
    for b in objects:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text,font, x, y):
    textobj = font.render(text,1 ,TEXTCOLOUR)
    textrect =textobj.get_rect()
    textrect.topleft =(x,y)
    windowSurface.blit(textobj,textrect)

#start game,timer ,window and cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_WEIGHT))
pygame.display.set_caption("Dodger")
pygame.mouse.set_visible(False)

font =  pygame.font.SysFont('helvetica',15)

#setup images
playerImg = pygame.image.load('player.png')
playerRect = playerImg.get_rect()
objectImg = pygame.image.load('object.png')

#START SCREEN

drawText('Carlos hijo de puta',font, (WINDOW_WIDTH/2), (WINDOW_WEIGHT/2))
drawText('Pulsa algo pa que vaya esta wea',font, (WINDOW_WIDTH/2)-50, (WINDOW_WEIGHT/2) -50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0

while True:
    objects = []
    score = 0
    playerRect.topleft = (WINDOW_WIDTH/2, WINDOW_WEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    objectAddCounter = 0

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
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = True
                    moveLeft = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = True
                    moveDown = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUP = False
                    moveDown = True

        if not reverseCheat and not slowCheat:
            objectAddCounter += 1
        if objectAddCounter == ADDNEWOBJECTRATE:
            objectAddCounter = 0
            objectSize = random.randint(MIN_SIZE, MAX_SIZE)
            newObject = {'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH-objectSize), 0 - objectSize, objectSize, objectSize),
                         'speed': random.randint(OBJECT_MIN_SPEED, OBJECT_MAX_SPEED),
                         'surface':pygame.transform.scale(objectImg, (objectSize, objectSize)),
                         }
            objects.append(newObject)

        if moveRight and playerRect.right < WINDOW_WIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1* PLAYERMOVERATE,0)
        if moveUp and playerRect.top < 0:
            playerRect.move_ip(0,PLAYERMOVERATE)
        if moveDown and playerRect.botton < WINDOW_WEIGHT:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)

        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        for b in objects:
                if not reverseCheat and not slowCheat:
                    b['rect'].move_ip(0,b['speed'])
                if reverseCheat:
                    b['rect'].move_ip(0,5)
                if slowCheat:
                    b['rect'].move_ip(0,1)
#DELETE OBJECTS THAT HAD FALL OVER THE LIMITS
        for b in objects[:]:
            if b['rect'].top > WINDOW_WEIGHT:
                objects.remove(b)

        windowSurface.fill(BACKGROUND_COLOUR)

        drawText('Score: %s' % (score), font, 10, 0)
        drawText('Top Score: %s' % (topScore), font, 10, 40)

        windowSurface.blit(playerImg, playerRect)

        for b in objects:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        if playerHasHitObject(playerRect,objects):
            if score > topScore:
                topScore = score
            break

        mainClock.tick(FPS)

        drawText('Game Over putos',font, (WINDOW_WIDTH/2), (WINDOW_WEIGHT/2))
        drawText('Pulsa algo pa intentar otra vez puto malo',font, (WINDOW_WIDTH/2)-50,(WINDOW_WEIGHT/2))
        pygame.display.update()
        waitForPlayerToPressKey()
