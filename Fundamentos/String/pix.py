import random

nome = input("Digite o seu nome completo: ")
cpf = input("Agora digite o seu CPF: ")

nome = nome.strip().lower().replace(" ", "")

cpf = cpf.strip().replace(".", "").replace("-", "")
while len(cpf) != 11:
    cpf = input("Ops, parece que algo deu errado. Tente novamente: ")
    cpf = cpf.strip().replace(".", "").replace("-", "")

chave = nome + cpf
chave_pix = chave[:8] + chave[-8:]

lista_embaralhada = list(chave_pix)
random.shuffle(lista_embaralhada)

pix = ''.join(lista_embaralhada[:16])
chave_pix_formatada = '-'.join([pix[i:i+4] for i in range(0, 16, 4)])

print("Chave Pix gerada:", chave_pix_formatada)
