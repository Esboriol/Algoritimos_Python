print("Ola iremos ver se voce pode tomar sorvete hoje")

dinheiro = float(input("Digite quanto de dinheiro voce tem: "))

tempo = input("Digite positivo se tiver sol e negativo se nao tiver: ")

sol = True

if tempo == "positivo":
    sol = True
elif tempo == "negativo":
    sol = False

dia = input("Digite o dia da semana: ")

if dinheiro >= 10 and sol == True and dia == "sabado" or dia == "domingo" and dinheiro >= 10 and sol == True:
    print("Voce pode ir tomar sorvete com seu amigo 😜")
else:
    print("Voce nao pode tomar sorvete com seu amigo")