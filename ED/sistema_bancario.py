import time

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair



--> """


saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    time.sleep(2)
    escolha = input(menu)

    if escolha == "d":
        print("Deposito\n")
        deposita_valor = float(input("Informe o valor de deposito:"))

        if deposita_valor > 0:
            saldo += deposita_valor
            print(f"Deposito: R$ {deposita_valor:.2f}\n")
            extrato.append(f"Deposito: R$ {deposita_valor:.2f}")
            time.sleep(2)
        else:
            print("Valor Inválido, faça o deposito novamente!")

    elif escolha == "s":
        print("Saque\n")
        saque = float(input("Valor para sacar: "))

        if saque > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Valor maior que o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Máximo de saques atingido.")
        elif saque > 0:
            saldo -= saque
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            time.sleep(2)
        else:
            print("Valor Inválido.")

    elif escolha == "e":
        print("\n -------------- Extrato --------------")
        print("Sem atividade." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n -------------------------------------")
        time.sleep(2)
    elif escolha == "q":
        print("Até Logo!")
        break

    else:
        print("Alternativa Inválida, tente novamente.")
