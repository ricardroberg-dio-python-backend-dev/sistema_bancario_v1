menu = """
==== MENU OPCOES ====
[d] Depositas
[s] Sacar
[e] Extrato
[q] Sair
====================
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

lista_saques = []
lista_depositos = []

while True:
    opcao = input(menu)
    if opcao.lower() == 'd':
        print("Deposito")
        valor_deposito = input("Digite o valor do depósito: ")
        valor_deposito = int(valor_deposito)

        if valor_deposito <= 0:
            print("Valor incorreto. Valor depósito deve ser maior que 0(zero)!")
        else:
            saldo += valor_deposito
            lista_depositos.append(valor_deposito)

    elif opcao.lower() == 's':
        print("Saque")
        if numero_saques < 3:
            valor_saque = input("Digite o valor a sacar: ")
            valor_saque = int(valor_saque)
            if valor_saque <= 0 or valor_saque > saldo:
                print("Valor incorreto ou saldo insuficiente!")

            else:
                saldo -= valor_saque
                numero_saques += 1
                lista_saques.append(valor_saque)
        else:
            print("Limite de saques excedidos pelo dia!")
    elif opcao.lower() == 'e':
        print("Extrato")
        for valor in lista_depositos:
            print(f" + R${valor}")
        for valor in lista_saques:
            print(f" - R${valor}")
        print(f"Salto: {saldo}")
    elif opcao.lower() == 'q':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Selecione opção correta!")

