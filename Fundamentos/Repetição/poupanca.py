
def juros (numero, juros):
    total = (numero / 100) * juros
    return total

quantidade = 6

contador = 1

soma = 0

print("Ola iremos guardar dinheiro na sua poupança (6 vezes) porem ira ter uma taxa em juros de 5%")

while quantidade > 0:

    numero = float(input(f"Digite o {contador} numero: "))

    soma += numero

    quantidade -= 1
    contador += 1

print(f"O total foi {soma}")

print(f"A taxa sera de {juros(soma, 5)}")