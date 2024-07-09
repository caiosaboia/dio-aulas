import time


def chama_menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Lista contas
    [nu] Novo usuário
    [q] Sair


    --> """
    return input(menu)


def deposita_valor(saldo, valor, extrato, /):

    if deposita_valor > 0:
        saldo += deposita_valor
        print(f"Deposito: R$ {deposita_valor:.2f}\n")
        extrato.append(f"Deposito: R$ {deposita_valor:.2f}")
        time.sleep(2)

    else:
        print("Valor Inválido, faça o deposito novamente!")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor maior que o limite.")
    elif numero_saques >= limite_saques:
        print("Máximo de saques atingido.")
    elif saque > 0:
        saldo -= saque
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque efetuado!")
        time.sleep(2)
    else:
        print("Valor Inválido.")


def mostra_extrato(saldo, /, *, extrato):
    print("\n -------------- Extrato --------------")
    print("Sem atividade." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n -------------------------------------")
    time.sleep(2)


def filtra_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for i in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def cria_usuario(usuarios):
    cpf = input("Coloque o CPF(apenas numeros): ")
    busca_usuario = filtra_usuario(cpf, usuarios)

    if busca_usuario:
        print("\n !!! Usuários já existe !!!")
        return

    nome_usuario = input("Nome completo: ")
    nascimento_usuario = input("Data de Nascimento (dd-mm-aaaa): ")
    endereco_usuario = input("Endereço: ")

    usuarios.append(
        {
            "nome": nome_usuario,
            "data de nascimento": nascimento_usuario,
            "cpf": cpf,
            "endereco": endereco_usuario,
        }
    )
    print("Usuário criado !")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']} 
        """
        print("=" * 100)


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        time.sleep(2)
        escolha = chama_menu()

        if escolha == "d":

            print("Deposito\n")
            valor = float(input("Informe o valor de deposito:"))

            saldo, extrato = deposita_valor(saldo, valor, extrato)

        elif escolha == "s":
            print("Saque\n")
            valor = float(input("Valor para sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif escolha == "e":
            mostra_extrato(saldo, extrato=extrato)

        elif escolha == "nu":
            cria_usuario(usuarios)

        elif escolha == "nc":
            numero_conta = len(contas) + 1
            conta = cria_usuario(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif escolha == "lc":
            listar_contas(contas)

        elif escolha == "q":
            print("Até Logo!")
            break

        else:
            print("Alternativa Inválida, tente novamente.")
