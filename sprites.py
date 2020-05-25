from os import path
import pygame
from config import WIDTH, GRAVITY, JUMPING_SIZE, GROUND, RUN, JUMPING, FALLING, OBSTACLE_SIZE

# Class que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):
    # Construtor da classe pai (Sprite).
    def __init__(self, tile_img, x, y, speedx):
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

        self.movement = [speedx,0]

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()

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