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
        else:
            print("Valor Inválido, faça o deposito novamente!")

    elif escolha == "s":
        print("Saque")

    elif escolha == "e":
        print("Extrato")
        print(extrato)
    elif escolha == "q":
        print("Até Logo!")
        break

    else:
        print("Alternativa Inválida, tente novamente.")
