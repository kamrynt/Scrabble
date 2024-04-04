import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creates the screen 

player = pygame.Rect((308, 82, 800, 800))

run = True
while run:

    pygame.draw.rect(screen, ())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()