"""
Programa do jogo Night Runner

Autores: Rodrigo Paoilello de Medeiros e Pedro Santana Costa
"""
# Importando as bibliotecas
import pygame
from config import TITULO, WIDTH, HEIGHT, INIT, DONE, PLAYING, PLAYAGAIN, INSTRUCTION
from gamescreen import game_screen
from initscreen import init_screen
from playagain import play_again
from instructionscreen import instruction_screen

# Inicialização do pygame
pygame.init()
pygame.mixer.init()

# Tamanho da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Loop do jogo
state, highscore, world_speed = INIT, 0, -11
while state != DONE:
    if state == INIT:
        state = init_screen(screen)
    elif state == PLAYING:
        state, highscore, world_speed = game_screen(screen)
    elif state == PLAYAGAIN:
        state = play_again(screen)
    elif state == INSTRUCTION:
        state = instruction_screen(screen)
    else:
        state = DONE

pygame.quit()