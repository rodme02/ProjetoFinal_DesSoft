"""
Programa do jogo Johnny Run
Autores: Rodrigo Paoilello de Medeiros e Pedro Santana Costa
"""

# Importando as bibliotecas necessárias
from os import path
import pygame
from config import TITULO, WIDTH, HEIGHT, INIT, DONE, PLAYING
from gamescreen import game_screen
from initscreen import init_screen

# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime titulo
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))

# Comando para evitar travamentos.
state = INIT
while state != DONE:
    if state == INIT:
        state = init_screen(screen)
    elif state == PLAYING:
        state = game_screen(screen)
    else:
        state = INIT
        pygame.mixer.music.stop()

pygame.quit()