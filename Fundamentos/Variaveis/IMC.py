
peso = 80
altura = 1.70

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f"Voce esta magro com {imc:.2f}")
elif imc > 18.6 and imc < 24.9:
    print(f"Voce esta imc normal de {imc:.2f}")
elif imc > 25 and imc < 29.9:
    print(f"Voce esta com sobrepeso com {imc:.2f}")
elif imc > 30 and imc < 39.9:
    print(f"Voce esta com obesidade com {imc:.2f}")
elif imc > 40:
    print(f"Voce virou uma baleia com {imc:.2f}")