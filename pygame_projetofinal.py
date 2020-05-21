"""
Programa do jogo Johnny Run
Autores: Rodrigo Paoilello de Medeiros e Pedro Santana Costa
"""

# Importando as bibliotecas necessárias.
import pygame
from os import path
from config import TITULO, WIDTH, HEIGHT
from gamescreen import game_screen

# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Música do jogo
pygame.mixer.music.load(path.join('audio', 'song.wav'))
pygame.mixer.music.play(-1)


# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime titulo
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()