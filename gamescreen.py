import pygame
from os import path
import random
from sprites import Tile, Player
from config import PLAYER_IMG, WIDTH, HEIGHT, FPS, img_dir, BLOCK_IMG, BACKGROUND_IMG, GROUND, BLACK, PLAYING, DONE, PLAYAGAIN
from assets import load_assets

def game_screen(screen):
    world_speed = -10

    # Música do jogo
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.load(path.join('audio', 'fill.wav'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play()


    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega imagem
    player_img = pygame.image.load(path.join(img_dir, 'johnny.png')).convert_alpha()

    # Cria Sprite do jogador
    player = Player(player_img)
    # Cria um grupo de todos os sprites e adiciona o jogador.
    sprites = pygame.sprite.Group()
    sprites.add(player)

    # Carrega assets
    assets = load_assets(img_dir)

    # Carrega o fundo do jogo
    background = assets[BACKGROUND_IMG]
    # Redimensiona o fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # Cria Sprite do jogador
    player = Player(assets[PLAYER_IMG])
    # Cria um grupo de todos os sprites e adiciona o jogador.
    sprites = pygame.sprite.Group()
    sprites.add(player)
    
    # Cria um grupo para guardar somente os sprites do mundo (obstáculos, objetos, etc).
    # Esses sprites vão andar junto com o mundo (fundo)
    world_sprites = pygame.sprite.Group()

    font = pygame.font.Font(pygame.font.get_default_font(), 40)

    pygame.time.set_timer(pygame.USEREVENT+1, 100) # Timer de 1 milisegundo para aumentar a velocidade do jogo

    pygame.time.set_timer(pygame.USEREVENT+2, 1500) # Timer de 1 segundo para criar novos blocos

    score = 0
    highscore = 0
    state = PLAYING
    while state == PLAYING:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (teclado, mouse e tempo)
        for event in pygame.event.get():

            if event.type == pygame.USEREVENT+1:
                # Aumenta a velocidade do jogo
                world_speed -= 1e-2
                score += 1

            if event.type == pygame.USEREVENT+2:
                # Cria novos blocos
                block_x = random.randint(int(WIDTH), int(WIDTH*1.5))
                block_y = (GROUND-80)
                block = Tile(assets[BLOCK_IMG], block_x, block_y, world_speed)
                world_sprites.add(block)
                # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
                sprites.add(block)
                
            if event.type == pygame.USEREVENT:
                pygame.mixer.music.load(path.join('audio', 'song.wav'))
                pygame.mixer.music.set_volume(0.8)
                pygame.mixer.music.play(-1)

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.JUMPING()
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE

        hits = pygame.sprite.spritecollide(player, world_sprites, True, pygame.sprite.collide_mask)

        if len(hits) > 0:
            crash = pygame.mixer.Sound(path.join('audio', 'crash.wav'))
            crash.play()
            if score > highscore:
                highscore = score
            state = PLAYAGAIN
    
        # Verifica se algum bloco saiu da janela
        for block in world_sprites:
            if block.rect.right < 0:
                # Destrói o bloco e cria um novo no final da tela
                block.kill()
                block_x = random.randint(int(WIDTH), int(WIDTH*4))
                block_y = (GROUND-80)
                block = Tile(assets[BLOCK_IMG], block_x, block_y, world_speed)
                sprites.add(block)
                world_sprites.add(block)
        sprites.update()
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        sprites.draw(screen)

        # Atualiza a posição da imagem de fundo.
        background_rect.x += world_speed

        # Se o fundo saiu da janela, faz ele voltar para dentro.
        if background_rect.right < 0:
            background_rect.x += background_rect.width
        # Desenha o fundo e uma cópia para a direita.
        # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
        # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
        screen.blit(background, background_rect)
        # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        screen.blit(background, background_rect2)

        score_texto = font.render('score: {0}'.format(score), True, (BLACK))
        screen.blit(score_texto, (10, 10))
        

        highscore_texto = font.render('highscore: {0}'.format(highscore), True, (BLACK))
        screen.blit(highscore_texto, (10, 50))
        



        sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
