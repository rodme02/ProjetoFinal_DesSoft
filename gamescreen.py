import pygame
from os import path
import random
from sprites import Spike, Player
from config import WIDTH, HEIGHT, GROUND, FPS, img_dir, font_dir, SPIKE_IMG, SNAKE_IMG, BACKGROUND_IMG, BLACK, WHITE, PLAYING, DONE, PLAYAGAIN
from assets import load_assets

highscore = 0
world_speed = -11

def game_screen(screen):
    
    
    # Música do jogo
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.load(path.join('audio', 'fill.wav'))
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    

    # Variável para o ajuste do FPS
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Carrega o fundo do jogo
    background = assets[BACKGROUND_IMG]
    # Redimensiona o fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # Carrega spritesheet
    player_sheet = pygame.image.load(path.join(img_dir, 'hero.png')).convert_alpha()
    # Cria sprite do jogador
    player = Player(player_sheet)
    # Cria um grupo de todos os sprites e adiciona o jogador
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    # Cria um grupo para guardar somente os sprites do mundo
    world_sprites = pygame.sprite.Group()

    font = pygame.font.Font(path.join(font_dir, 'fonte.TTF'), 40)

    pygame.time.set_timer(pygame.USEREVENT+1, 10) # Timer de 100 milisegundos para aumentar a velocidade do jogo

    pygame.time.set_timer(pygame.USEREVENT+2, random.randint(1000, 2000)) # Timer aleatório de 1 a 2 segundos para criar novos blocos

    # Define o score inicial
    score = 0

    # Define a variável world_speed inicial e a define como como global
    global world_speed
    world_speed = -12

    # Define a variável highscore como global
    global highscore

    # Game Loop
    state = PLAYING
    while state == PLAYING:

        # Ajusta o FPS
        clock.tick(FPS)

        # Processa os eventos
        for event in pygame.event.get():

            if event.type == pygame.USEREVENT+1:
                # Aumenta a velocidade do jogo
                world_speed -= 1e-3

                # Conta os pontos da partida
                score += 1e-1

            # Cria novos blocos em função do timer
            if event.type == pygame.USEREVENT+2:
                block_x = random.randint(int(WIDTH), int(WIDTH*1.5))
                block_y = (GROUND - 130)
                block = Spike(assets[SPIKE_IMG], assets[SNAKE_IMG], block_x, block_y, world_speed)
                world_sprites.add(block)
                all_sprites.add(block)
                
            if event.type == pygame.USEREVENT:
                pygame.mixer.music.load(path.join('audio', 'song.wav'))
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)

            # Verifica se soltou alguma tecla
            if event.type == pygame.KEYDOWN:
                # Faz o jogador pular
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.JUMPING()
            
            # Verifica se o jogo foi fechado
            if event.type == pygame.QUIT:
                state = DONE

        
        hits = pygame.sprite.spritecollide(player, world_sprites, True, pygame.sprite.collide_mask)

        if len(hits) > 0:
            state = PLAYAGAIN
            death = pygame.mixer.Sound(path.join('audio', 'death.wav'))
            death.set_volume(0.7)
            death.play()
            if score > highscore:
                highscore = score

        all_sprites.update()
        
    
        # A cada loop redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Atualiza a posição do fundo
        background_rect.x += world_speed

        # Se o fundo saiu da janela, desenha outro pra direita
        if background_rect.right < 0:
            background_rect.x += background_rect.width
        screen.blit(background, background_rect)

        # Desenha a imagem deslocada
        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        screen.blit(background, background_rect2)

        # Mostra o score da partida atual
        score_texto = font.render('score: {0}'.format(int(score)), True, (WHITE))
        screen.blit(score_texto, (30, 70))
        
        # Mostra o highscore
        highscore_texto = font.render('highscore: {0}'.format(int(highscore)), True, (WHITE))
        screen.blit(highscore_texto, (30, 25))
        
        # Desenha os sprites
        all_sprites.draw(screen)

        # Após desenhar inverte o display
        pygame.display.flip()

    return state, highscore, world_speed