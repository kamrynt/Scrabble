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

# Add any additional settings you have here
letter_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}
