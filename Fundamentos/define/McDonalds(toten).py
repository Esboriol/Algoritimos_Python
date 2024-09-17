def desconto(valor, desconto):
    des = (valor / 100) * desconto
    return valor - des

total = 0.0

print("Seja bem-vindo ao totem do Mec")

escolha = True

while escolha:
    produto = input("Qual produto você deseja (Sorvete, Lanche e Bebida): ").lower()

    if produto == "sorvete":
        print("Ok, escolha qual sorvete você prefere")
        print("Casquinha: R$5,99\nMilkshake: R$14,50")  # Corrigido "/n" para "\n"
        sorvete = input("Digite qual você prefere: ").lower()

        if sorvete == "casquinha":
            total += 5.99
        elif sorvete == "milkshake":
            total += 14.50
        else:
            print("Parece que algo deu errado. Tente outra vez.")
            continue  # Corrigido para "continue" em vez de "break" para reiniciar o loop

    elif produto == "lanche":
        print("Ok, esses são os lanches disponíveis")
        print("McLanche feliz: R$24,90\nMontanha: R$30")  # Corrigido "/n" para "\n"
        lanche = input("Digite qual lanche você deseja: ").lower()

        if lanche == "mclanche feliz":
            total += 24.90
        elif lanche == "montanha":
            total += 30
        else:
            print("Ops, parece que algo deu errado. Tente novamente.")
            continue  # Corrigido para "continue" em vez de "break" para reiniciar o loop

    elif produto == "bebida":
        print("Ok, essas são as nossas bebidas")
        print("Coca Cola: R$7,99\nPepsi: R$6,99")  # Corrigido "/n" para "\n"
        bebida = input("Digite a bebida desejada: ").lower()

        if bebida == "coca cola":
            total += 7.99
        elif bebida == "pepsi":
            total += 6.99
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

    if tipo == "ABC5F":
        total = desconto(total, 5)
    elif tipo == "WER2A":
        total = desconto(total, 8)
    elif tipo == "BNM9R":
        total = desconto(total, 10)
    elif tipo == "QDG8X":
        total = desconto(total, 18)
    else:
        print("Cupom inválido.")

    print(f"O total será R${total:.2f}")

print("Tenha um ótimo dia 😀")
