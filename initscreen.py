import pygame
from os import path
from config import img_dir, BLACK, FPS, PLAYING, DONE, WIDTH, HEIGHT, INIT, INSTRUCTION

def init_screen(screen):

    
    # Música do menu
    pygame.mixer.music.load(path.join('audio', 'intro.wav'))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    
    # Variável para ajustar o FPS
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    background_rect = background.get_rect()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    logo = pygame.image.load(path.join(img_dir, 'logo.png')).convert_alpha()
    background.blit(logo, (WIDTH/3.5, -30))
    
    playbutton = pygame.image.load(path.join(img_dir, 'playbutton.png')).convert_alpha()
    background.blit(playbutton, (422, 430))
    playbutton = playbutton.get_rect()
    playbutton.x = 422
    playbutton.y = 430

    instru = pygame.image.load(path.join(img_dir, 'instructions.png')).convert_alpha()
    background.blit(instru, (422, 600))
    instru = instru.get_rect()
    instru.x = 422
    instru.y = 600

    state = INIT
    while state == INIT:

        # Ajusta o FPS
        clock.tick(FPS)

        # Processa os eventos
        for event in pygame.event.get():
            # Verifica se é para fechar
            if event.type == pygame.QUIT:
                state = DONE

            # Qualquer tecla para começar o jogo
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                if playbutton.collidepoint(mouse_x, mouse_y):
                    state = PLAYING

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                if instru.collidepoint(mouse_x, mouse_y):
                    state = INSTRUCTION

        # A cada loop, redesenha o fundo
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo inverte o display
        pygame.display.flip()

    return state