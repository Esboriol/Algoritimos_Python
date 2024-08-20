
Total = 5623.90

def conta(Total, Procentagem):
    Valor_total = Total / 100 * Procentagem
    print(f"O valor que voce recebera sera de {Valor_total:.2f}")

print("Qual do vencedores voce foi: 1, 2 e 3")

baba = input("Digite sua colocação: ")

if baba == "1":
    conta(Total, 44)
elif baba == "2":
    conta(Total, 36)
elif baba == "3":
    conta(Total, 20)