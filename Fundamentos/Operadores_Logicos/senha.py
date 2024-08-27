nome = input("Ola, digite o seu nome de usuario: ")

senha = input("Agora, digite a sua senha: ")

if nome == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Voce nao tem acesso")