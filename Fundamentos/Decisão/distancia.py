def valor(e, s):
    total = e * s
    print(f"O valor a ser pago sera de {total:.2f}")

distancia = float(input("Digite a distancia em Km: "))

if distancia > 200:
    valor(distancia, 0.45)
else:
    valor(distancia, 0.50)