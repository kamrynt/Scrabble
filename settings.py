# settings.py
import pygame

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1020
BOARD_BACKGROUND_COLOR = (84, 52, 28)
LETTER_STAND_COLOR = (84, 52, 28)
SETTINGS_BAR_COLOR = (187, 58, 58)
SCORE_BOARD_COLOR = (187, 58, 58)
BUDDY_BACKGROUND_COLOR = (5, 78, 131)
BUDDY_COLOR = (242, 242, 242)
SCRAMBLE_COLOR = (5, 78, 131)
TILE_COLOR = (242, 242, 242)
BONUS_TILE_WIDTH = 20
BONUS_TILE_HEIGHT = 20
HIGHLIGHT_COLOR = (5, 78, 131)
BOARD_TOP_LEFT_X = 800  # Adjust this value based on your board's position
BOARD_TOP_LEFT_Y = 800  # Adjust this value based on your board's position
SPACE_WIDTH = 20       # Adjust this to match the width of your board spaces
SPACE_HEIGHT = 20      # Adjust this to match the height of your board spaces




# Define bonus tile positions and their corresponding multipliers
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

# Define the layout of the board with bonus tiles
board_layout = [
    ['TW', None, None, 'DL', None, None, None, 'TW', None, None, None, 'DL', None, None, 'TW'],
    [None, 'DW', None, None, None, 'TL', None, None, None, 'TL', None, None, None, 'DW', None],
    [None, None, 'DW', None, None, None, 'DL', None, 'DL', None, None, None, 'DW', None, None],
    ['DL', None, None, 'DW', None, None, None, 'DL', None, None, None, 'DW', None, None, 'DL'],
    [None, None, None, None, 'DW', None, None, None, None, None, 'DW', None, None, None, None],
    [None, 'TL', None, None, None, 'TL', None, None, None, 'TL', None, None, None, 'TL', None],
    [None, None, 'DL', None, None, None, 'DL', None, 'DL', None, None, None, 'DL', None, None],
    ['TW', None, None, 'DL', None, None, None, 'CL', None, None, None, 'DL', None, None, 'TW'],
    [None, None, 'DL', None, None, None, 'DL', None, 'DL', None, None, None, 'DL', None, None],
    [None, 'TL', None, None, None, 'TL', None, None, None, 'TL', None, None, None, 'TL', None],
    [None, None, None, None, 'DW', None, None, None, None, None, 'DW', None, None, None, None],
    ['DL', None, None, 'DW', None, None, None, 'DL', None, None, None, 'DW', None, None, 'DL'],
    [None, None, 'DW', None, None, None, 'DL', None, 'DL', None, None, None, 'DW', None, None],
    [None, 'DW', None, None, None, 'TL', None, None, None, 'TL', None, None, None, 'DW', None],
    ['TW', None, None, 'DL', None, None, None, 'TW', None, None, None, 'DL', None, None, 'TW'],
]

# 1 means normal score, 2 means double letter score, 3 means triple letter score, etc.
multiplier_layout = [
    [3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 3],
    [1, 2, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 2, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 3],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [1, 2, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3],
    # Continue filling out the matrix according to your board's layout
]

def get_multipliers(row, col):
    tile_multiplier = 1
    word_multiplier = 1

    bonus_type = board_layout[row][col]
    if bonus_type == "DL":
        tile_multiplier = 2
    elif bonus_type == "TL":
        tile_multiplier = 3
    elif bonus_type == "DW":
        word_multiplier = 2
    elif bonus_type == "TW":
        word_multiplier = 3

    return tile_multiplier, word_multiplier


# Add any additional settings you have here
letter_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}
