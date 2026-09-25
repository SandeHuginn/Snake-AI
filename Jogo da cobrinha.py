import pygame
import random

# Inicializa pygame
pygame.init()

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (213, 50, 80)
VERDE = (0, 255, 0)
AZUL = (50, 153, 213)

# Tela
LARGURA = 600
ALTURA = 400

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

clock = pygame.time.Clock()

# Configurações
TAMANHO_BLOCO = 10
VELOCIDADE = 15

# Direções
CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

# Fontes
fonte = pygame.font.SysFont("arial", 30)
fonte_titulo = pygame.font.SysFont("arial", 50)

# Lista para salvar pontuações
pontuacoes = []


def escrever(texto, cor, tamanho, x, y):
    fonte_temp = pygame.font.SysFont("arial", tamanho)
    texto_render = fonte_temp.render(texto, True, cor)
    tela.blit(texto_render, (x, y))


def desenhar_cobra(tamanho, lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(
            tela,
            VERDE,
            [bloco[0], bloco[1], tamanho, tamanho]
        )


def mostrar_pontuacao(score):
    texto = fonte.render(f"Pontos: {score}", True, BRANCO)
    tela.blit(texto, [10, 10])

# MENU PRINCIPAL
def menu():
    while True:
        tela.fill(PRETO)

        escrever("JOGO DA COBRINHA", VERDE, 45, 120, 60)

        escrever("1 - Iniciar Jogo", BRANCO, 30, 180, 170)
        escrever("2 - Pontuações", BRANCO, 30, 180, 220)
        escrever("3 - Sair", BRANCO, 30, 180, 270)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_1:
                    jogo()

                elif evento.key == pygame.K_2:
                    tela_pontuacoes()

                elif evento.key == pygame.K_3:
                    pygame.quit()
                    quit()

# TELA DE PONTUAÇÕES
def tela_pontuacoes():

    while True:

        tela.fill(PRETO)

        escrever("PONTUAÇÕES", AZUL, 45, 170, 40)

        if len(pontuacoes) == 0:
            escrever("Nenhuma pontuação ainda", BRANCO, 25, 150, 150)

        else:
            y = 120

            for i, pontos in enumerate(sorted(pontuacoes, reverse=True)):
                escrever(f"{i+1}° Lugar: {pontos}", BRANCO, 28, 180, y)
                y += 40

        escrever("ESC - Voltar", VERMELHO, 25, 210, 340)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

# Movimentação
def mover_cobra(x, y, direcao):
    if direcao == CIMA:
        y -= TAMANHO_BLOCO

    elif direcao == DIREITA:
        x += TAMANHO_BLOCO

    elif direcao == BAIXO:
        y += TAMANHO_BLOCO

    elif direcao == ESQUERDA:
        x -= TAMANHO_BLOCO

    return x,y

# JOGO
def jogo():

    fim_jogo = False
    game_over = False

    x = LARGURA / 2
    y = ALTURA / 2

    direcao = DIREITA

    cobra_lista = []
    comprimento = 1

    comida_x = round(
        random.randrange(0, LARGURA - TAMANHO_BLOCO) / 10.0
    ) * 10.0

    comida_y = round(
        random.randrange(0, ALTURA - TAMANHO_BLOCO) / 10.0
    ) * 10.0

    while not fim_jogo:

        # GAME OVER
        while game_over:

            tela.fill(PRETO)

            escrever("VOCÊ PERDEU!", VERMELHO, 45, 150, 100)

            escrever(
                "C - Jogar Novamente",
                BRANCO,
                30,
                150,
                200
            )

            escrever(
                "M - Menu Principal",
                BRANCO,
                30,
                150,
                240
            )

            escrever(
                "Q - Sair",
                BRANCO,
                30,
                150,
                280
            )

            pygame.display.update()

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_c:
                        jogo()

                    elif evento.key == pygame.K_m:
                        return

                    elif evento.key == pygame.K_q:
                        pygame.quit()
                        quit()

        # EVENTOS
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                fim_jogo = True

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_LEFT:
                    direcao = ESQUERDA

                elif evento.key == pygame.K_RIGHT:
                    direcao = DIREITA

                elif evento.key == pygame.K_UP:
                    direcao = CIMA

                elif evento.key == pygame.K_DOWN:
                    direcao = BAIXO

        # Colisão com parede
        if x >= LARGURA or x < 0 or y >= ALTURA or y < 0:

            pontuacoes.append(comprimento - 1)

            game_over = True

        # Atualiza posição
        x, y = mover_cobra(x, y, direcao)

        tela.fill(PRETO)

        # Comida
        pygame.draw.rect(
            tela,
            VERMELHO,
            [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO]
        )

        # Cobra
        cabeca = [x, y]
        cobra_lista.append(cabeca)

        if len(cobra_lista) > comprimento:
            del cobra_lista[0]

        # Colisão com o próprio corpo
        for bloco in cobra_lista[:-1]:

            if bloco == cabeca:

                pontuacoes.append(comprimento - 1)

                game_over = True

        desenhar_cobra(TAMANHO_BLOCO, cobra_lista)

        mostrar_pontuacao(comprimento - 1)

        pygame.display.update()

        # Comer comida
        if x == comida_x and y == comida_y:

            comida_x = round(
                random.randrange(
                    0,
                    LARGURA - TAMANHO_BLOCO
                ) / 10.0
            ) * 10.0

            comida_y = round(
                random.randrange(
                    0,
                    ALTURA - TAMANHO_BLOCO
                ) / 10.0
            ) * 10.0

            comprimento += 1

        clock.tick(VELOCIDADE)

    pygame.quit()
    quit()


# Inicia o menu
menu()