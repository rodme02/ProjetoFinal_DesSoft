"""
Programa do jogo Johnny Run
Autores: Rodrigo Paoilello de Medeiros e Pedro Santana Costa
"""

# Importando as bibliotecas necessárias.
import pygame
import random
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

# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

'''
# Música do jogo
pygame.mixer.music.load(path.join('audio', 'song.wav'))
pygame.mixer.music.play(-1)
'''

# Class que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, x, y, speedx):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (OBSTACLE_SIZE, OBSTACLE_SIZE))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = x
        self.rect.y = y

        self.speedx = speedx

    def update(self):
        self.rect.x += self.speedx


# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = RUN

        # Aumenta o tamanho da imagem
        player_img = pygame.transform.scale(player_img, (150, 150))

        # Define a imagem do sprite.
        self.image = player_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posição inicical
        self.rect.centerx = int(WIDTH/3)
        self.rect.top = GROUND

        self.speedy = 0

        # Metodo que atualiza a posição do personagem
    def update(self):
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            # Reposiciona para a posição do chão
            self.rect.bottom = GROUND
            # Para de cair
            self.speedy = 0
            # Atualiza o estado para parado
            self.state = RUN

    # Faz o personagem pular
    def JUMPING(self):
        if self.state == RUN:
            self.speedy -= JUMPING_SIZE
            self.state = JUMPING

# Carrega os assets
def load_assets(img_dir):
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(path.join(img_dir, 'johnny.png')).convert_alpha()
    assets[BLOCK_IMG] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert()
    assets[BACKGROUND_IMG] = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    return assets

def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega imagem
    player_img = pygame.image.load(path.join(img_dir, 'johnny.png')).convert_alpha()

    # Cria Sprite do jogador
    player = Player(player_img)
    # Cria um grupo de todos os sprites e adiciona o jogador.
    sprites = pygame.sprite.Group()
    sprites.add(player)

    # Carrega assets
    assets = load_assets(img_dir)

    # Carrega o fundo do jogo
    background = assets[BACKGROUND_IMG]
    # Redimensiona o fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # Cria Sprite do jogador
    player = Player(assets[PLAYER_IMG])
    # Cria um grupo de todos os sprites e adiciona o jogador.
    sprites = pygame.sprite.Group()
    sprites.add(player)

    # Cria um grupo para guardar somente os sprites do mundo (obstáculos, objetos, etc).
    # Esses sprites vão andar junto com o mundo (fundo)
    world_sprites = pygame.sprite.Group()
    # Cria blocos espalhados em posições aleatórias do mapa
    for i in range(INITIAL_BLOCKS):
        block_x = random.randint(int(WIDTH), int(WIDTH*2))
        block_y = (GROUND-80)
        block = Tile(assets[BLOCK_IMG], block_x, block_y, world_speed)
        world_sprites.add(block)
        # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
        sprites.add(block)

    PLAYING = 0
    DONE = 1

    score = 0

    state = PLAYING
    while state != DONE:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.JUMPING()
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE

                '''
        for player in Tile:
            if player.rect.collidepoint(Tile.rect.x, Tile.rect.y):
                [print('morreu')]
                '''

        hits = pygame.sprite.spritecollide(player, world_sprites, True, pygame.sprite.collide_mask)

        if len(hits) > 0:
            print('morreu')
            state = DONE 

        # Verifica se algum bloco saiu da janela
        for block in world_sprites:
            if block.rect.right < 0:
                # Destrói o bloco e cria um novo no final da tela
                block.kill()
                block_x = random.randint(int(WIDTH * 3), int(WIDTH * 4))
                block_y = (GROUND-80)
                new_block = Tile(assets[BLOCK_IMG], block_x, block_y, world_speed)
                sprites.add(new_block)
                world_sprites.add(new_block)
        sprites.update()

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        sprites.draw(screen)

        # Atualiza a posição da imagem de fundo.
        background_rect.x += world_speed

        # Se o fundo saiu da janela, faz ele voltar para dentro.
        if background_rect.right < 0:
            background_rect.x += background_rect.width
        # Desenha o fundo e uma cópia para a direita.
        # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
        # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
        screen.blit(background, background_rect)
        # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        screen.blit(background, background_rect2)


        sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()



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