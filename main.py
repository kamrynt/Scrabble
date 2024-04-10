import pygame
pygame.init()

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1020

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creates the screen 
pygame.display.set_caption('BisonProductions')
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
occupied_spaces = []
spaces = []
for i in range(15):
    for j in range(15):
        space = pygame.Rect(340 + 50 * i, 120 + 50 * j, 40, 40)
        spaces.append(space)
letters = []
for i in range(7):
    first_letter = 100
    x = 390
    y = 901 
    w = 40
    h = 40
    letter = pygame.Rect(x + first_letter * i, y, w, h)
    letters.append(letter)
clicked = False
bag = []
a = 1
b = 3
c = 3

def adjacent_spaces(space_rect):
    adjacent = []
    for delta in [(0, -40), (0, 40), (-40, 0), (40, 0)]:
        adjacent_rect = space_rect.move(delta)
        if adjacent_rect.collidelist(spaces) != -1:
            adjacent.append(adjacent_rect)
    return adjacent

initial_tile_positions = [letter.topleft for letter in letters]

def is_valid_move(space_rect):
    # Check if the space is empty
    if space_rect not in occupied_spaces:
        # Check if the space is adjacent to an existing tile on the board
        adjacent = False
        for adjacent_space in adjacent_spaces(space_rect):
            if adjacent_space in occupied_spaces:
                adjacent = True
                break
        if adjacent:
            return True
    return False

def move_tile(active_letter, space_rect):
    # Move the tile to the board position
    letter = letters.pop(active_letter)
    letter.topleft = space_rect.topleft
    occupied_spaces.append(space_rect)
    # Replenish the rack with a new tile
    new_letter = pygame.Rect(390 + 100 * (len(letters) + 1), 901, 20, 20)
    letters.append(new_letter)

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

    for space in spaces:
        pygame.draw.rect(screen, (242,242,242), space)
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
                for space in spaces:
                    if space.collidepoint(event.pos):
                        # Place the tile on the board if the position is valid
                        if is_valid_move(space):
                            move_tile(active_letter, space)
                            active_letter = None
                            break
                else:
                    # If the release is not on a valid board position, return the tile to its original position
                    if active_letter is not None:
                        letters[active_letter].topleft = initial_tile_positions[active_letter]
                        active_letter = None


                       
       if event.type == pygame.MOUSEMOTION:
           if active_letter != None:
                letters[active_letter].move_ip(event.rel)
                
    if event.type == pygame.QUIT:
        run = False
    pygame.display.update()
