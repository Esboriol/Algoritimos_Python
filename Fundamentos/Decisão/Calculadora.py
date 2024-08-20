def soma(esc, esc2):
    resultado = esc + esc2
    print(f"O resultado foi de {resultado:.2f}")

def subtração(esc, esc2):
    resultado = esc - esc2
    print(f"O resultado foi de {resultado:.2f}")

def divi(esc, esc2):
    resultado = esc / esc2
    print(f"O resultado foi de {resultado:.2f}")

def Multi(esc, esc2):
    resultado = esc * esc2
    print(f"O resultado foi de {resultado:.2f}")

print("Hola sou uma calculadora e irei resolver os seus 'problemas'")

primeiro = float(input("Digite o primeiro numero: "))

segundo = float(input("Digite o segundo numero: "))

seila = input("Escreva se voce deseja soma, subtração, divisão e multiplicação: ")

if seila == "soma":
    soma(primeiro, segundo)

elif seila == "subtração":
    subtração(primeiro, segundo)

elif seila == "divisão":
    divi(primeiro, segundo)

elif seila == "multiplicação":
    Multi(primeiro, segundo)

else:
    print("Errou kk")