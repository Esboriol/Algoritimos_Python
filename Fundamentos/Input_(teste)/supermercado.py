marmita = True

total = 0



while marmita:

    conta = 0

    print(f"Ola seja bem vindo ao nosso Supermercado")

    Tipo = input(f"Selecione qual setor voce quer (carne, fruta, doce): ")

    carne = ""
    fruta = ""
    doce = ""

    if (Tipo == "carne"):
        carne = input("Digite qual tipo de carne voce deseja \n Bife = R$20 \n Frango = R$15 \n Costela = R$40 \n")
        if (carne == "Bife"):
            conta += 20
        elif (carne == "Frango"):
            conta += 15
        elif (carne == "Costela"):
            conta += 40
    elif (Tipo == "fruta"):
        fruta = input("Digite qual tipo de fruta voce deseja \n Banana = R$5 \n Maça = R$7 \n Melancia = R$10")
        if (fruta == "Banana"):
            conta += 5
        elif (fruta == "Maça"):
            conta += 7
        elif (fruta == "Melancia"):
            conta += 10
    elif (Tipo == "doce"):
        doce = input("Digite qual tipo de doce voce deseja \n Brigadeiro = R$7,50 \n Bolo = R$15 \n Sorvete = R$20")
        if (doce == "Brigadeiro"):
            conta += 7.50
        elif (doce == "Bolo"):
            conta += 15
        elif (doce == "Sorvete"):
            conta += 20

    compra = input(f"Voce deseja continuar comprando? [S/N]")

    total += conta

    if (compra == "N"):
        marmita = False

desconto = int(input("Digite o desconto: "))

pato = desconto / 100
n_sei = total * pato
verdade = total - n_sei

print(f"O total da sua compra foi R${verdade:.2f}")