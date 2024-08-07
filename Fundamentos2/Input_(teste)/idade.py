
print(f"Ola sou um ladrão de dados")

nome = input("Digite o seu nome: ")

while True:
    try:
        idade = int(input("Digite a sua idade: "))
        break
    except ValueError:
        print("Pare de ser burro e coloque um numero :)")

print(f"Seja bem vindo {nome}, estamos te registrando com {idade} anos")