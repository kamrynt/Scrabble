import pygame
from pygame.locals import *
pygame.init()

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1020

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creates the screen 
pygame.display.set_caption('BisonProductions')
board = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-",
         "-","-","-","-","-","-","-","-","-","-","-","-","-","-","-",
         "-","-","-","-","-","-","-","-","-","-","-","-","-","-","-",]
board_background = pygame.Rect((308, 82, 800, 800))
settings_bar = pygame.Rect((100,150,104,730))
letter_stand = pygame.Rect((353, 910, 744, 87))
score_board = pygame.Rect((1132,24,290,93))
buddy_background = pygame.Rect((1132,156,290,287))
buddy = pygame.Rect((1168,211,218,190))
scramble = pygame.Rect((283,941,51,51))
player = "X"
score = 0
gameRunning = True
active_letter = None
letters = []
for i in range(7):
    first_letter = 100
    x = 390
    y = 901 
    w = 80
    h = 80
    letter = pygame.Rect(x + first_letter * i, y, w, h)
    letters.append(letter)
clicked = False

run = True
while run:
    
    screen.fill((255,255,255))

    pygame.draw.rect(screen, (84, 52, 28), board_background)#draws on screen and the color
    pygame.draw.rect(screen,(84, 52, 28), letter_stand )
    pygame.draw.rect(screen, (187,58,58), settings_bar)
    pygame.draw.rect(screen, (187,58,58), score_board)
    pygame.draw.rect(screen,(5,78,131), buddy_background)
    pygame.draw.rect(screen,(242, 242, 242), buddy)
    pygame.draw.rect(screen,(5,78,131), scramble)

    for letter in letters:
        pygame.draw.rect(screen, (242, 242, 242), letter)
   #update and draw letters



    for event in pygame.event.get():
       
       if event.type == pygame.MOUSEBUTTONDOWN:
           if event.button == 1:
               for num, letter in enumerate(letters):
                   if letter.collidepoint(event.pos):
                       active_letter = num
       if event.type == pygame.MOUSEBUTTONUP:
           if event.button == 1:
              active_letter = None
                       
       if event.type == pygame.MOUSEMOTION:
           if active_letter != None:
                letters[active_letter].move_ip(event.rel)
                
    if event.type == pygame.QUIT:
        run = False
    pygame.display.update()
