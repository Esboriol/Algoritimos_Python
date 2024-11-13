
print("Ola eu sou um programa feito para contar letras de uma frase")
nerd = input("Para iniciarmos, digite a sua frase: ")

letras = len(nerd.strip())

print("quantidade de letras sem espaço:", letras,"\n Quantidade de letras com espaço:", len(nerd) ,"\nQuantidade de palavras", len(nerd.split(" ")))