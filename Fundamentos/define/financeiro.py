def verificação (par,valor,dinheiro):

    total = valor / par
    trin = dinheiro / 100 * 30

    if total > trin:
        print("Voce não ira conseguir comprar o imovel")
    elif total < trin:
        print("Voce consegue comprar o imovel")

valor = float(input("Digite o valor do imovel: "))
parcela = int(input("Digite o valor da parcela: "))
salario = float(input("Digite o seu salario: "))

verificação(parcela,valor,salario)