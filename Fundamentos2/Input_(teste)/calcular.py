
print(f"Ola eu sou um calculador de numeros")

operação = input("Digite qual operação você deseja (somar, subtrair, dividir, mutiplicar): ")

while True:
    try:
        numero = float(input("Digite o primeiro numero: "))
        break
    except ValueError:
        print("Aparentemente você não sabe oq é um numero kk")

while True:
    try:
        numero_2 = float(input("Digite o primeiro numero: "))
        break
    except ValueError:
        print("Aparentemente você não sabe oq é um numero kk")

resultado = 0

if (operação == "somar"):
    resultado = numero + numero_2
elif (operação == "subtrair"):
    resultado = numero - numero_2
elif (operação == "dividir"):
    resultado = numero / numero_2
elif (operação == "mutiplicar"):
    resultado = numero * numero_2


print(f"O resultado da sua conta sera {resultado:.2f}")