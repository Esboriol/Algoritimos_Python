
escolha = input("Voce ira converter minutos ou horas? ")
segundos = 0

if escolha == "minutos":
    troca = int(input("Digite o tempo em minutos: "))

    segundos = troca * 60

elif escolha == "horas":
    troca = int(input("Digite o tempo em horas: "))

    mapa = troca * 60
    segundos = mapa * 60

print(f"{segundos:.2f}")