def jogar_forca():
    print("-------------------------------")
    print("\nBem vindo ao jogo da forca!\n")
    print("-------------------------------")
  #lista = ["_ _ _ _ _ _ _ _ _ _ _"]
    arquivo = open("jogos_lucas/palavras.txt", "r")
    palavra = []

    for linha in palavra:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    palavra_secreta = "processador".lower()
    letras_acertadas = ["_" for letra in palavra_secreta]
    perdeu = False
    acertou = False
    erros = 0 
    while (not perdeu and not acertou):
        chute = input("Escreva uma letra: ")
        chute = chute.strip().lower()

        #index define a posição da letra
        index = 0
        
        if chute in palavra_secreta:

            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] =letra
                index += 1
        else:
            erros = erros + 1
        perdeu = erros == 6 
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
if(__name__ == "__main__"):
    jogar_forca()