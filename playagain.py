import pygame
from os import path
from config import img_dir, BLACK, FPS, PLAYING, DONE, WIDTH, HEIGHT


def play_again(screen):

    # Música do menu
    pygame.mixer.music.load(path.join('audio', 'intro.wav'))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    background_rect = background.get_rect()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    logo = pygame.image.load(path.join(img_dir, 'logo.png')).convert_alpha()
    background.blit(logo,(256, 0))

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False

            if event.type == pygame.KEYUP:
                state = PLAYING
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

    
        font = pygame.font.Font(pygame.font.get_default_font(), 40)
        highscore_texto = font.render('highscore: {0}'.format(highscore), True, (BLACK))
        screen.blit(highscore_texto, (100, 50))
        

        # Depois de desenhar tudo
        pygame.display.flip()

    return state