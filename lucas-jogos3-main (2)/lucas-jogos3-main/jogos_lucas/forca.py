import random as rd

def  mensagem_inicial():
    print("-------------------------------")
    print("\nBem vindo ao jogo da forca!\n")
    print("-------------------------------")

def selec_palavra_aletor():

    arquivo = open("palavra.txt", "r")
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()
    posicao = rd.randrange(0,len(palavra))
    palavra_secreta =palavra[posicao]
    return palavra_secreta

def letras_corretas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def entrada_dados():
    chute = input("Escreva uma letra: ")
    chute = chute.strip().lower()
    return chute


def chute_correto(palavra_secreta,chute,letras_acertadas):
    index = 0
    
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
            index += 1
def jogar_forca():
    mensagem_inicial()
    palavra_secreta = selec_palavra_aletor()

    letras_acertadas = letras_corretas(palavra_secreta)

    perdeu = False
    acertou = False
    erros = 0

    #Enquanto não acertar a palavra secreta
    while not perdeu and not acertou:
        chute = entrada_dados()
        #index define a posição da letra
        
        if chute in palavra_secreta:
           chute_correto(palavra_secreta,chute,letras_acertadas)
        else:
            erros += 1

        perdeu = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

if(__name__ == "__main__"):
    jogar_forca()