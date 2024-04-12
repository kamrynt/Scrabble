# utils.py

# Assuming letter_scores are defined in settings.py or another appropriate placehi
from settings import letter_scores, board_layout
# Add any additional game object classes here
import random

def get_random_letters(number=7):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_tiles = []
    return random.sample(letters, number)

def calculate_tile_score(letter, tile_multiplier):
    # Dictionary of letter scores as in Scrabble or similar games
    letter_scores = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4,
        'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
        'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
        'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
        'Y': 4, 'Z': 10
    }

    # Compute the score based on the letter value
    base_score = letter_scores.get(letter.upper(), 0)
    # Multiply the base score by the tile multiplier
    return base_score * tile_multiplier

def get_multipliers(row, col):
    # Assuming board_layout is defined in your settings and accessible here
    # and that it is structured as a 2D list where each cell contains a string indicating the bonus type
    tile_multiplier = 1
    word_multiplier = 1

    # Access the bonus type from the board layout using the row and col values
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


def get_word_tiles(row, col, board):
    word_tiles = []
    
    # Horizontal tiles
    # Start from the current tile and expand left and right
    start = col
    while start > 0 and board.board_state[row][start - 1] is not None:
        start -= 1
    end = col
    while end < len(board.board_state[row]) - 1 and board.board_state[row][end + 1] is not None:
        end += 1
    
    if end != start:  # Ensure there's actually a word here
        word_tiles.extend([board.board_state[row][i] for i in range(start, end + 1)])

    # Vertical tiles
    # Start from the current tile and expand up and down
    start = row
    while start > 0 and board.board_state[start - 1][col] is not None:
        start -= 1
    end = row
    while end < len(board.board_state) - 1 and board.board_state[end + 1][col] is not None:
        end += 1
    
    if end != start:  # Ensure there's actually a word here
        word_tiles.extend([board.board_state[i][col] for i in range(start, end + 1)])

    return word_tiles




def calculate_word_score(row, col, board, word_multiplier):
    # This should retrieve all tiles forming a word given the placement at row, col
    word_tiles = get_word_tiles(row, col, board)  # Make sure this function returns a list of tiles

    word_score = 0
    for tile in word_tiles:
        tile_multiplier, _ = get_multipliers(tile.row, tile.col)
        word_score += calculate_tile_score(tile.letter, tile_multiplier)
    
    return word_score * word_multiplier


def apply_bonus(tile_score, word_multiplier, space_rect):
    x = (space_rect.left - 340) // 50
    y = (space_rect.top - 120) // 50
    bonus_type = board_layout[y][x] if (0 <= y < len(board_layout) and 0 <= x < len(board_layout[0])) else None

    if bonus_type in ('DL', 'TL'):
        letter_multiplier = 3 if bonus_type == 'TL' else 2
        tile_score *= letter_multiplier
    elif bonus_type in ('DW', 'TW'):
        word_multiplier *= 3 if bonus_type == 'TW' else 2

    return tile_score * word_multiplier  # Return the final score after applying both bonuses

def update_player_score(score_to_add):
    global player_score
    player_score += score_to_add
