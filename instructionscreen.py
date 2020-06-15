from os import path
import pygame
from config import img_dir, BLACK, WHITE, FPS, PLAYING, DONE, WIDTH, HEIGHT, font_dir, INSTRUCTION
from sprites import PlayerInstru

def instruction_screen(screen):

    # Variável para o ajuste do FPS
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    background_rect = background.get_rect()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    playbutton = pygame.image.load(path.join(img_dir, 'playbutton.png')).convert_alpha()
    background.blit(playbutton, (440, 180))
    playbutton = playbutton.get_rect()
    playbutton.x = 440
    playbutton.y = 180

    font = pygame.font.Font(path.join(font_dir, 'fonte.TTF'), 70)
    instru_texto = font.render('Aperte ESPAÇO para pular', True, (WHITE))
    background.blit(instru_texto, (150, 50))

    # Carrega spritesheet
    player_sheet = pygame.image.load(path.join(img_dir, 'hero.png')).convert_alpha()
    # Cria sprite do jogador
    player = PlayerInstru(player_sheet)
    # Cria um grupo de todos os sprites e adiciona o jogador
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    state = INSTRUCTION
    while state == INSTRUCTION:

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

            # Verifica se soltou alguma tecla
            if event.type == pygame.KEYDOWN:
                # Faz o jogador pular
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.JUMPING()

        all_sprites.update()

        # A cada loop redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Desenha os sprites
        all_sprites.draw(screen)

        # Depois de desenhar tudo inverte o display
        pygame.display.flip()

    return state