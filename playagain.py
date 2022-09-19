from os import path
import pygame
from config import img_dir, font_dir, BLACK, WHITE, FPS, PLAYING, DONE, WIDTH, HEIGHT, PLAYAGAIN, INSTRUCTION
import gamescreen

playbutton_x = 440
playbutton_y = 450
instru_x = playbutton_x
instru_y = 590

def play_again(screen):
    
    # Música do menu
    pygame.mixer.music.load(path.join('audio', 'intro.wav'))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    
    # Variável para o ajuste do FPS
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    background_rect = background.get_rect()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    font = pygame.font.Font(path.join(font_dir, 'fonte.TTF'), 70)
    gameover_texto = font.render('Game Over!', True, (WHITE))
    background.blit(gameover_texto, (407, 120))
    playagain_texto = font.render('Quer tentar de novo?', True, (WHITE))
    background.blit(playagain_texto, (250, 250))

    playbutton = pygame.image.load(path.join(img_dir, 'playbutton.png')).convert_alpha()
    background.blit(playbutton, (playbutton_x, playbutton_y))
    playbutton = playbutton.get_rect()
    playbutton.x = playbutton_x
    playbutton.y = playbutton_y

    instru = pygame.image.load(path.join(img_dir, 'instructions.png')).convert_alpha()
    background.blit(instru, (instru_x, instru_y))
    instru = instru.get_rect()
    instru.x = instru_x
    instru.y = instru_y
    
    # Mostra o highscore
    font = pygame.font.Font(path.join(font_dir, 'fonte.TTF'), 40)
    highscore = gamescreen.highscore
    
    highscore_texto = font.render('highscore: {0}'.format(int(highscore)), True, (WHITE))
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

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                if instru.collidepoint(mouse_x, mouse_y):
                    state = INSTRUCTION

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo inverte o display
        pygame.display.flip()

    return state