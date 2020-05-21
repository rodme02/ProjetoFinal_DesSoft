import pygame
from os import path
import random
from sprites import Tile, Player
from config import PLAYER_IMG, INITIAL_BLOCKS, WIDTH, HEIGHT, world_speed, FPS, img_dir, BLOCK_IMG, BACKGROUND_IMG, GROUND, BLACK
from assets import load_assets

def game_screen(screen):
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
    # Cria blocos espalhados em posições aleatórias do mapa
    for blocks in range(INITIAL_BLOCKS):
        block_x = random.randint(int(WIDTH), int(WIDTH*2))
        block_y = (GROUND-80)
        block = Tile(assets[BLOCK_IMG], block_x, block_y, world_speed)
        world_sprites.add(block)
        # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
        sprites.add(block)

    PLAYING = 0
    DONE = 1

    state = PLAYING
    while state != DONE:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

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
            print('morreu')
            state = DONE 

        # Verifica se algum bloco saiu da janela
        for block in world_sprites:
            if block.rect.right < 0:
                # Destrói o bloco e cria um novo no final da tela
                block.kill()
                block_x = random.randint(int(WIDTH*5), int(WIDTH*7))
                block_y = (GROUND-80)
                new_block = Tile(assets[BLOCK_IMG], block_x, block_y, world_speed)
                sprites.add(new_block)
                world_sprites.add(new_block)
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


        sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()