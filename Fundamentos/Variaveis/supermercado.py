
vezes = int(input("Ola quantos produtos voce ira calcular? "))
soma = 0

for i in range(vezes):
    valor = float(input("Digite o preço do produto: "))

    soma +=valor

print(f"O total sera de {soma:.2f} reais")