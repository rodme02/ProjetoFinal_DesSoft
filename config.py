from os import path

# Estabelece a pasta que contém as figuras e sons
img_dir = path.join(path.dirname(__file__), 'img')
audio_dir = path.join(path.dirname(__file__), 'audio')
font_dir = path.join(path.dirname(__file__), 'font')

# Dados gerais do jogo
TITULO = "Night Runner"
WIDTH = 1180 # Largura da tela
HEIGHT = 800 # Altura da tela
FPS = 90 # Frames por segundo
RUN_IMG = 'run_img'
JUMP_IMG = 'jump_img'
STILL_IMG = 'still_img'
SPIKE_IMG = 'spike_img'
SNAKE_IMG = 'snake_img'
BACKGROUND_IMG = 'background_img'
LOGO_IMG = 'logo_img'
LOGO_SIZE = 100

# Estados do jogo
PLAYING = 0
DONE = 1
INIT = 2
PLAYAGAIN = 3
INSTRUCTION = 4

# Variáveis para a posição do jogador
GRAVITY = 2
JUMPING_SIZE = 28
GROUND = HEIGHT - 140

# Estados do jogador
STILL = 0
WALKING = 1
JUMPING = 2

# Define as cores preto e branco
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Constantes do obstáculo
INITIAL_BLOCKS = 2
SPIKE_SIZE = 120
SNAKE_SIZE = 140
