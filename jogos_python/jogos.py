import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    while(True):

        print("\n(1) Forca (2) Adivinhação (3) Encerrar")

        jogo = int(input("\nQual jogo deseja jogar? "))

        if(jogo == 1):
            print("\nJogando forca")
            forca.jogar()
        elif(jogo == 2):
            print("\nJogando adivinhação")
            adivinhacao.jogar()
        elif(jogo >= 3 or jogo < 1):
            print("\nMuito obrigado por jogar!")
            break

if(__name__ == "__main__"):
    escolhe_jogo()
