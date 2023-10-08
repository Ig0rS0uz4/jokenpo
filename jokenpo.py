import random
inicio = input('Deseja iniciar o jogo? [S/N]: ')
eqp = ['pedra', 'papel', 'tesoura']
contadorJ1 = 0
contadorJ2 = 0
while inicio == 's':
    for x in range(3):
        j1 = input('PEDRA,   PAPEL  OU  TESOURA?\n'
                   'escolha: ')
        j2 = random.choice(eqp)

        if j1 == "pedra" and j2 == 'tesoura':
            contadorJ1 += 1
            print(f'|{j1}|x|{j2}| j1 venceu')
        elif j2 == 'pedra' and j1 == 'tesoura':
            contadorJ2 += 1
            print(f'|{j1}|x|{j2}| j2 venceu')
        elif j1 == 'tesoura' and j2 == 'papel':
            contadorJ1 += 1
            print(f'|{j1}|x|{j2}| j1 venceu')
        elif j2 == 'tesoura' and j1 == 'papel':
            contadorJ2 += 1
            print(f'|{j1}|x|{j2}| j2 venceu')
        elif j1 == 'papel' and j2 == 'pedra':
            contadorJ1 += 1
            print(f'|{j1}|x|{j2}| j1 venceu')
        elif j2 == 'papel' and j1 == 'pedra':
            contadorJ2 += 1
            print(f'|{j1}|x|{j2}| j2 venceu')
        else:
            contadorJ1 += 0
            contadorJ2 += 0
            print(f'|{j1}|x|{j2}| empate')
    if contadorJ1 > contadorJ2:
        print('Jogador 1 ganhou!')
    elif contadorJ2 > contadorJ1:
        print('Jogador 2 ganhou!')
    else:
        print('o jogo empatou!')
    inicio = input('Deseja reiniciar o jogo? [S/N]: ')
print(f'PONTUAÇÃO: J1[{contadorJ1}] X J2[{contadorJ2}]')