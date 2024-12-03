
restaurante = ['Mc Donald', 'Claudinhos', 'Trevisan']

cardapio_almoco_mc = ['Big Mac', 'Mc Chiken', 'Mc Quarteirão', 'Mc Lanche Feliz']

cardapio_almoco_preco_mc = [16.99, 15.99, 19.99, 9.99]

cardapio_refri_mc = ['Coca cola', 'Sprite', 'Suco de laranja']

cardapio_refri_preco_mc = [12.99, 11.99, 14.99]

cardapio_sobremesa_mc = ['Casquinha', 'Mc Colosso', 'Tortinha']

cardapio_sobremesa_preco_mc = [3.90, 9.99, 7.99]

pedidos = []
pedidos_preco = []

print("Seja bem vindo ao ipobre")
print("Temos desconto de 25% por pedidos com mais ou de 3 produtos")

escolha = input(f"Temos esses restaurantes: {', '.join(restaurante)}. Digite qual você deseja: ")

ha = escolha.lower()
while True:
    if ha == 'mc donald':
        tipo = input("Digite sim para um lanche com bebida e não para um lanche sem bebida: ")

        if tipo == "sim":
            print("Ok, carregando...")

            lanche = int(input("Digite o numero equivalente para o lanche\n 1 para Big Mac -R$16,99 \n 2 para Mc chiken - R$15,99\n 3 para MC Quarteirão - 19,99\n 4 para Mc Lanche Feliz - 9,99: "))

            lanche -= 1

            pedidos.append((cardapio_almoco_mc[lanche]))
            pedidos_preco.append(cardapio_almoco_preco_mc[lanche])

            bebida = int(input("Agora irei mostrar as bebidas\n 1 para Coca Cola - R$12,99\n 2 para Sprite - R$11,99 \n 3 para Suco de Laranja - 14,99: "))

            bebida -= 1

            pedidos.append(cardapio_refri_mc[bebida])
            pedidos_preco.append(cardapio_refri_preco_mc[bebida])

        elif tipo == 'não' or 'nao':
            print("Ok, carregando...")

            lanche = int(input(
                "Digite o numero equivalente para o lanche\n 1 para Big Mac -R$16.99 \n 2 para Mc chiken - R$15.99\n 3 para MC Quarteirão - 19.99\n 4 para Mc Lanche Feliz - 9.99: "))

            lanche -= 1

            pedidos.append((cardapio_almoco_mc[lanche]))
            pedidos_preco.append(cardapio_almoco_preco_mc[lanche])

        sobres = input("Voce gostaria de uma sobremesa: ")

        if sobres == 'sim':

            sobremesa = int(input("Digite o numero correspondente para a sobremesa\n 1 para Casquinha - R$3,90\n 2 para Mc Colosso - R$9,99\n 3 para Tortinha - R$7,99: "))

            sobremesa -= 1
            pedidos.append(cardapio_sobremesa_mc[sobremesa])
            pedidos_preco.append(cardapio_sobremesa_preco_mc[sobremesa])

        elif sobres == 'nao':
            print("Ok")

        continuar = input("Voce quer fazer outra compra? ")

        conti = continuar.lower()

        if conti == 'sim':
            print("ok")
        elif conti == 'não' or conti == 'nao':
            break

total = 0
for i in  range(len(pedidos_preco)):
    total += pedidos_preco[i]

if len(pedidos) >= 3:

    desconto = total - (total * 0.25)
    print(f"O valor total com desconto sera de R${desconto:.2f}")
else:
    print(f"O valor total da sua compra foi de R${total:.2f}")