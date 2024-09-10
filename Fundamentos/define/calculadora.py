def calculadora(numero,segundo,operação):

    if operação == "soma":
        resultado = numero + segundo
        return resultado
    elif operação == "subtracao":
        resultado = numero - segundo
        return  resultado
    elif operação == "divisao":
        resultado = numero / segundo
        return resultado
    elif operação == "multiplicacao":
        resultado = numero * segundo
        return resultado

print("Ola sou uma calculadora")

primeiro = float(input("Digite o primeiro numero: "))
segundo = float(input("Digite o segundo numero: "))
operacao = input("Digite a operação (digite em letra minuscula e sem acento): ")

print(f"O resultado foi {calculadora(primeiro,segundo,operacao)}")