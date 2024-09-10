def calcular_litros_agua(idade):
    if idade <= 10:
        return 18
    elif 11 <= idade <= 18:
        return 30
    elif 19 <= idade <= 25:
        return 42
    else:
        return 24

def calcular_despesa(total_litros_agua):
    return total_litros_agua * 0.60


print("Olá, sou um calculador de conta de água")
pessoas = int(input("Digite quantas pessoas tem na sua casa: "))

total_litros_agua = 0

for i in range(pessoas):
    idade = float(input(f"Digite a idade da {i+1}ª pessoa: "))
    total_litros_agua += calcular_litros_agua(idade)

print(f"O total gasto de litros foi de {total_litros_agua:.2f}")

dinheiro = calcular_despesa(total_litros_agua)

print(f"E o total gasto em dinheiro será de R$ {dinheiro:.2f}")