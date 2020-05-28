import pygame
from os import path
from config import img_dir, BLACK, FPS, PLAYING, DONE, WIDTH, HEIGHT, PLAYAGAIN
from gamescreen import *

def play_again(screen):
    
    # Música do menu
    pygame.mixer.music.load(path.join('audio', 'intro.wav'))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Variável para o ajuste do FPS
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    background_rect = background.get_rect()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    logo = pygame.image.load(path.join(img_dir, 'logo.png')).convert_alpha()
    background.blit(logo, (WIDTH/3.5, -30))

    playbutton = pygame.image.load(path.join(img_dir, 'playbutton.png')).convert_alpha()
    background.blit(playbutton, (375, 450))
    playbutton = playbutton.get_rect()
    playbutton.x = 375
    playbutton.y = 450
    
    # Mostra o highscore
    font = pygame.font.Font(pygame.font.get_default_font(), 50)
    
    highscore_texto = font.render('highscore: {0}'.format(highscore), True, (BLACK))
    background.blit(highscore_texto, (30, 25))
    
    
    state = PLAYAGAIN
    while state == PLAYAGAIN:

        # Ajusta o FPS
        clock.tick(FPS)

        # Processa os eventos
        for event in pygame.event.get():
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                state = DONE

            # Qualquer tecla para começar o jogo
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                if playbutton.collidepoint(mouse_x, mouse_y):
                    state = PLAYING

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo inverte o display
        pygame.display.flip()

    return state