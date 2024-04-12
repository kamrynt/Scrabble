# game_objects.py

import pygame
import os
from resources import load_tile_images, load_bonus_tile_images
from settings import bonus_tiles, board_layout, get_multipliers, SPACE_WIDTH, SPACE_HEIGHT, BOARD_TOP_LEFT_X, BOARD_TOP_LEFT_Y
from utils import calculate_tile_score, apply_bonus, calculate_word_score, get_word_tiles, update_player_score


class LetterTile:
    def __init__(self, letter, rect, image=None):
        self.letter = letter
        self.rect = rect
        self.image = pygame.image.load(os.path.join('images', f'{letter}_tile.png'))
        

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class Board:
    def __init__(self):
        self.active_letter = None
        self.occupied_spaces = []
        self.board_background = pygame.Rect(308, 82, 800, 800)
        self.spaces = []
        self.settings_bar = pygame.Rect((100,150,104,730))
        self.letter_stand = pygame.Rect((353, 910, 744, 87))
        self.score_board = pygame.Rect((1132,24,290,93))
        self.buddy_background = pygame.Rect((1132,156,290,287))
        self.buddy = pygame.Rect((1168,211,218,190))
        self.scramble = pygame.Rect((283,941,51,51))
        # Initialize other board-related attributes
        self.letters = []  # Assuming this is where you initialize LetterTiles
        self.top_left_x = 800  # Example value, adjust as needed
        self.top_left_y = 800  # Example value, adjust as needed
        self.space_width = 20  # Example value, adjust as needed
        self.space_height = 20  # Example value, adjust as needed
        self.board_state = [[None for _ in range(15)] for _ in range(15)]

        for i in range(15):  # Assuming a 15x15 board
            for j in range(15):
                space = pygame.Rect(340 + 50 * i, 120 + 50 * j, 40, 40)
                self.spaces.append(space)

    def place_tile(self, letter, row, col):
        if 0 <= row < 15 and 0 <= col < 15:  # Ensure row and col are within bounds
            self.board_state[row][col] = letter
            return True
        return False
     

board = Board() 
    
    # Board-related methods...

def initialize_game():
    global letter_tiles  # Declare as global if you plan to modify it outside this function
    letter_tiles = []
    # Further initialization logic, such as adding LetterTile instances to letter_tiles



def adjacent_spaces(space_rect):
    adjacent = []
    for delta in [(0, -40), (0, 40), (-40, 0), (40, 0)]:
        adjacent_rect = space_rect.move(delta)
        if adjacent_rect.collidelist(board.spaces) != -1:
            adjacent.append(adjacent_rect)
    return adjacent

def is_valid_move(row, col):
    # Example condition to check if a space is occupied
    if board.board_state[row][col] is None:
        # Further checks for adjacency or other game rules can be added here
        return True
    return False



def move_tile(letter_tiles, active_letter, row, col, board):
    if 0 <= active_letter < len(letter_tiles):
        tile = letter_tiles[active_letter]
        letter = tile.letter  # Get the letter directly from the tile object

        # Calculate the position of the tile based on row and col
        space_rect = pygame.Rect(col * SPACE_WIDTH + BOARD_TOP_LEFT_X, row * SPACE_HEIGHT + BOARD_TOP_LEFT_Y, SPACE_WIDTH, SPACE_HEIGHT)

        # Get the multipliers for the tile's new position
        tile_multiplier, word_multiplier = get_multipliers(row, col)

        # Calculate the score for the individual tile
        tile_score = calculate_tile_score(letter, tile_multiplier)

        # Calculate the score for the entire word involving the new tile
        word_tiles = get_word_tiles(row, col, board)  # Fetch all tiles forming the word
        word_score = 0
        for word_tile in word_tiles:
            # Calculate score for each tile in the word
            tile_multiplier, _ = get_multipliers(word_tile.row, word_tile.col)
            word_score += calculate_tile_score(word_tile.letter, tile_multiplier)

        # Apply word multiplier to the total word score
        final_word_score = apply_bonus(word_score, word_multiplier, space_rect)

        # Update the game state and player's score
        update_player_score(final_word_score)  # Ensure this function updates global or player-specific score

    else:
        print("Error: Active letter index is out of range.")


 





