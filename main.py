import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, board_layout
from game_objects import LetterTile, Board, is_valid_move, move_tile
from utils import calculate_tile_score, calculate_word_score, get_random_letters
from resources import load_tile_images, load_bonus_tile_images, letter_images

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creates the screen 
pygame.display.set_caption('BisonProductions')

board = Board()
gameRunning = True
clock = pygame.time.Clock()
tile_images = load_tile_images()
bonus_tile_images = load_bonus_tile_images()



active_letter = None
occupied_spaces = []
spaces = []
for i in range(15):
    for j in range(15):
        space = pygame.Rect(340 + 50 * i, 120 + 50 * j, 40, 40)
        spaces.append(space)

# Define the list of letter tiles
       
letters = get_random_letters()
letter_tiles = []
for i, letter in enumerate(letters):
    x = board.letter_stand.x + i * (board.letter_stand.width / 7)
    y = board.letter_stand.y
    letter_tiles.append(LetterTile(letter, pygame.Rect(x, y, 40, 40), letter_images[letter]))
#for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#    rect = pygame.Rect(390 + 100 * i, 901, 40, 40)  # Adjust size and position as needed
 #   letters.append(LetterTile(letter, rect))    


clicked = False
initial_tile_positions = [tile.rect.topleft for tile in letter_tiles]



run = True
while run:
    
    screen.fill((255,255,255))

        # Draw other elements
    pygame.draw.rect(screen, (84, 52, 28), board.board_background)#draws on screen and the color
    pygame.draw.rect(screen,(84, 52, 28), board.letter_stand )
    pygame.draw.rect(screen, (187,58,58), board.settings_bar)
    pygame.draw.rect(screen, (187,58,58), board.score_board)
    pygame.draw.rect(screen,(5,78,131), board.buddy_background)
    pygame.draw.rect(screen,(242, 242, 242), board.buddy)
    pygame.draw.rect(screen,(5,78,131), board.scramble)

    # Scale images if they are not the correct size
    for key, image in bonus_tile_images.items():
        bonus_tile_images[key] = pygame.transform.scale(image, (40, 40))  # Scale to 40x40 pixels or whatever size your tiles are


    # Draw spaces
    for space in spaces:
        pygame.draw.rect(screen, (242,242,242), space)
        
    # Draw letter tiles
    for tile in letter_tiles:
        letter_image = letter_images[tile.letter]
        screen.blit(letter_image, tile.rect.topleft)

    # Draw bonus tiles
    for row_index, row in enumerate(board_layout):
        for col_index, bonus_type in enumerate(row):
            if bonus_type:
                # Calculate position based on bonus tile size
                x = 340 + 50 * col_index 
                y = 120 + 50 * row_index
                bonus_image = bonus_tile_images[bonus_type]
                screen.blit(bonus_image, (x, y))



    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, tile in enumerate(letter_tiles):  # Use 'letter_tiles', which should be a list of LetterTile objects.
                    if letter.rect.collidepoint(event.pos):
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
