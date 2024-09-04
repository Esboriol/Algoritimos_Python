print("Hola irei calcular o numero pares para voce")

numero = float(input("Digite o numero escolhido: "))

soma = 0

while numero > 0:

    if numero % 2 == 0:

        soma += numero
    numero -= 1

print(soma)