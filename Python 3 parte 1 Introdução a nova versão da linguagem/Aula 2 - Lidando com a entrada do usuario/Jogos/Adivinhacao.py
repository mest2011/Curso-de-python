import random

def jogar():
    print('*******************************')
    print('Bem vindo ao jogo de adinhação!')
    print('*******************************')

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade você deseja?')
    nivel = input('(1) Facíl (2) Médio (3) Difícil \n')

    if(nivel == "1"):
        total_tentativas = 20
    elif(nivel == "2"):
        total_tentativas = 10
    else:
        total_tentativas = 5


    #rodada = 1

    for rodada in range(1, total_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_tentativas))
        digitado = input('Digite um número entre 1 e 100: ')

        numero_digitado = int(digitado)

        if(numero_digitado < 1 or numero_digitado > 100):
            print('Você digitou um número inválido, o número deve estar entre 1 e 100!')
            continue

        acertou     = numero_secreto == numero_digitado
        chute_maior = numero_secreto <  numero_digitado
        chute_menor = numero_secreto >  numero_digitado

        if(acertou):
            print('Parabéns você acertou o número!')
            print(f'Você fez um total de {pontos} pontos!')
            break
        else:
            if(chute_maior):
                print('Que pena você errou o número! O seu chute foi MAIOR que o número secreto!')
            elif(chute_menor):
                print('Que pena você errou o número! O seu chute foi MENOR que o número secreto!')
        #rodada += 1
        pontos_perdidos = round(abs(numero_secreto - numero_digitado) / 3)
        pontos = pontos - pontos_perdidos

    print(f'O número secreto era {numero_secreto}')
    print('Fim de Jogo!')

if (__name__ == '__main__'):
    jogar()