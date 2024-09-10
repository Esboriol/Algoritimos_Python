def alterar(c, f, opcao):
    if opcao == "celsius":
        resultado = (c * 1.8) + 32
        return resultado
    elif opcao == "fahrenheit":
        resultado = (f - 32) / 1.8
        return resultado

opcao = input("Você deseja transformar celsius ou fahrenheit: ").strip().lower()
numero = float(input("Digite a temperatura: "))

if opcao == "fahrenheit":
    print(f"A conversão para celsius foi de {alterar(0, numero, opcao)}º C")
elif opcao == "celsius":
    print(f"A conversão para fahrenheit foi de {alterar(numero, 0, opcao)} F°")
