
saldo = 0
usuario_dono = "Otávio Esboriol da Silva"
senha_dono = 220312
usuario = ''
senha = ''
extrato = []

print("Seja bem vindo ao banco paralelo")
teres = input("Digite sim se possuir uma conta e não se não possuir: ")
ter = teres.lower()

if ter == "sim":
    usu_certo = input("Digite o seu nome de usuario: ")

    while usu_certo != usuario:
        if usu_certo == usuario_dono:
            break
        usu_certo = input("Opss, voce digitou o nome errado: ")

    sen_certa = int(input("Digite a sua senha: "))

    while sen_certa != senha:
        if sen_certa == senha_dono:
            break
        sen_certa = int(input("Opss, voce digitou a senha errada: "))

    des = float(input("Faça um deposito inicial: "))
    while des <= 0:
        des = float(input("Opss algo deu errado digite novamente: "))
    saldo += des
    extrato.append(f"Foi depósitado um valor de R${des:.2f}")
if ter == 'não' or ter == 'nao':
    usuario = input("Primeiro digite o seu nome completo: ")
    senha = int(input("Agora digite a sua senha: "))
    saldo = float(input("Agora faça um deposito: "))
    extrato.append(f"Foi feito um deposito de R${saldo}")

while True:
    escolha = input("Digite a opção desejada 'Depósito', 'Saque', 'Transferência', 'Saldo', 'Extrato' e 'Sair': ")
    certp = escolha.lower()

    if certp == "deposito" or certp == "depósito":
        deposito = float(input("Digite o valor do depósito: "))
        while deposito <= 0:
            deposito = float(input("Ops algo deu errado digite novamente: "))
        saldo += deposito
        extrato.append(f"Foi depósitado um valor de R${deposito:.2f}")
        print("Depositando...")

    if certp == 'saque':
        saque = float(input("Digite o valor do saque: "))
        saldo -= saque
        if saldo < 0:
            print("Erro, voltando...")
            saldo += saque
        if saldo >= 0:
            print("Sacando...")
            extrato.append(f"Foi feito um saque de R${saque:.2f}")

    if certp == "transferência" or certp == "transferencia":
        conta = input("Digite o nome da conta que ira tranferir: ")
        valor = float(input("Digite o valor da transferencia: "))
        saldo -= valor
        if saldo < 0:
            print("Erro, voltando...")
            saldo += valor
        if saldo >= 0:
            print("Trasnsferindo...")
            extrato.append(f"Um valor de R${valor:.2f}, foi transferido para a conta de {conta}")

    if certp == "saldo":
        print(f"O seu saldo total é de R${saldo:.2f}")

    if certp == "extrato":
        print("Aqui esta o seu extrato ao longo do uso da sua conta bancaria: ")
        print(extrato)

    if certp == "sair":
        print("Saindo da sua conta...")
        break

print("Obrigado pela sua atenção 😀😀😀")