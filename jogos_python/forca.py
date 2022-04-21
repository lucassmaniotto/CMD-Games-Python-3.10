import random

def mensagemIncial():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print("**Seu julgamento será iniciado!**")
    print("*********************************")

def selecionaPalavraSecreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def adicionaLetrasAcertadas(palavra):
    return ['_' for letra in palavra]

def tentativaChute():
    chute = input('Digite sua letra: ')
    chute = chute.strip().upper()

    return chute

def chuteCorreto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def desenhaForca(erros):
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

def imprimeVencedor():
    print("A cidade reconhece sua inocência e lhe parabeniza!")
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
    print("\nVocê sobreviveu e ganhou um troféu brilhante :O")

def imprimePerdedor(palavra_secreta):
    print("A cidade o julgou culpado!")
    print(f"A palavra era {palavra_secreta}")
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
    print("\nVocê foi enforcado :(")

def jogar():

    mensagemIncial()
    palavra_secreta = selecionaPalavraSecreta()
    letras_acertadas = adicionaLetrasAcertadas(palavra_secreta)
    print(letras_acertadas, "\n")

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        
        chute = tentativaChute()
        
        if (chute in palavra_secreta):
            chuteCorreto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenhaForca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas, "\n")

    if acertou:
        imprimeVencedor()
    else:
        imprimePerdedor(palavra_secreta)

if(__name__ == "__main__"):
    jogar()
