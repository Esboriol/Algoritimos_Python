def contador(frase):
    vogais = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    frase = frase.lower()

    for letra in frase:
        if letra in vogais:
            vogais[letra] += 1

    return vogais


# Solicitando a frase ao usuário
palavra = input("Digite a sua frase: ")

# Contando as vogais
resultado = contador(palavra)

# Exibindo o resultado
for vogal, contagem in resultado.items():
    print(f"A letra '{vogal}' apareceu {contagem} vez(es).")
