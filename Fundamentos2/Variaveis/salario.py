"""
Exemplo de algoritmo que calcula o aumento de salário do colaborador baseando se
no percentual do aumento
"""

colaborador_nome = "Pamonha"
empresa = "Senai"
salario = 3456.90
percentual = 7

valor_aumento = salario * (percentual / 100)
novo_salario = valor_aumento + salario

formatted_salario = f"{novo_salario:.2f}"

print(f"O colaborador {colaborador_nome} da empresa {empresa} teve um ajuste de salario para {formatted_salario} reais")