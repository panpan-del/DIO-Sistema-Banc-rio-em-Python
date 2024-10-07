

menu = """

[d] Depositar  
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor digitado é invalido")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque:"))

        passou_saldo = valor > saldo

        passou_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if passou_saldo:
            print("Operação falhou, saldo insuficiente")
        
        elif passou_limite:
            print("Operação falhou, valor de saque excede o limite de saques")
        
        elif excedeu_saques:
            print("Operação falhou, numero máximo de saques excedido")

        elif valor > 0:
                saldo -= valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                numero_saques += 1

        else:
            print("Operção invalida, valor invalido")

    elif opcao == "e":
        print("\nExtrato")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    
    elif opcao == "q":
       break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")