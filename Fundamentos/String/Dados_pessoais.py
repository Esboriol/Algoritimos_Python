
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
endereso = input("Digite o endereço: ")
numero = input("Agora a sua numero: ")
estado = input("Digite o estado: ")


print("Prezado(a),", nome.strip().capitalize() + " " + sobrenome.strip().capitalize(), "\nSua residencia esta localizada no endereço", endereso.strip().title() + " de numero " + numero.strip(), "\nLocalizado no estado de", estado.strip().capitalize())