import random





def jogar():
    imprime_abertura_jogo()

    palavra_secreta = gerar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0



    print(letras_acertadas)
    while(not enforcou and not acertou):

        chute = capturar_chute_jogador()


        if (chute in palavra_secreta):
            letras_acertadas = marca_letra_acertadas(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)


        print(letras_acertadas)

        acertou = "_" not in letras_acertadas
        enforcou = erros == 7

    if acertou:
        imprimir_acetou()
    else:
        imprimir_errou(palavra_secreta)

    print("Fim do jogo")

def desenha_forca(erros):
    print("Você errou, ainda restão {} tentativas!".format(7 - erros))
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprimir_errou(palavra_secreta):
    print('Você perdeu!')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print(f'A palavra era {palavra_secreta}!')

def imprimir_acetou():
    print('Parabens voce acertou a palavra!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def marca_letra_acertadas(palavra_secreta,chute,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = chute
        index += 1
    return letras_acertadas

def capturar_chute_jogador():
    chute = input('Digite uma letra: ')
    chute = chute.strip().upper()
    return chute

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def imprime_abertura_jogo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def gerar_palavra_secreta():
    frutas = open('Frutas.txt', 'r')
    lista_frutas = [fruta.strip() for fruta in frutas]
    palavra_secreta = lista_frutas[random.randrange(0, len(lista_frutas))].upper()
    return palavra_secreta

if(__name__ == "__main__"):
    jogar()
