print("Ola sou um calculador de conta de agua")
pessoas = int(input("Digite quantas pesssoas tem na sua casa: "))

idade = []

total_litros_agua = 0

for i in range(0, pessoas):
    legal = float(input(f"Digite a idade da {i+1}° pessoa: "))
    idade.append(legal)

    if idade [i] <= 10:
        total_litros_agua += 18
    elif idade [i] > 10 and idade [i] <= 18:
        total_litros_agua += 30
    elif idade [i] > 18 and idade [i] <=25:
        total_litros_agua += 42
    elif idade [i] > 26:
        total_litros_agua += 24

print(f"O total gasto de litros foi de {total_litros_agua:.2f}")

dinheiro = total_litros_agua * 0.60

print(f"E o total gasto em dinheiro sera de R$ {dinheiro:.2f}")