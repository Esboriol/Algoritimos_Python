
print(f"Ola, sou um convertor de temperatura")

escolha = input("Digite se voce deseja escolher Graus ou Fahrenheit: ")

if (escolha == "Graus"):
    Graus = float(input("Digite a temperatura:"))

    transformar = (Graus * 9/5) + 32

    print(f"A temperatura em Fahrenheit sera {transformar:.2f}")
elif (escolha == "Fahrenheit"):
    fahrenheit = float(input("Digite a temperatura: "))

    transformar = (fahrenheit - 32) * (5/9)

    print(f"A temperatura em Graus sera {transformar:.2f}")