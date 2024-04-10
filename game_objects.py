# game_objects.py

import pygame
import os
from resources import load_tile_images, load_bonus_tile_images
from settings import bonus_tiles, board_layout
from utils import calculate_tile_score, apply_bonus


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

        for i in range(15):  # Assuming a 15x15 board
            for j in range(15):
                space = pygame.Rect(340 + 50 * i, 120 + 50 * j, 40, 40)
                self.spaces.append(space)
     

board = Board() 
    
    # Board-related methods...





def update_player_score(score):
    global player_score  # Assuming player_score is a global variable representing the player's score
    player_score += score

def adjacent_spaces(space_rect):
    adjacent = []
    for delta in [(0, -40), (0, 40), (-40, 0), (40, 0)]:
        adjacent_rect = space_rect.move(delta)
        if adjacent_rect.collidelist(board.spaces) != -1:
            adjacent.append(adjacent_rect)
    return adjacent

def is_valid_move(space_rect):
    # Check if the space is empty
    if space_rect not in board.occupied_spaces:
        # Check if the space is adjacent to an existing tile on the board
        adjacent = False
        for adjacent_space in adjacent_spaces(space_rect):
            if adjacent_space in board.occupied_spaces:
                adjacent = True
                break
        if adjacent:
            return True
    return False



def move_tile(active_letter, space_rect):
    # Move the tile to the board position
    letter = board.letters.pop(active_letter)
    letter.topleft = space_rect.topleft
    board.occupied_spaces.append(space_rect)
    # Apply bonus if applicable
    tile_score = calculate_tile_score(letter)  # Implement this function based on your scoring system
    tile_score = apply_bonus(tile_score, space_rect)
    update_player_score(tile_score)  # Implement this function to update the player's score
    # Replenish the rack with a new tile
    new_letter = pygame.Rect(390 + 100 * (len(board.letters) + 1), 901, 20, 20)
    board.letters.append(new_letter)