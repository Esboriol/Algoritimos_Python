def falta(media):
    media = media - 5
    return media

def media(p, e):
    pr = (p / 100) * 70
    ex = (e / 100) * 30
    total = pr + ex
    return total

print("Olá professor, irei calcular para você a média dos seus alunos.")

p1 = float(input("Para começar, digite a nota da primeira prova: "))
p2 = float(input("Agora, digite a nota da segunda prova: "))

e1 = float(input("Digite a nota do primeiro exercício: "))
e2 = float(input("Agora, do segundo exercício: "))
e3 = float(input("E o último exercício agora: "))

provas = (p1 + p2) / 2
exercicios = (e1 + e2 + e3) / 3

nota = media(provas, exercicios)

faltas = int(input("Digite agora a quantidade de faltas desse aluno: "))

if faltas >= 5:
    nota = falta(nota)
    if nota < 0:
        nota = 0
    print("Subtraindo 5 pontos da média.")
else:
    print("Ok, iremos continuar normalmente.")

print(f"A média do aluno será de {nota:.2f} pontos.")
