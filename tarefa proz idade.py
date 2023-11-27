def aniversario():

    nome = input("Entre com o seu nome completo: ")

    while True:

        try:

            nascimento = int(input("Entre com o ano de seu nascimento: "))

            if nascimento < 1922 or nascimento > 2023:
                print("Entre com um ano entre 1922 e 2023")
                
            elif nascimento >= 1922 and nascimento<=2023:

                idade = 2023 - nascimento
                print(f"{nome} nasceu no ano de {nascimento} e completou/completará {idade} anos em 2023")
                break

        except:
            print("Entre com um número válido")
           
aniversario()