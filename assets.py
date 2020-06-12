import pygame
from os import path
from config import BLOCK_IMG, BACKGROUND_IMG, LOGO_IMG

# Carrega os assets
def load_assets(img_dir):
    assets = {}
    assets[BLOCK_IMG] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert()
    assets[BACKGROUND_IMG] = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    assets[LOGO_IMG] = pygame.image.load(path.join(img_dir, 'logo.png')).convert_alpha()
    return assets