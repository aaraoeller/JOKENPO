from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0,2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)

print('-=' * 11)

print('O Computador jogou {}'.format(itens[computador]))

print('O Jogador jogou {}'.format(itens[jogador]))

print('-=' * 11)

if computador == 0: # O computador jogou Pedra
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('O JOGADOR VENCEU')

    elif jogador == 2:
        print('O COMPUTADOR VENCEU')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: # O computador jogou Papel
    if jogador == 0:
        print('O COMPUTADOR VENCEU')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('O JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: # O computador jogou Tesoura
    if jogador == 0:
        print('O JOGADOR VENCEU')

    elif jogador == 1:
        print('O COMPUTADOR VENCEU')

    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')