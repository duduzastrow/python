import forca
import main

def escolhe_jogo():
    print("*****************************")
    print("******Escolha seu Jogo!******")
    print("*****************************")


    print("(1) Forca   (2) Adivinhação")

    jogo = int(input("Qual jogo você quer jogar?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo de adivinhação")
        main.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()