import pygame
from os import path
import random
from sprites import Tile, Player
from config import PLAYER_IMG, WIDTH, HEIGHT, GROUND, FPS, img_dir, BLOCK_IMG, BACKGROUND_IMG, BLACK, PLAYING, DONE, PLAYAGAIN
from assets import load_assets
from initscreen import init_screen

highscore = 0

def game_screen(screen):

    # Música do jogo
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.load(path.join('audio', 'fill.wav'))
    pygame.mixer.music.set_volume(0.4)
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

    # Cria sprite do jogador
    player = Player(assets[PLAYER_IMG])
    # Cria um grupo de todos os sprites e adiciona o jogador
    sprites = pygame.sprite.Group()
    sprites.add(player)
    
    # Cria um grupo para guardar somente os sprites do mundo
    world_sprites = pygame.sprite.Group()

    font = pygame.font.Font(pygame.font.get_default_font(), 30)

    pygame.time.set_timer(pygame.USEREVENT+1, 100) # Timer de 100 milisegundos para aumentar a velocidade do jogo

    pygame.time.set_timer(pygame.USEREVENT+2, random.randint(1000, 2000)) # Timer aleatório de 1 a 2 segundos para criar novos blocos

    # Define a velocidade e o score inicial
    world_speed = -11
    score = 0

    # Game Loop
    state = PLAYING
    while state == PLAYING:

        # Ajusta o FPS
        clock.tick(FPS)

        # Processa os eventos
        for event in pygame.event.get():

            if event.type == pygame.USEREVENT+1:
                # Aumenta a velocidade do jogo
                world_speed -= 1e-2
                score += 1

            # Cria novos blocos em função do timer
            if event.type == pygame.USEREVENT+2:
                block_x = random.randint(int(WIDTH), int(WIDTH*1.5))
                block_y = (GROUND-80)
                block = Tile(assets[BLOCK_IMG], block_x, block_y, world_speed)
                world_sprites.add(block)
                sprites.add(block)
                
            if event.type == pygame.USEREVENT:
                pygame.mixer.music.load(path.join('audio', 'song.wav'))
                pygame.mixer.music.set_volume(0.8)
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
            crash = pygame.mixer.Sound(path.join('audio', 'crash.wav'))
            crash.play()
            global highscore
            if score > highscore:
                highscore = score
            state = PLAYAGAIN
            
    
        '''
        for sprite in sprites:
            sprite.update_speed(world_speed)
        '''

        sprites.update()
        
    
        # A cada loop redesenha o fundo e os sprites
        screen.fill(BLACK)
        sprites.draw(screen)

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
        score_texto = font.render('score: {0}'.format(score), True, (BLACK))
        screen.blit(score_texto, (30, 60))
        
        
        # Mostra o highscore
        highscore_texto = font.render('highscore: {0}'.format(highscore), True, (BLACK))
        screen.blit(highscore_texto, (30, 25))
        
        
        # Desenha os sprites
        sprites.draw(screen)

        # Depois de desenhar tudo inverte o display
        pygame.display.flip()

    return state, highscore