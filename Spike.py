from os import path
import random
import pygame
from config import WIDTH, GRAVITY, JUMPING_SIZE, GROUND, STILL, WALKING, JUMPING, SPIKE_SIZE, SNAKE_SIZE
import gamescreen

# Class que representa o obstáculo espinho e cobra
class Spike(pygame.sprite.Sprite):
    # Construtor da classe pai
    def __init__(self, spike_img, snake_img, x, y, speedx):
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do obstáculo
        spike_img = pygame.transform.scale(spike_img, (SPIKE_SIZE, SPIKE_SIZE))
        snake_img = pygame.transform.scale(snake_img, (SNAKE_SIZE, SNAKE_SIZE))

        # Define a imagem do obstáculo
        list_blocks = [spike_img, snake_img]
        self.image = list_blocks[random.randint(0, 1)]
        # Detalhes sobre o posicionamento
        self.rect = self.image.get_rect()


        # Posiciona o obstáculo
        self.rect.x = x
        self.rect.y = y

        # Dedine a velocidade do obstáculo
        self.speedx = speedx
        self.movement = [speedx, 0]

    # Atualiza a posição dos obstáculos
    def update(self):
        world_speed = gamescreen.world_speed
        self.speedx = world_speed
        self.movement = [self.speedx, 0]
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()