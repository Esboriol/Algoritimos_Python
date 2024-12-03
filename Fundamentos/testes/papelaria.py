
produto = []

caderno = ["Azul grande", "Preto medio", "Vermelho piqueno"]
caneta = ["Caneta azul", "Caneta Preta", "Caneta vermelha"]
lapizera = ["Lapireza azul 0.7", "Lapizera preta 0.5", "Lapizera branca 2.0"]

valor_caderno = [100, 50, 30]
valor_caneta = [5, 5, 5]
valor_lapizera =[10, 9.50, 12]

print("Hola seja bem vindo a papelaria perebas")

while True:
    escolha = input("Voce gostaria de ir na seção de caderno, caneta ou lapizara: ")
    certo = escolha.lower()

    if certo == 'caderno':
        cade = int(input("Coloque o numero equivalente ao produto\n 1 para Caderno Azul Grande - R$100\n 2 para Caderno Preto Medio - R$50\n 3 para Caderno Vermelho Pequeno - R$30: "))

        cade -=1
        produto.append(valor_caderno[cade])
    elif certo == 'caneta':
        cade = int(input("Coloque o numero equivalente ao produto\n 1 para Caneta Azul - R$5\n 2 para Caneta Preta - R$5\n 3 para Caneta vermelha - R$5: "))

        cade -= 1
        produto.append(valor_caneta[cade])
    elif certo == 'lapizera':
        cade = int(input("Coloque o numero equivalente ao produto\n 1 para Lapizera Azul 0.7 - R$10\n 2 para Lapizera Preta 0.5 R$9.50\n 3 para Lapizera Branca 2.0 - R$12: "))

        cade -= 1
        produto.append(valor_lapizera[cade])

    conti = input("Voce gostaria de comprar outro produto: ")
    continuar = conti.lower()

    if continuar == 'sim':
        print("Ok voltando")
    elif continuar == 'nao' or continuar == 'não':
        break

total = 0

for i in range (len(produto)):
    total += produto[i]

if total >= 100:
    desconto = total - (total * 0.055)
    print(f"O total sera R${desconto:.2f}")
elif total < 100:
    print(f"O total sera de R${total:.2f}")