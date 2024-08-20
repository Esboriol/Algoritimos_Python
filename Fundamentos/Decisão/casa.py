print("Hola irei converter o seu dinheiro em reais para dolar")

quantia = float(input("Digite a quantia que sera tranferida em reais: "))

dolar = quantia / 5.16

if dolar >= 5000:
    taxa = dolar * 0.15
    total = taxa + dolar

    print(f"Voce teve uma taxa a pagar de {taxa:.2f} dolares pelo motivo de ter mais de 5k de dolares")
    print(f"Voce agora ira ter que pagar o total de {total:.2f} para receber o valor de {dolar:.2f}")
else:
    print(f"Voce recebera em dolar {dolar:.2f}")