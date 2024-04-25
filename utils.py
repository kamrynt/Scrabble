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
    word_horizontal = ''
    tiles_horizontal = []

    # Check horizontally for connected tiles
    start_col = col
    while start_col > 0 and board.board_state[row][start_col - 1] is not None:
        start_col -= 1
    end_col = col
    while end_col < len(board.board_state[row]) - 1 and board.board_state[row][end_col + 1] is not None:
        end_col += 1

    if end_col != start_col:
        word_horizontal += ''.join(board.board_state[row][i].letter for i in range(start_col, end_col + 1))
        tiles_horizontal.extend([(row, i) for i in range(start_col, end_col + 1)])

    # Check vertically for connected tiles
    word_vertical = ''
    tiles_vertical = []
    start_row = row
    while start_row > 0 and board.board_state[start_row - 1][col] is not None:
        start_row -= 1
    end_row = row
    while end_row < len(board.board_state) - 1 and board.board_state[end_row + 1][col] is not None:
        end_row += 1

    if end_row != start_row:
        word_vertical += ''.join(board.board_state[i][col].letter for i in range(start_row, end_row + 1))
        tiles_vertical.extend([(i, col) for i in range(start_row, end_row + 1)])

    # Return results as a dictionary or two separate words and their tiles
    return {
        'horizontal': {'word': word_horizontal, 'tiles': tiles_horizontal},
        'vertical': {'word': word_vertical, 'tiles': tiles_vertical}
    }




def calculate_word_score(board):
    total_score = 0
    word_multiplier = 1  # Initialize with a default value that does not affect multiplication

    # Example: Assuming you're calculating based on tiles already placed on the board
    for row in range(len(board.board_state)):
        for col in range(len(board.board_state[row])):
            tile = board.board_state[row][col]
            if tile is not None:  # Ensure there is a tile
                letter = tile.letter
                tile_multiplier, potential_word_multiplier = get_multipliers(row, col)
                letter_score = letter_scores[letter] * tile_multiplier
                total_score += letter_score
                # Check if this tile's position affects the word multiplier
                if potential_word_multiplier > word_multiplier:
                    word_multiplier = potential_word_multiplier  # Update to the higher multiplier if applicable

    # Apply the highest word multiplier found (if any) to the total score
    total_score *= word_multiplier
    return total_score


def find_position_of_letter(board, letter):
    # Implement a way to find the position of each letter, this is just a placeholder
    for row in range(len(board.board_state)):
        for col in range(len(board.board_state[row])):
            if board.board_state[row][col] == letter:
                return row, col
    return None, None


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
