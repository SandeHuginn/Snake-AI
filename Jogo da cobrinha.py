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

        escrever("JOGO DA COBRINHA", VERDE, 45, 120, 50)
        escrever("1 - Jogar", BRANCO, 30, 180, 150)
        escrever("2 - Pontuações", BRANCO, 30, 180, 195)
        escrever("3 - Testar IA", BRANCO, 30, 180, 240)
        escrever("4 - Sair", BRANCO, 30, 180, 285)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_1:
                    jogo(modo_ia=False)

                elif evento.key == pygame.K_2:
                    tela_pontuacoes()

                elif evento.key == pygame.K_3:
                    jogo(modo_ia=True)

                elif evento.key == pygame.K_4:
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

# Verifica se uma posição é perigosa
def existe_perigo(x, y, direcao, cobra_lista, comida_x, comida_y):

    # Calcula a próxima posição da cobra
    proximo_x, proximo_y = mover_cobra(x, y, direcao)

    # Verifica se a cobra vai bater na parede
    if (
        proximo_x < 0
        or proximo_x >= LARGURA
        or proximo_y < 0
        or proximo_y >= ALTURA
    ):
        return True

    # Verifica se a cobra vai bater no próprio corpo
    proxima_posicao = [proximo_x, proximo_y]

    corpo = cobra_lista[:-1]

    # Se não comer, a cauda normalmente vai sair da posição atual
    vai_comer = (
        proximo_x == comida_x
        and proximo_y == comida_y
    )

    if not vai_comer and corpo:
        corpo = corpo[1:]

    if proxima_posicao in corpo:
        return True

    # Se não encontrar perigo
    return False

# Obtém o estado atual para a IA
def obter_estado(x, y, direcao, cobra_lista, comida_x, comida_y):

    # Descobre as direções relativas à cobra
    direcao_direita = (direcao + 1) % 4
    direcao_esquerda = (direcao - 1) % 4

    # Detecta os perigos
    perigo_frente = existe_perigo(
        x, y, direcao, cobra_lista, comida_x, comida_y
    )

    perigo_direita = existe_perigo(
        x, y, direcao_direita, cobra_lista, comida_x, comida_y
    )

    perigo_esquerda = existe_perigo(
        x, y, direcao_esquerda, cobra_lista, comida_x, comida_y
    )

    # Retorna as informações em uma tupla
    estado = (
        perigo_frente,
        perigo_direita,
        perigo_esquerda,

        direcao == ESQUERDA,
        direcao == DIREITA,
        direcao == CIMA,
        direcao == BAIXO,

        comida_x < x,
        comida_x > x,
        comida_y < y,
        comida_y > y
    )

    return estado

def escolher_acao_aleatoria(estado):
    # Lê os três primeiros valores do estado:
    # perigo à frente, à direita e à esquerda.
    perigo_frente = estado[0]
    perigo_direita = estado[1]
    perigo_esquerda = estado[2]

    # Guarda as ações que não apresentam perigo imediato.
    acoes_seguras = []

    if not perigo_frente:
        acoes_seguras.append(0)

    if not perigo_direita:
        acoes_seguras.append(1)

    if not perigo_esquerda:
        acoes_seguras.append(2)

    # Se houver ações seguras, escolhe uma delas.
    if acoes_seguras:
        return random.choice(acoes_seguras)

    # Se todas forem perigosas, escolhe uma ação mesmo assim.
    return random.choice([0, 1, 2])


def aplicar_acao(direcao, acao):
    # Ação 0: continuar em frente.
    if acao == 0:
        return direcao

    # Ação 1: virar à direita.
    elif acao == 1:
        return (direcao + 1) % 4

    # Ação 2: virar à esquerda.
    elif acao == 2:
        return (direcao - 1) % 4

    return direcao

# JOGO
def jogo(modo_ia=False):

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
                        jogo(modo_ia=modo_ia)

                    elif evento.key == pygame.K_m:
                        return

                    elif evento.key == pygame.K_q:
                        pygame.quit()
                        quit()

        # EVENTOS
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                fim_jogo = True

            elif evento.type == pygame.KEYDOWN and not modo_ia:

                if evento.key == pygame.K_LEFT:
                    direcao = ESQUERDA

                elif evento.key == pygame.K_RIGHT:
                    direcao = DIREITA

                elif evento.key == pygame.K_UP:
                    direcao = CIMA

                elif evento.key == pygame.K_DOWN:
                    direcao = BAIXO

        # Encerra o loop se a janela for fechada.
        if fim_jogo:
            break

        # Se estiver no modo IA, ela escolhe a direção.
        if modo_ia:
            estado = obter_estado(
            x, y, direcao, cobra_lista, comida_x, comida_y
        )

        acao = escolher_acao_aleatoria(estado)

        direcao = aplicar_acao(direcao, acao)

        # Atualiza posição
        x, y = mover_cobra(x, y, direcao)

        # Colisão com parede
        if x >= LARGURA or x < 0 or y >= ALTURA or y < 0:
            
            pontuacoes.append(comprimento - 1)

            game_over = True
            continue

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