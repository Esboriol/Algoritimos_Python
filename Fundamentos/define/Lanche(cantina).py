def desconto(valor, desconto):
    des = (valor / 100) * desconto
    return valor - des

total = 0.0

print("Seja bem-vindo a lanchonete do sesi")

escolha = True

while escolha:
    produto = input("Qual produto você deseja (Lanche e Bebida): ").lower()

    if produto == "lanche":
        print("Ok, esses são os lanches/pratos disponíveis")
        print("Coxinha: R$9,90\nPrato de comida: R$20")  # Corrigido "/n" para "\n"
        lanche = input("Digite qual lanche você deseja: ").lower()

        if lanche == "coxinha feliz":
            total += 9.90
        elif lanche == "prato de comida":
            total += 20
        else:
            print("Ops, parece que algo deu errado. Tente novamente.")
            continue  # Corrigido para "continue" em vez de "break" para reiniciar o loop

    elif produto == "bebida":
        print("Ok, essas são as nossas bebidas")
        print("Coca Cola: R$7,99\nSuco: R$4,99")  # Corrigido "/n" para "\n"
        bebida = input("Digite a bebida desejada: ").lower()

        if bebida == "coca cola":
            total += 7.99
        elif bebida == "suco":
            total += 4.99
        else:
            print("Parece que algo deu errado. Tente novamente.")
            continue  # Corrigido para "continue" em vez de "break" para reiniciar o loop

    else:
        print("Produto não reconhecido. Tente novamente.")
        continue  # Corrigido para "continue" em vez de "break" para reiniciar o loop

    continuar = input("Digite 'sim' se você quiser selecionar outro item e 'não' para finalizar a compra: ").lower()

    if continuar == "não":
        escolha = False
    elif continuar == "sim":
        print("Ok, irei colocá-lo de volta na seleção")
    else:
        print("Resposta inválida. Finalizando a compra.")
        break  # Adicionado para tratar respostas inválidas e finalizar a compra

print(f"O total da sua conta foi R${total:.2f}")

cupom = input("Digite 'sim' se você tiver algum cupom de desconto: ").lower()

if cupom == "sim":
    tipo = input("Digite o cupom: ").upper()  # Corrigido para manter a consistência com os códigos de cupom fornecidos

    if tipo == "DEV_SESI":
        total = desconto(total, 5)
    elif tipo == "ELE_SESI":
        total = desconto(total, 8)
    else:
        print("Cupom inválido.")

    print(f"O total será R${total:.2f}")

print("Tenha um ótimo dia 😀")
