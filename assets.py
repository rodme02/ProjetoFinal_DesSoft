import pygame
from os import path
from config import SPIKE_IMG, SNAKE_IMG, BACKGROUND_IMG, LOGO_IMG

# Carrega os assets
def load_assets(img_dir):
    assets = {}
    assets[SPIKE_IMG] = pygame.image.load(path.join(img_dir, 'spikes.png')).convert_alpha()
    assets[SNAKE_IMG] = pygame.image.load(path.join(img_dir, 'snake_1.png')).convert_alpha()
    assets[BACKGROUND_IMG] = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    assets[LOGO_IMG] = pygame.image.load(path.join(img_dir, 'logo.png')).convert_alpha()
    return assets