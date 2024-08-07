
carro = "Gol com escada mt pika"
gasolina = 5.69
etanol = 3.49
km_gasolina = 12
km_etanol = 9

cidade_saida = "Piracicaba"
cidade_destino = "São José dos Campos"
kilometros = 221

litros_gasolina = kilometros / km_gasolina
litros_etanol = kilometros / km_etanol

valor_gasolina = litros_gasolina * gasolina
valor_etanol = litros_etanol * etanol

print(f"Utilizando um {carro} \nSera gasto {valor_gasolina:.2f} reais com gasolina ou {valor_etanol:.2f} reais com etanol \nDe {cidade_saida} a {cidade_destino}")