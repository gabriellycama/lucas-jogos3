
    import main
    import forca 
    


    print("(1) main (2)forca")

    opcao_jogo = int(input('escolha seu jogo'))
        if(opcao_jogo == 1):
        print("escolhendo adivinhacao")
        main.jogar_main()
        elif(opcao_jogo == 2):
            print("ESCOLHENDO FORCA")
            forca.jogar_forca()