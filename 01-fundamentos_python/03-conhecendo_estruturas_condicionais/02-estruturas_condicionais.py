"""
A estrutura condicional permite o desvio de fluxo de controle quando
determinadas expressões lógicas são atendidas.
"""

# =========================================================================
print("\n====== Exemplo condicional com if  ======")

saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print(f"Realizando saque de R$ {saque:.2f}")

if saldo < saque:
    print("Saldo insuficiente!")


# =========================================================================
print("\n====== Exemplo condicional com if e else ======")

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print(f"Realizando saque de R$ {saque:.2f}")
else:
    print("Saldo insuficiente!")


# =========================================================================
print("\n====== Exemplo condicional com if, elif e else ======")

opcao = int(input("Informe uma opção - [1] Sacar [2] Extrato: "))

if opcao == 1:
    valor_saque = float(input("Informe o valor do saque: "))
    print(f"Realizando saque de R$ {valor_saque:.2f}")
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida!")


# =========================================================================
print("\n====== Exemplo condicional com if, elif e else aninhados ======")

saldo = 2000
opcao = int(input("Informe uma opção - [1] Sacar [2] Extrato: "))

if opcao == 1:
    valor_saque = float(input("Informe o valor do saque: "))

    if saldo >= valor_saque:
        print(f"Realizando saque de R$ {valor_saque:.2f}")
    elif saldo < valor_saque:
        print("Saldo insuficiente!")
    else:
        print("Um erro ocoreu. Tente novamente!")

elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida!")


# =========================================================================
print("\n====== Exemplo com if ternário ======")

saldo = 2000
valor_saque = float(input("Informe o valor do saque: "))

status = "Sucesso" if saldo >= valor_saque else "Falha"

print(f"{status} ao realizar o saque!")
