import pygame
from os import path
from config import PLAYER_IMG, BLOCK_IMG, BACKGROUND_IMG

# Carrega os assets
def load_assets(img_dir):
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(path.join(img_dir, 'johnny.png')).convert_alpha()
    assets[BLOCK_IMG] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert()
    assets[BACKGROUND_IMG] = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    return assets