from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
audio_dir = path.join(path.dirname(__file__), 'audio')

# Dados gerais do jogo.
TITULO = "Johnny's Run"
WIDTH = 1024 # Largura da tela
HEIGHT = 768 # Altura da tela
FPS = 60 # Frames por segundo
PLAYER_IMG = 'player_img'
BLOCK_IMG = 'block_img'
BACKGROUND_IMG = 'background_img'

GRAVITY = 2
JUMPING_SIZE = 28
GROUND = HEIGHT - 90

RUN = 0
JUMPING = 1
FALLING = 2

# Define algumas variáveis com as cores básicas
BLACK = (0, 0, 0)

# Define a velocidade inicial do mundo
world_speed = -10

# Outras constantes
INITIAL_BLOCKS = 6
OBSTACLE_SIZE = 80
