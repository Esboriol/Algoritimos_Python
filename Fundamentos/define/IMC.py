def calculo(peso,altura):

    resultado = peso / (altura * altura)
    return resultado

altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

IMC = calculo(peso,altura)

if IMC < 18.5:
    print("Baixo peso")
elif IMC > 18.5 and IMC < 24.9:
    print("Peso normal")
elif IMC > 25.0 and IMC < 29.9:
    print("Sobrepeso")
elif IMC > 30.0 and IMC < 34.9:
    print("Obesidade grau I")
elif IMC > 35.0 and IMC < 39.9:
    print("Obesidade grau II")
elif IMC > 39.9:
    print("Obesidade grau III")