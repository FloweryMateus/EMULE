import pygame, sys, math, time
from itertools import cycle
from pygame.locals import *
from pong import *
from main import *
BLINK_EVENT = pygame.USEREVENT + 0 

### DEFINIÇÃO DAS VARIÁVEIS CONTENDO AS IMAGENS
Opening = pygame.image.load('Assets/Others/Opening.png')
Menu = pygame.image.load('Assets/Others/Menu.png')



Clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('EMULE')
pygame.display.set_icon(pygame.image.load('Assets/Others/Icon.png'))
DISPLAY = pygame.display.set_mode((400, 450))
 
 
def opening():
    ### ANIMAÇÃO DO ELEMENTO DO MENU 'OPENING'
    onOpeningElement = pygame.image.load('Assets/Others/OpeningElement.png')
    blinkRect = onOpeningElement.get_rect()
    offOpeningElement = pygame.Surface(blinkRect.size)
    offOpeningElement.fill((0, 0, 0))
    blinkSurfaces = cycle([onOpeningElement, offOpeningElement])
    blinkSurface = next(blinkSurfaces)
    pygame.time.set_timer(BLINK_EVENT, 1000)

    DISPLAY.blit(Opening, (0, 0))



    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    menu()
            if event.type == BLINK_EVENT:
                blinkSurface = next(blinkSurfaces)

            DISPLAY.blit(blinkSurface, (78, 423))
        


    
 
        pygame.display.update()
        Clock.tick(60)

def menu():

    while True:
        DISPLAY.blit(Menu, (0, 0))

        rect = pygame.Rect(133, 255, 132, 36)
        mouse = pygame.mouse.get_pos()
        mouseOnRect = rect.collidepoint(mouse)
        if mouseOnRect == True:
            Jogo = Pong()
            Jogo.executar()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            


        
        pygame.display.update()
        Clock.tick(60)

opening()