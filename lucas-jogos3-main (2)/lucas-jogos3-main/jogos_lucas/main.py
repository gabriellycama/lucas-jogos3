import random as rd 

def jogar_adivinhacao():
    print("-------------------------------")
    print("Bem vindo ao jogo da prestigitação!3")
    print("-------------------------------")
    #definicao das variaveis
    n_secreto = rd.randrange(1, 101)

    n_tentativas = 5 
    rodada = 1
    for rodada  in range(1, n_tentativas + 1):
        print(f"tentativa {rodada}de {n_tentativas}")
        entrada = int(input("digite um numero entre 1 e 100: "))
        acertou = entrada == n_secreto
        entrada_maior = entrada > n_secreto
        entrada_menor = entrada < n_secreto

        if(entrada > 100 or entrada <1):
            
            print ("valo nao compativel")
            continue
        
        print(f"Você digitou o número: {entrada}")

        if(acertou):
            
            print("Parabéns, você acertou o número secreto")
            break
        else:
            if(entrada_maior):
                print("Você errou! O número digitado foi maior que o secreto")
            if(entrada_menor):
                print("Você errou! O número digitado foi menor que o secreto")
        rodada = rodada +1
    
    print("Fim de jogo") 