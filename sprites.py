import pygame
from os import path
from config import WIDTH, GRAVITY, JUMPING_SIZE, GROUND, STILL, WALKING, JUMPING, SPIKE_SIZE, SNAKE_SIZE
import gamescreen
import random

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
        self.image = list_blocks[random.randint(0,1)]
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

# Spritesheet do jogador
def load_spritesheet(spritesheet, rows, columns):
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height))
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

# Class que representa o jogador na game screen
class Player(pygame.sprite.Sprite):

    # Construtor da classe pai
    def __init__(self, player_sheet):

        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        player_sheet = pygame.transform.scale(player_sheet, (800, 700))

        # Define sequências de sprites de cada animação
        spritesheet = load_spritesheet(player_sheet, 4, 8)
        self.animations = {
            STILL: [spritesheet[0], spritesheet[5]],
            WALKING: spritesheet[25:32],
            JUMPING: spritesheet[6:8],
        }
        # Define estado atual
        self.state = STILL
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]

        # Detalhes sobre o posicionamento
        self.rect = self.image.get_rect()

        # Posição inicical
        self.rect.centerx = int(WIDTH/3)
        self.rect.top = GROUND

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 100

        self.speedy = 0

    # Atualiza a posição do jogador
    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        # Se já está na hora de mudar de imagem
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            # Reinicia a animação caso o índice da imagem atual seja inválido
            if self.frame >= len(self.animation):
                self.frame = 0
            # Atualiza imagem atual
            self.image = self.animation[self.frame]

        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = JUMPING

        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0
            self.state = WALKING

    # Faz o personagem pular
    def JUMPING(self):
        if self.state == WALKING or self.state == STILL:
            jump = pygame.mixer.Sound(path.join('audio', 'jump.wav'))
            jump.set_volume(0.2)
            jump.play()
            self.speedy -= JUMPING_SIZE
            self.state = JUMPING

# Class que representa o jogador na instruction screen
class PlayerInstru(pygame.sprite.Sprite):

    # Construtor da classe pai
    def __init__(self, player_sheet):

        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        player_sheet = pygame.transform.scale(player_sheet, (800, 700))

        # Define sequências de sprites de cada animação
        spritesheet = load_spritesheet(player_sheet, 4, 8)
        self.animations = {
            STILL: spritesheet[0:1],
            WALKING: spritesheet[24:32],
            JUMPING: spritesheet[6:8],
        }
        # Define estado atual
        self.state = STILL
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]

        # Detalhes sobre o posicionamento
        self.rect = self.image.get_rect()

        # Posição inicical
        self.rect.centerx = int(WIDTH/3)
        self.rect.top = GROUND

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 100

        self.speedy = 0

    # Atualiza a posição do jogador
    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        # Se já está na hora de mudar de imagem
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            # Reinicia a animação caso o índice da imagem atual seja inválido
            if self.frame >= len(self.animation):
                self.frame = 0
            # Atualiza imagem atual
            self.image = self.animation[self.frame]

        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = JUMPING

        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0
            self.state = STILL

    # Faz o personagem pular
    def JUMPING(self):
        if self.state == STILL:
            jump = pygame.mixer.Sound(path.join('audio', 'jump.wav'))
            jump.set_volume(0.2)
            jump.play()
            self.speedy -= JUMPING_SIZE
            self.state = JUMPING