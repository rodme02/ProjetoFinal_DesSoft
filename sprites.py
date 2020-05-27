import pygame
from config import WIDTH, GRAVITY, JUMPING_SIZE, GROUND, RUN, JUMPING, FALLING, OBSTACLE_SIZE

# Class que representa os obstáculos do cenário
class Tile(pygame.sprite.Sprite):
    # Construtor da classe pai
    def __init__(self, tile_img, x, y, speedx):
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do obstáculo
        tile_img = pygame.transform.scale(tile_img, (OBSTACLE_SIZE, OBSTACLE_SIZE))

        # Define a imagem do obstáculo
        self.image = tile_img
        # Detalhes sobre o posicionamento
        self.rect = self.image.get_rect()

        # Posiciona o obstáculo
        self.rect.x = x
        self.rect.y = y

        self.speedx = speedx

        self.movement = [speedx,0]

    # Atualiza a posição dos obstáculos
    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()

# Class que representa o jogador
class Player(pygame.sprite.Sprite):

    # Construtor da classe pai
    def __init__(self, player_img):
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        self.state = RUN

        # Aumenta o tamanho da imagem
        player_img = pygame.transform.scale(player_img, (150, 150))

        # Define a imagem do sprite
        self.image = player_img
        # Detalhes sobre o posicionamento
        self.rect = self.image.get_rect()

        # Posição inicical
        self.rect.centerx = int(WIDTH/3)
        self.rect.top = GROUND

        self.speedy = 0

    # Atualiza a posição do jogador
    def update(self):
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0
            self.state = RUN

    # Faz o personagem pular
    def JUMPING(self):
        if self.state == RUN:
            self.speedy -= JUMPING_SIZE
            self.state = JUMPING