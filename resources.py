# resources.py
import pygame

def load_tile_images():
    tile_images = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        tile_images[letter] = pygame.image.load(f'images/{letter}_tile.png')
    return tile_images

def load_bonus_tile_images():
    bonus_images = {
        'TW': pygame.image.load('images/TW_tile.png'),
        'DW': pygame.image.load('images/DW_tile.png'),
        'TL': pygame.image.load('images/TL_tile.png'),
        'DL': pygame.image.load('images/DL_tile.png'),
        'CL': pygame.image.load('images/Center_tile.png')
    }
    return bonus_images
# Load letter tile images
letter_images = {}
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    letter_images[letter] = pygame.image.load(f'images/{letter}_tile.png')

# Load other resources like sounds or fonts as needed
