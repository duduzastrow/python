def jogar():
    print("*****************************")
    print("Bem-Vindo ao Jogo da Forca!!!")
    print("*****************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]


    enforcou = False
    acertou = False
    erros = erros == 12

    print(letras_acertadas)

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute=chute.strip().upper()

        if(chute in palavra_secreta):
            index=0
            for letra in palavra_secreta:
                    if(chute == letra):
                        letras_acertadas[index] = letra
                        print("Encontrei a letra {} na posição {}".format(letra, index))
                    index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print("Você ganhou!!!")
        else:
            print("Você perdeu!!!")

        print("jogando...")

    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar()