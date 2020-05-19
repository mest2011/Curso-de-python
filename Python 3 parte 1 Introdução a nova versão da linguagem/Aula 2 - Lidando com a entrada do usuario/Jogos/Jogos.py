import Adivinhacao
import Forca

def escolher_jogo():
    print('*******************************')
    print('********Escolha um jogo!*******')
    print('*******************************')

    print('(1) Forca (2) Advinhação')
    jogo = int(input('Qual jogo deseja jogar?\n'))

    if(jogo == 1):
        Forca.jogar()
    elif(jogo == 2):
        Adivinhacao.jogar()

if(__name__ == '__main__'):
    escolher_jogo()