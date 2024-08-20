def valor(a, b):
    parcela = a / b
    return parcela

print("Irei financiar uma casa")

preco = float(input("Digite o valor da casa: "))

pres = float(input("Digite em quantas vezes voce ira parcelar: "))

salario = float(input("Digite o seu salario: "))

porcentagem = salario / 100 * 35

entrada = input("Voce ira dar alguma entrada no imovel[S/N]")

if entrada == "S":
    fds = float(input("Digite o valor: "))
    preco = preco - fds
else:
    print("Ok")

while True:
    if pres == 1:
        print(f"Voce ira pagar {preco:.2f}")
        break
    elif pres >= 2:
        palmeiras = valor(preco, pres)
        if palmeiras > porcentagem:
            print("Voce nao ira conseguir compra fazer oq :/")
            break
        print(f"Voce ira pagar {palmeiras:.2f} reais")
        break