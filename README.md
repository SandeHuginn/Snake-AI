# Snake AI

Projeto de evolução do clássico jogo da cobrinha desenvolvido em Python
com Pygame.

A proposta deste projeto é transformar o jogo tradicional em um ambiente
onde uma Inteligência Artificial possa aprender a jogar através de
Aprendizado por Reforço (Reinforcement Learning).

## Origem do projeto

Este projeto é uma evolução de um jogo da cobrinha
desenvolvido anteriormente em Python e Pygame.

A versão original do jogo serviu como base para o
desenvolvimento deste projeto, que adiciona conceitos
de Inteligência Artificial e Aprendizado por Reforço.

## Objetivo

Desenvolver uma IA capaz de aprender estratégias para jogar Snake
utilizando tentativa e erro.

A IA deverá observar o estado do jogo, escolher uma ação e receber
recompensas ou punições de acordo com o resultado de suas decisões.

## Tecnologias

- Python
- Pygame
- Aprendizado por Reforço
- Q-Learning

## Funcionamento atual

Atualmente o projeto possui:

- Menu principal
- Sistema de pontuação
- Movimento da cobra
- Geração aleatória da comida
- Colisão com paredes
- Colisão com o próprio corpo
- Tela de Game Over
- Controle através do teclado

## Objetivo da Inteligência Artificial

A futura IA deverá:

1. Observar o estado atual do jogo.
2. Identificar possíveis perigos.
3. Observar a posição da comida.
4. Escolher uma ação.
5. Receber uma recompensa ou punição.
6. Atualizar seu conhecimento.
7. Repetir o processo durante várias partidas.

### Sistema inicial de recompensas

| Situação | Recompensa |
|---|---:|
| Comer comida | +10 |
| Morrer | -10 |
| Movimento normal | -0.1 |

Esses valores poderão ser alterados durante os testes.

## Arquitetura planejada

Estado do jogo
      ↓
Agente de IA
      ↓
Escolha de ação
      ↓
Snake executa ação
      ↓
Recebe recompensa
      ↓
Agente aprende
      ↓
Novo estado

## Diário de desenvolvimento

### Etapa 1 — Refatoração da movimentação

Foi iniciado o processo de preparação do jogo para receber
uma Inteligência Artificial.

Foram criadas constantes para representar as direções:

- CIMA
- DIREITA
- BAIXO
- ESQUERDA

Também foi criada a função `mover_cobra()` para separar
a decisão da direção da execução do movimento.

### Próximo passo

Criar uma representação do estado do jogo que possa ser
interpretada pelo agente de IA.