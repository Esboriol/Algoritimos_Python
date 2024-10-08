def valor_parcela(valor, parcelas):
    cada = valor / parcelas
    return cada


def adicional(valor, parcelas):
    adicional = (valor / parcelas) + (valor * 1.05)
    return adicional


def juros(valor, juro):
    jur = (valor / 100) * juro
    return jur


mes = 0
dia = 12
ano = 2024

print("Seja bem-vindo! Irei ajudá-lo a calcular o financiamento do seu veículo/imóvel.")

escolha = input("Primeiro, gostaria de saber se você está escolhendo um imóvel ou veículo: ")

while escolha != "imovel" and escolha != "veiculo":
    escolha = input("Parece que você digitou a escolha errada. Tente novamente: ")

print("Guardando informação...")
print("Carregando perguntas...")

if escolha == "veiculo":
    renda = float(input("Primeiro, digite a sua renda: "))

    valor = float(input("Digite o valor do veículo: "))

    anos = int(input("Digite quantos anos irá pagar o veículo (até 20 anos): "))

    while anos > 20 or anos <= 0:
        anos = int(input("Você passou ou digitou um número errado. Por favor, digite novamente: "))

    parcelas = anos * 12
    meio = valor_parcela(valor, parcelas)

    idade = int(input("Digite a idade do carro (se for 0 Km, digite 0): "))
    if idade >= 24:
        juro = 2.5
        juros_total = juros(meio, juro)
    elif idade < 24 and idade > 0:
        juro = 1.9
        juros_total = juros(meio, juro)
    elif idade <= 0:
        juro = 0.5
        juros_total = juros(meio, juro)

    valor_total = meio + juros_total

elif escolha == "imovel":
    renda = float(input("Primeiro, digite a sua renda: "))

    valor = float(input("Digite o valor do imóvel: "))

    anos = int(input("Digite quantos anos irá pagar o imóvel (até 35 anos): "))

    while anos > 35 or anos <= 0:
        anos = int(input("Você passou ou digitou um número errado. Por favor, digite novamente: "))

    parcelas = anos * 12
    valor_total = valor_parcela(valor, parcelas)

valor_adicional = adicional(valor, parcelas)

if valor_total > (renda / 100) * 30:
    print("Ops, parece que você passou do limite da sua renda.")
    print("Não será possível continuar.")
    quit()

if escolha == "imovel":
    financiamento = input(
        "Digite 'sim' se você quiser pagar o adicional na décima parcela e 'não' para pagar em cada parcela: ")

    while financiamento != "sim" and financiamento != "nao":
        financiamento = input("Parece que você digitou errado. Tente novamente: ")

    if financiamento == "sim":
        for i in range(1, parcelas + 1):
            mes += 1

            if mes > 12:
                mes = 1
                ano += 1

            if i == 10:
                valor_total10 = valor_total + valor_adicional
                print(f"Parcela: data de pagamento:  Valor: \n{i}       {dia}/{mes}/{ano}          {valor_total10:.2f}")
            elif i > 10:
                print(f"Parcela: data de pagamento:  Valor: \n{i}       {dia}/{mes}/{ano}          {valor_total:.2f}")
            else:
                print(f"Parcela: data de pagamento:  Valor: \n{i}        {dia}/{mes}/{ano}           {valor_total:.2f}")
    elif financiamento == "nao":
        for i in range(1, parcelas + 1):
            mes += 1
            valor_adicional = valor_adicional / parcelas
            valor_total = valor_total + valor_adicional

            if mes > 12:
                mes = 1
                ano += 1
            if i < 10:
                print(f"Parcela: data de pagamento:  Valor: \n{i}        {dia}/{mes}/{ano}           {valor_total:.2f}")
            elif i >= 10:
                print(f"Parcela: data de pagamento:  Valor: \n{i}       {dia}/{mes}/{ano}          {valor_total:.2f}")

elif escolha == "veiculo":
    for i in range(1, parcelas + 1):
        mes += 1

        if mes > 12:
            mes = 1
            ano += 1
        if i < 10:
            print(f"Parcela: data de pagamento:  Valor: \n{i}        {dia}/{mes}/{ano}           {valor_total:.2f}")
        elif i >= 10:
            print(f"Parcela: data de pagamento:  Valor: \n{i}       {dia}/{mes}/{ano}          {valor_total:.2f}")
