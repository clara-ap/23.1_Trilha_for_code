# pedra, papel e tesoura melhor de 5
from random import choice

pontosDoJogador = 0 
pontosDoBot = 0 
rodada = 0

while rodada != 5:
    escolhaDoJogador = input('PEDRA, PAPEL OU TESOURA\nESCOLHA: ')
    escolhaDoJogador = escolhaDoJogador.lower()

    opcoes = ['pedra','papel','tesoura']

    escolhaDoBot = choice(opcoes)
    print(f'\nJOGADOR: {escolhaDoJogador}\nBOT: {escolhaDoBot}')

    if escolhaDoBot == escolhaDoJogador:
        pontosDoJogador += 1
        pontosDoBot += 1

    elif escolhaDoBot == 'pedra' and escolhaDoJogador == 'tesoura':
        pontosDoBot += 1

    elif escolhaDoBot == 'pedra' and escolhaDoJogador == 'papel':
        pontosDoJogador += 1

    elif escolhaDoBot == 'tesoura' and escolhaDoJogador == 'pedra':
        pontosDoJogador += 1

    elif escolhaDoBot == 'tesoura' and escolhaDoJogador == 'papel':
        pontosDoBot += 1

    elif escolhaDoBot == 'papel' and escolhaDoJogador == 'tesoura':
        pontosDoJogador += 1 

    elif escolhaDoBot == 'papel' and escolhaDoJogador == 'pedra':
        pontosDoBot += 1
    
    print(f'\n    JOGADOR    vs    BOT\n       {pontosDoJogador}              {pontosDoBot}\n')
    rodada += 1


if pontosDoBot > pontosDoJogador:
    print('VOCÊ PERDEU :(')
else: 
    print('VOCÊ GANHOU! ;)')
