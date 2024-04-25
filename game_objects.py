# game_objects.py

import pygame
import os
from resources import load_tile_images, load_bonus_tile_images
from settings import bonus_tiles, board_layout, get_multipliers, SPACE_WIDTH, SPACE_HEIGHT, BOARD_TOP_LEFT_X, BOARD_TOP_LEFT_Y,letter_scores
from utils import calculate_tile_score, apply_bonus, calculate_word_score, get_word_tiles, update_player_score


class LetterTile:
    def __init__(self, letter, rect, image=None):
        from utils import calculate_tile_score
        self.letter = letter
        self.rect = rect
        self.image = pygame.image.load(os.path.join('images', f'{letter}_tile.png'))

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class Board:
    def __init__(self):
        self.current_score = 0
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
        self.top_left_x = 340
        self.top_left_y = 120 
        self.space_width = 50 
        self.space_height = 50  
        self.board_state = [[None for _ in range(15)] for _ in range(15)]

        for i in range(15):  # Assuming a 15x15 board
            for j in range(15):
                space = pygame.Rect(340 + 50 * i, 120 + 50 * j, 40, 40)
                self.spaces.append(space)

    def place_tile(self, active_letter, row, col):
        if 0 <= row < 15 and 0 <= col < 15:  # Ensure row and col are within bounds
            self.board_state[row][col] = active_letter
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

def is_valid_move(row, col, board):
    # Example check: Ensure the position is within the board limits and is empty
    if 0 <= row < len(board.board_state) and 0 <= col < len(board.board_state[0]):
        return board.board_state[row][col] is None
    return False



def update_score(board, row, col, letter):
    # Example: Simple scoring, adjust as needed for your game rules
    base_score = letter_scores[letter]
    if hasattr(board, 'current_score'):
        board.current_score += base_score
    else:
        board.current_score = base_score

def check_game_end_conditions(board):
    # Example condition: Check if the board is full
    if all(cell is not None for row in board.board_state for cell in row):
        print("Game Over: Board is full")
        return True
    return False


def move_tile(letter_tiles, active_letter, row, col, board):
    # Assume 'board' has attributes for managing state and a method for checking valid placements
    if not is_valid_move(row, col, board):
        print("Move is not valid.")
        return False

    tile = letter_tiles[active_letter]
    # Calculate pixel positions for rendering
    new_x = board.top_left_x + col * board.space_width
    new_y = board.top_left_y + row * board.space_height
    tile.rect.x = new_x
    tile.rect.y = new_y

    # Update the board state
    if 0 <= row < len(board.board_state) and 0 <= col < len(board.board_state[row]):
        board.board_state[row][col] = tile.letter
        print(f"Tile {tile.letter} placed at ({row}, {col}).")

        # Update scoring (not detailed here, depends on your scoring system)
        update_score(board, row, col, tile.letter)

        # Additional game state updates
        check_game_end_conditions(board)

        return True
    else:
        print("Position out of board range.")
        return False
    
def get_placed_word(board):
    # Assuming board.board_state is a list of lists where each tile can be None or an instance of LetterTile
    word = ""
    for row in board.board_state:
        for tile in row:
            if tile is not None:
                word += tile.letter  # Assuming each tile has a 'letter' attribute
    return word




 





