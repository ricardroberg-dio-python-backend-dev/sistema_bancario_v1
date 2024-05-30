import textwrap

def menu ():
    menu = """\n
    ==== MENU OPCOES ====
    [d]\tDepositas
    [s]\tSacar
    [e]\tExtrato
    [c]\tCadastra conta
    [l]\tListar contas
    [u]\tCadastra usuario
    [q]\tSair
    ====================
    => """
    return input(textwrap.dedent(menu))

def efetua_deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Valor incorreto. Valor depósito deve ser maior que 0(zero)! @@@")
    
    return saldo, extrato

def efetua_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de sques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibe_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizdas movimentações." if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}")
    print("\n=========================================")

def cadastra_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data do nascimento (dd-mm-aaaa): ")
    endereco = input("Inform o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n @@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t\t{conta['usuario']['nome']}
        """
        print("=" * 10)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    # lista_saques = []
    # lista_depositos = []

    while True:
        opcao = menu()
        if opcao == 'd':
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = efetua_deposito(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input("Digite o valor a sacar: "))
            saldo, extrato = efetua_saque(saldo = saldo,
                                        valor = valor,
                                        extrato = extrato, 
                                        limite = limite,
                                        numero_saques = numero_saques,
                                        limite_saques = LIMITE_SAQUES
                                        )

        elif opcao == 'e':
            exibe_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            cadastra_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'l':
            listar_contas(contas)

        elif opcao.lower() == 'q':
            print("Saindo...")
            break
        else:

            print("Opção inválida. Selecione opção correta!")

main()