print("Iremos calcular o seu novo aumento")

salario = float(input("Digite o seu salario atual: "))
aumento = float(input("Digite o quanto irá receber de aumento (em porcentagem): "))

GG = (salario * aumento / 100)
total = GG + salario

if GG >= 750:
    print(f"Você recebeu um aumento significativo e agora está com o salário de {total:.2f} reais.")
elif GG >= 350:
    print(f"Você recebeu um aumento decente e agora está com o salário de {total:.2f} reais.")
elif GG >= 100:
    print(f"Você recebeu um aumento pequeno e agora está com o salário de {total:.2f} reais.")
else:
    print(f"Seu aumento foi menor e agora seu salário é de {total:.2f} reais.")
