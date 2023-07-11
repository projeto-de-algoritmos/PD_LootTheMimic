# PD_LootTheMimic

**Número da Lista**: 29<br>
**Conteúdo da Disciplina**: Programação Dinâmica<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0016563  |  Filipe Santana Machado |
| 18/0014412  |  Cainã Valença de Freitas |

## Sobre 
Este projeto implementa algoritmo que soluciona o problema de [Knapsack](https://en.wikipedia.org/wiki/Knapsack_problem) de forma dinâmica. É um método aprimorado de usar recursividade que ao invés de chamar uma função várias vezes ele, na primeira vez que é chamado, armazena o resultado para que cada vez que a função for chamada novamente volte o resultado e não uma requisição para ser resolvida.

Ele também é um jogo que testa o jogador na capacidade de escolher itens com peso que cabe na sua mochila. O jogador pode escolher um item e adiciona-lo a sua mochila, ao escolher um item errado que não cabe no melhor resultado possivel, ele é devorado e perde todos seus pontos. Ele pode sair mais cedo sem escolher todos os items possiveis, tendo assim que escolher entre continuar apostando ou não.

## Screenshots
![image](https://github.com/projeto-de-algoritmos/PD_LootTheMimic/assets/49414401/80809a20-ef3f-4b1f-aaea-1dc7bf0ae2f2)
![image](https://github.com/projeto-de-algoritmos/PD_LootTheMimic/assets/49414401/fc80f2d9-a6c9-4bed-a885-1ea49a6a76a1)



<br>

## Instalação 
**Linguagem**: Python<br>
**Framework**: Pygame<br>

#### Comando de instalação

A única dependência externa do projeto, além do python, é o pygame.
Na pasta raiz do repositório basta executar:

```sh
make install
```

ou

```sh
pip install -r requirements.txt
```

## Uso 

#### Execução

```sh
make run
```

ou

```sh
python -m src.game.main
```

#### Como jogar
Na tela do jogo irá aparecer uma lista de itens<br>
Em cada item você pode clicar no botão "add" para adiciona-lo a mochila<br>
No botão "submit" você pode clicar para terminar a rodada e sair com o que você ainda tem na mochila<br>
O botão de continue serve para continuar para a proxima rodada. <br>

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.
