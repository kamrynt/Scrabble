# utils.py

# Assuming letter_scores are defined in settings.py or another appropriate placehi
from settings import letter_scores, board_layout
# Add any additional game object classes here
import random

def get_random_letters(number=7):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_tiles = []
    return random.sample(letters, number)

def calculate_tile_score(letter, multiplier):
   #Calculates the score for a single letter placed on a board tile.
   base_score = letter_scores[letter]
   return base_score * multiplier



def calculate_word_score(word, tiles):
   #Calculates the score for a whole word and updates the multipliers for bonus tiles.
    word_score = 0
    word_multiplier = 1
    
    for letter, tile in zip(word, tiles):
        tile_score = calculate_tile_score(letter, 1)  # Start with no multiplier
        tile_score, word_multiplier = apply_bonus(tile_score, tile, word_multiplier)
        word_score += tile_score
    
    word_score *= word_multiplier
    return word_score

def apply_bonus(tile_score, space_rect, word_multiplier):
    #Applies bonus multipliers from special board tiles to the tile score.
    x = (space_rect.left - 340) // 50  # Adjust if your grid starts elsewhere or cells have different sizes
    y = (space_rect.top - 120) // 50
    # Retrieve the bonus type for this position, if any
    bonus_type = board_layout[y][x] if (0 <= y < len(board_layout) and 0 <= x < len(board_layout[0])) else None
    
    if bonus_type in ('DL', 'TL'):
        # Double or triple letter score
        letter_multiplier = 3 if bonus_type == 'TL' else 2
        tile_score *= letter_multiplier
    elif bonus_type in ('DW', 'TW'):
        # Double or triple word score
        word_multiplier *= 3 if bonus_type == 'TW' else 2

    return tile_score, word_multiplier