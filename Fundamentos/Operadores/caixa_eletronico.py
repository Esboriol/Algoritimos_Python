import sys

Saldo = 2500

while True:

    print("Hola sou um caixa eletronico")

    print("\nAgora digite 1 para sacar, 2 para depositar, 3 para consultar e 4 para sair:")

    escolha = input("Coloque a resposta a seguir: ")

    if escolha < "1":
        print("Puts voce errou kk")
        sys.exit()
    elif escolha == "1":
        Saque = float(input(f"Digite a quantidade que deseja (Voce tem um saldo de {Saldo:.2f}: "))

        Saldo = Saldo - Saque

        print(f"Voce sacou {Saque:.2f} reais")

    elif escolha == "2":
        Deposito = float(input("Digite o quanto deseja depositar na sua conta: "))

        Saldo = Saldo + Deposito

        print(f"A sua conta esta agora com {Saldo:.2f} reais")

    elif escolha == "3":
        print(f"O seu saldo total é de {Saldo:.2f} reais")

    elif escolha == "4":
        print("Espero que tenha um bom dia ate mais :)")
        break
    elif escolha >= "5":
        print("Burro kk")