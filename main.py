import pygame
pygame.init()

# Define a custom class to represent each letter tile
class LetterTile:
    def __init__(self, letter, rect):
        self.letter = letter
        self.rect = rect

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

 # Define the list of letter tiles       
letters = []
for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    rect = pygame.Rect(390 + 100 * i, 901, 40, 40)  # Adjust size and position as needed
    letters.append(LetterTile(letter, rect))
#for i in range(7):
#   x = 390
 #   y = 901 
  #  w = 40
   # h = 40
    #letter = pygame.Rect(x + first_letter * i, y, w, h)
    #letters.append(letter)
clicked = False

letter_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

def calculate_tile_score(letter_rect):
    # Assuming the letter is represented as a single character string
    letter = letter_rect.symbol # Change this line according to your implementation
    return letter_scores.get(letter.upper(), 0)

def update_player_score(score):
    global player_score  # Assuming player_score is a global variable representing the player's score
    player_score += score

def adjacent_spaces(space_rect):
    adjacent = []
    for delta in [(0, -40), (0, 40), (-40, 0), (40, 0)]:
        adjacent_rect = space_rect.move(delta)
        if adjacent_rect.collidelist(spaces) != -1:
            adjacent.append(adjacent_rect)
    return adjacent

# Store initial positions of letter tiles
initial_tile_positions = [letter.rect.topleft for letter in letters]

BONUS_TILE_WIDTH = 20
BONUS_TILE_HEIGHT = 20

# Load tile images for letters
tile_images = {}
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    tile_images[letter] = pygame.image.load(f'images/{letter}_tile.png')

# Define bonus tile positions and their corresponding multipliers
bonus_tiles = {
    (3, 0): 'TW',  # Triple Word Score
    (0, 0): 'TW',
    (7, 0): 'TW',
    (0, 3): 'TW',
    (14, 0): 'TW',
    (11, 0): 'TW',
    (3, 3): 'DW',  # Double Word Score
}

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

def apply_bonus(tile, space_rect):
    x = space_rect.left
    y = space_rect.top
    for position, bonus in bonus_tiles.items():
        if position == (x, y):
            if bonus == 'TW':
                return tile * 3  # Triple Word Score
            elif bonus == 'DW':
                return tile * 2  # Double Word Score
    return tile

def move_tile(active_letter, space_rect):
    # Move the tile to the board position
    letter = letters.pop(active_letter)
    letter.topleft = space_rect.topleft
    occupied_spaces.append(space_rect)
    # Apply bonus if applicable
    tile_score = calculate_tile_score(letter)  # Implement this function based on your scoring system
    tile_score = apply_bonus(tile_score, space_rect)
    update_player_score(tile_score)  # Implement this function to update the player's score
    # Replenish the rack with a new tile
    new_letter = pygame.Rect(390 + 100 * (len(letters) + 1), 901, 20, 20)
    letters.append(new_letter)

# Load letter tile images
letter_images = {}
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    letter_images[letter] = pygame.image.load(f'images/{letter}_tile.png')

# Load bonus tile images
bonus_images = {
    'TW': pygame.image.load('images/TW_tile.png'),
    'DW': pygame.image.load('images/DW_tile.png'),
    'TL': pygame.image.load('images/TL_tile.png'),
    'DL': pygame.image.load('images/DL_tile.png'),
}
board_layout = [
    ['TW', None, None, 'DL', None, None, None, 'TW', None, None, None, 'DL', None, None, 'TW'],
]

run = True
while run:
    
    screen.fill((255,255,255))

     # Draw game elements

    for row_index, row in enumerate(board_layout):
        for col_index, bonus_type in enumerate(row):
            if bonus_type:
                # Calculate position based on bonus tile size
                x = col_index * BONUS_TILE_WIDTH
                y = row_index * BONUS_TILE_HEIGHT
                bonus_image = bonus_images[bonus_type]
                screen.blit(bonus_image, (x, y))
    # Draw letter tiles, assuming letters is a list of Tile objects as defined previously
    for tile in letters:
        letter_image = letter_images[tile.letter]
        screen.blit(letter_image, tile.rect.topleft)

    for i, letter in enumerate(letters):
        # Assuming letters contain letter symbols ('A', 'B', etc.)
        tile_image = tile_images.get(letter.letter, None)
        if tile_image:
            screen.blit(tile_image, (390 + 100 * i, 901))  # Draw tile image at appropriate position
        else:
            # Draw a placeholder rectangle if no tile image is found
            pygame.draw.rect(screen, (242, 242, 242), letter)

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
               for num, letter_rect in enumerate(letters):
                   if letter_rect.collidepoint(event.pos):
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
