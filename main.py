import pygame
pygame.init()
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, board_layout, HIGHLIGHT_COLOR
from game_objects import LetterTile, Board, is_valid_move, move_tile, get_placed_word
from utils import calculate_tile_score, calculate_word_score, get_random_letters, update_player_score
from resources import load_tile_images, load_bonus_tile_images, letter_images



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creates the screen 
pygame.display.set_caption('BisonProductions')

player_score = 0  # Starting score
letter_tiles = []
for letter in get_random_letters():
    # Assuming get_random_letters() returns a list of letters you want to use
    rect = pygame.Rect(0, 0, 20, 20)  # Placeholder; set your desired position and size
    image = letter_images[letter]  # Assuming letter_images is a dict mapping letters to their images
    letter_tiles.append(LetterTile(letter, rect, image))
letters = get_random_letters()
board = Board()

def draw_button(screen, text_surface,text_rect, color):
        pygame.draw.rect(screen,(5,78,131), board.scramble)
        screen.blit(text_surface, text_rect)
gameRunning = True
clock = pygame.time.Clock()
tile_images = load_tile_images()
bonus_tile_images = load_bonus_tile_images()


text_color = (255, 255, 255)  # White text
hover_color = (255, 100, 100)  # Light red for hover effect

font = pygame.font.Font(None, 20)
text = "Done"
text_surface = font.render(text, True, text_color)
text_rect = text_surface.get_rect(center=board.scramble.center)

hovered_space = None 
active_letter = None
occupied_spaces = []
spaces = []
word = []
for i in range(15):
    for j in range(15):
        space = pygame.Rect(340 + 50 * i, 120 + 50 * j, 40, 40)
        spaces.append(space)

# Define the list of letter tiles
       


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
    draw_button(screen, text_surface, text_rect, board.scramble)
    

    if hovered_space is not None:
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, hovered_space, 5)  # Draws a highlight border; adjust thickness as needed


    # Scale images if they are not the correct size
    for key, image in bonus_tile_images.items():
        bonus_tile_images[key] = pygame.transform.scale(image, (40, 40))  # Scale to 40x40 pixels or whatever size your tiles are


    # Draw spaces
    for space in spaces:
        pygame.draw.rect(screen, (242,242,242), space)
        
    

    # Draw bonus tiles
    for row_index, row in enumerate(board_layout):
        for col_index, bonus_type in enumerate(row):
            if bonus_type:
                # Calculate position based on bonus tile size
                x = 340 + 50 * col_index 
                y = 120 + 50 * row_index
                bonus_image = bonus_tile_images[bonus_type]
                screen.blit(bonus_image, (x, y))

    

    # Draw letter tiles
    for tile in letter_tiles:
        screen.blit(tile.image, tile.rect)
        #letter_image = letter_images[tile.letter]
        #screen.blit(letter_image, tile.rect.topleft)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for idx, tile in enumerate(letter_tiles):
                    if tile.rect.collidepoint(event.pos):
                        active_letter = idx
                        offset_x = tile.rect.x - event.pos[0]
                        offset_y = tile.rect.y - event.pos[1]
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and active_letter is not None:
                placed = False
                for space in spaces:
                    if space.collidepoint(event.pos):
                        # Correct calculation of row and column
                        col = (space.x - board.top_left_x) // board.space_width
                        row = (space.y - board.top_left_y) // board.space_height
                        print("Board top left:", board.top_left_x, board.top_left_y)
                        print("Space position:", space.x, space.y)
                        print("Calculated row:", row, "Calculated col:", col)
                        if is_valid_move(row, col, board):
                            if board.place_tile(letter_tiles[active_letter], row, col):
                                new_x = board.top_left_x + col * board.space_width
                                new_y = board.top_left_y + row * board.space_height
                                letter_tiles[active_letter].rect.topleft = (new_x, new_y)
                                print("Resizing tile image to 20x20")
                                letter_tiles[active_letter].rect.size = (40, 40)
                                letter_tiles[active_letter].image = pygame.transform.scale(letter_tiles[active_letter].image, (40, 40))

                                placed = True
                                print("Valid move placed")

                                word.append(letter_tiles[active_letter])
                                break
                if not placed:
                    # Return the tile to its original position
                    letter_tiles[active_letter].rect.topleft = initial_tile_positions[active_letter]
                    active_letter = None
                    print("Invalid move, tile reset")

                active_letter = None
   

        elif event.type == pygame.MOUSEMOTION and active_letter is not None:
            # Move the tile with the mouse
            mouse_x, mouse_y = event.pos
            letter_tiles[active_letter].rect.x = mouse_x + offset_x
            letter_tiles[active_letter].rect.y = mouse_y + offset_y
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                if board.scramble.collidepoint(mouse_pos):
                    placed_word = get_placed_word(board)

                    word_score = calculate_word_score(board)
                    print(f"Word: {placed_word}, Score: {word_score}")
                    
                
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
