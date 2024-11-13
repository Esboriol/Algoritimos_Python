
numeros = [10, 29, 69, 13]

multiplicador = float(input("Digite o numero que ira multiplicar a lista: "))

lista = []
for i in numeros:
    casa = i * multiplicador
    lista.append(casa)

print(lista)