def hah (tempo,valor,risco):

    investimento = ""
    rentabilidade = 0

    if risco == "baixo":
        investimento = "AZ"

        if tempo == 24:
            rentabilidade = (valor / 100) * 0.5 * tempo
        elif tempo == 60:
            rentabilidade = (valor / 100) * 0.8 * tempo
        elif tempo == 120:
            rentabilidade = (valor / 100) * 1.2 * tempo

    elif risco == "medio":
        investimento = "Crypto"

        if tempo == 24:
            rentabilidade = (valor / 100) * 1.1 * tempo
        elif tempo == 60:
            rentabilidade = (valor / 100) * 1.5 * tempo
        elif tempo == 120:
            rentabilidade = (valor / 100) * 1.9 * tempo

    elif risco == "alto":
        investimento = "Bitcoin"

        if tempo == 24:
            rentabilidade = (valor / 100) * 2.1 * tempo
        elif tempo == 60:
            rentabilidade = (valor / 100) * 2.8 * tempo
        elif tempo == 120:
            rentabilidade = (valor / 100) * 3.9 * tempo

    print(f"Se voce escolher um risco {risco} com o tempo de {tempo} meses voce ira investir na empresa {investimento} e tera um retorno de R${rentabilidade}")

tempo = int(input("Escolha entre 24 meses, 60 meses, 120 meses: "))
risco = input("Escolha entre baixo risco, medio e alto: ")
dinheiro = float(input("Digite o valor em reais que voce ira investir: "))

hah(tempo,dinheiro,risco)