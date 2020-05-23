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

LOGO_IMG = 'logo_img'
LOGO_SIZE = 100

PLAYING = 0
DONE = 1
INIT = 2
PLAYAGAIN = 3

GRAVITY = 2
JUMPING_SIZE = 33
GROUND = HEIGHT - 90

RUN = 0
JUMPING = 1
FALLING = 2

# Define algumas variáveis com as cores básicas
BLACK = (0, 0, 0)

# Outras constantes
INITIAL_BLOCKS = 2
OBSTACLE_SIZE = 80
