import pygame
from menu_new import Menu
import sys


pygame.init()
display = pygame.display.set_mode((800,600),pygame.RESIZABLE)
clock = pygame.time.Clock()
menu = Menu()
screen = None
startGame = False
while True:
    w = display.get_width()
    h = display.get_height()
    if not startGame:
        menu.update()
        screen = menu.screen
    else:
        screen = pygame.surface.Surface((100,100))
        screen.fill(pygame.Color("Black"))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         test = not test
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode(event.size, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)    
        if not startGame:
            startGame = menu.eventHandler(event,w,h)
        else:
            menu = None

    display.blit(pygame.transform.scale(screen,display.get_rect().size),(0,0))


    pygame.display.flip()
    clock.tick(60)

