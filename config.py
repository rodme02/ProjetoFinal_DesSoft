from os import path

# Estabelece a pasta que contém as figuras e sons
img_dir = path.join(path.dirname(__file__), 'img')
audio_dir = path.join(path.dirname(__file__), 'audio')
font_dir = path.join(path.dirname(__file__), 'font')

# Dados gerais do jogo
TITULO = "Johnny's Run"
WIDTH = 1180 # Largura da tela
HEIGHT = 800 # Altura da tela
FPS = 60 # Frames por segundo
PLAYER_IMG = 'player_img'
BLOCK_IMG = 'block_img'
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
JUMPING_SIZE = 30
GROUND = HEIGHT - 120

# Estados do jogador
RUN = 0
JUMPING = 1
FALLING = 2

# Define a cor preto
BLACK = (0, 0, 0)

# Constantes do obstáculo
INITIAL_BLOCKS = 2
OBSTACLE_SIZE = 80
