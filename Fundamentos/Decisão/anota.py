print("Hola iremos calcular a sua media")

pri = float(input("Digite a sua primeira nota: "))

seg = float(input("Digite a sua segunda nota: "))

area = (pri + seg) / 2

if area >= 7:
    print(f"Vode passou de ano com a media de {area:.2f}")
else:
    print(f"Voce repetiu de ano com a media de {area:.2f}")
