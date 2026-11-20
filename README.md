# Snake AI

Projeto de evolução do clássico jogo da cobrinha, desenvolvido em Python com Pygame.

A proposta é transformar o jogo tradicional em um ambiente no qual uma Inteligência Artificial possa aprender a jogar por meio de **Aprendizado por Reforço (Reinforcement Learning)**, utilizando o algoritmo **Q-Learning**. O projeto também conta com um assistente virtual integrado ao jogo, capaz de responder dúvidas sobre seu funcionamento e sobre os conceitos de Inteligência Artificial utilizados.

## Origem do projeto

Este projeto é uma evolução de um jogo da cobrinha desenvolvido anteriormente em Python e Pygame.

A versão original serviu como base para a implementação de conceitos de Inteligência Artificial, mantendo a mecânica tradicional do jogo e adicionando um agente capaz de aprender por tentativa e erro.

## Objetivo

Desenvolver uma IA capaz de aprender estratégias para jogar Snake.

Para isso, o agente observa o estado atual do jogo, escolhe uma ação e recebe recompensas ou punições de acordo com o resultado de suas decisões.

Com a repetição desse processo, a IA atualiza seus conhecimentos e busca melhorar seu desempenho.

Além disso, o projeto possui um assistente virtual que permite ao usuário consultar informações sobre o jogo, o algoritmo Q-Learning e os parâmetros utilizados no treinamento.

## Tecnologias

- Python
- Pygame (pygame-ce)
- Aprendizado por Reforço (Reinforcement Learning)
- Q-Learning
- Dialogflow ES
- Google Cloud

## Funcionamento atual

O projeto possui:

- Menu principal;
- Sistema de pontuação;
- Movimento da cobra;
- Geração aleatória de comida;
- Detecção de colisão com paredes;
- Detecção de colisão com o próprio corpo;
- Tela de Game Over;
- Controle manual através do teclado;
- Modo de teste da Inteligência Artificial;
- Treinamento automático da IA;
- Treinamento acelerado;
- Registro de estatísticas do aprendizado;
- Assistente virtual integrado ao jogo;
- Comunicação com o Dialogflow ES para processamento das mensagens.

## Inteligência Artificial

O agente utiliza o algoritmo **Q-Learning**, uma técnica de Aprendizado por Reforço que permite aprender quais ações são mais vantajosas em diferentes situações.

### Representação do estado

O estado do jogo é representado por um conjunto de 11 características booleanas:

1. Perigo à frente;
2. Perigo à direita;
3. Perigo à esquerda;
4. Direção atual para a esquerda;
5. Direção atual para a direita;
6. Direção atual para cima;
7. Direção atual para baixo;
8. Comida à esquerda;
9. Comida à direita;
10. Comida acima;
11. Comida abaixo.

Essas informações permitem que o agente identifique sua situação atual e escolha uma ação.

### Ações disponíveis

A IA pode escolher entre três ações:

- Avançar;
- Virar à direita;
- Virar à esquerda.

A direção escolhida é convertida em movimento dentro do jogo.

### Sistema de recompensas

O agente recebe recompensas ou punições conforme suas ações:

| Situação | Recompensa |
|---|---:|
| Comer comida | +10 |
| Morrer | -10 |
| Movimento normal | -0.1 |

Esses valores podem ser ajustados durante os experimentos para avaliar seu impacto no aprendizado.

### Parâmetros do Q-Learning

O agente utiliza os seguintes parâmetros iniciais:

| Parâmetro | Valor | Função |
|---|---:|---|
| Taxa de aprendizado (Alpha) | 0.1 | Controla quanto o agente aprende com novas experiências |
| Fator de desconto (Gamma) | 0.9 | Define a importância das recompensas futuras |
| Epsilon inicial | 1.0 | Define a probabilidade inicial de explorar ações |
| Epsilon mínimo | 0.05 | Limite mínimo de exploração |
| Decaimento do Epsilon | 0.995 | Reduz gradualmente a exploração |

O agente utiliza uma tabela Q para armazenar os valores aprendidos para cada estado e ação.

## Modos de execução da IA

O projeto possui diferentes formas de executar e observar o agente:

- **Teste da IA:** permite acompanhar a IA jogando normalmente.
- **Treinamento automático:** permite que o agente continue jogando várias partidas sem retornar ao menu entre elas.
- **Treinamento acelerado:** executa as partidas em velocidade maior, reduzindo a renderização para acelerar o processo de aprendizado.

Durante o treinamento, são registradas informações como quantidade de episódios, pontuação, média das últimas 20 partidas, estados conhecidos, atualizações da tabela Q e valor atual de Epsilon.

## Assistente virtual

O projeto possui um assistente virtual integrado ao jogo por meio do **Dialogflow ES**, serviço do Google Cloud utilizado para interpretar mensagens e fornecer respostas.

O usuário pode acessar o assistente pelo menu principal, selecionar a opção correspondente e enviar perguntas diretamente pela interface do Pygame.

A integração é realizada por meio do arquivo `chatbot.py`, responsável por:

- Estabelecer a comunicação com o Dialogflow ES;
- Enviar as mensagens do usuário;
- Receber as respostas do agente;
- Retornar o conteúdo da resposta para a interface do jogo.

As consultas são executadas em uma thread separada, evitando que a comunicação com o serviço externo bloqueie a interface do jogo enquanto uma resposta está sendo processada.

### Intenções implementadas

O assistente possui intenções (*intents*) configuradas para reconhecer diferentes tipos de perguntas:

| Intenção | Finalidade |
|---|---|
| Saudacao | Responder a cumprimentos |
| RegrasDoJogo | Explicar as regras do Snake |
| ExplicarQLearning | Apresentar o funcionamento do Q-Learning |
| SistemaDeRecompensas | Explicar as recompensas e punições da IA |
| ModosDeJogo | Informar os modos de execução disponíveis |
| ParametrosQLearning | Explicar os parâmetros utilizados no treinamento |

A integração utiliza uma chave de credenciais armazenada localmente, fora do repositório. Dessa forma, informações sensíveis não precisam ser incluídas nos arquivos versionados do projeto.

## Arquitetura do aprendizado

O funcionamento do agente segue este ciclo:

1. O jogo fornece o estado atual;
2. O agente analisa as informações;
3. O agente escolhe uma ação;
4. A cobra executa o movimento;
5. O jogo fornece uma recompensa;
6. O agente atualiza sua tabela Q;
7. O processo se repete até o encerramento da partida.

## Diário de desenvolvimento

### Etapa 1 — Refatoração da movimentação

Foi iniciado o processo de preparação do jogo para receber uma Inteligência Artificial.

Foram criadas constantes para representar as direções:

- CIMA;
- DIREITA;
- BAIXO;
- ESQUERDA.

Também foi criada a função `mover_cobra()` para separar a decisão da direção da execução do movimento.

### Etapa 2 — Representação do estado

Foi desenvolvida a função `obter_estado()`, responsável por transformar as informações do jogo em um conjunto de 11 características booleanas.

Essa representação permite que o agente interprete os perigos ao redor da cobra e a posição da comida.

### Etapa 3 — Implementação do Q-Learning

Foi criada a classe `AgenteQLearning`, responsável por:

- Armazenar os valores Q;
- Escolher ações;
- Explorar novas possibilidades;
- Utilizar experiências anteriores;
- Atualizar os valores da tabela Q;
- Reduzir gradualmente a exploração por meio do Epsilon.

### Etapa 4 — Sistema de recompensas

Foram implementadas recompensas positivas e negativas para orientar o aprendizado do agente.

Comer comida gera uma recompensa positiva, enquanto morrer gera uma punição. Movimentos normais recebem uma pequena penalidade para incentivar decisões mais eficientes.

### Etapa 5 — Modos de treinamento e estatísticas

Foram implementados os modos de treinamento automático e acelerado.

Também foi criado um sistema de registro de estatísticas para acompanhar o desempenho do agente ao longo dos episódios.

### Etapa 6 — Integração do assistente virtual

Foi implementada a integração com o Dialogflow ES, permitindo que o usuário converse com um assistente virtual diretamente pela interface do jogo.

Foi criado o arquivo `chatbot.py` para realizar a comunicação com o serviço e o arquivo `teste_chatbot.py` para testar as respostas independentemente da interface gráfica.

Posteriormente, o assistente foi integrado ao menu principal do Pygame, com uma tela própria para envio e visualização de mensagens.

Também foi implementada a execução assíncrona das consultas, permitindo que o jogo continue responsivo enquanto aguarda as respostas do Dialogflow.

## Próximos passos

- Implementar um modo de avaliação sem exploração, utilizando Epsilon igual a zero;
- Comparar o desempenho da IA antes e depois do treinamento;
- Analisar a evolução das pontuações;
- Avaliar possíveis melhorias na representação do estado e no sistema de recompensas;
- Documentar os resultados dos experimentos;
- Expandir as intenções e as respostas do assistente virtual.

---

**Status do projeto:** implementação inicial do Q-Learning concluída e assistente virtual integrado ao jogo. O projeto está na fase de treinamento, avaliação e aprimoramento do agente.