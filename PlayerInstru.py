from os import path
import pygame
from config import WIDTH, GRAVITY, JUMPING_SIZE, GROUND, STILL, WALKING, JUMPING, SPIKE_SIZE, SNAKE_SIZE
from load_spritesheet import load_spritesheet

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
            jump.set_volume(0.15)
            jump.play()
            self.speedy -= JUMPING_SIZE
            self.state = JUMPING