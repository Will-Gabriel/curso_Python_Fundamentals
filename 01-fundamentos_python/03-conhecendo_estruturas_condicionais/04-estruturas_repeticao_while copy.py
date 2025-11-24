"""
São estruturas utilizadas para repetir um trecho de código um determinado
número de vezes. Esse número pode ser conhecido previamente ou determinado
através de uma expressão lógica.

while - O comando while é usado para repetir um bloco de código várias vezes.
Faz sentido usar while quando não sabemos o número extao de vezes que nosso
bloco de código deve ser executado.
"""

# =========================================================================
print("\n============ Exemplo de repetição com while ============")

opcao = -1

while opcao != 0:   # Enquanto a opção for diferente de zero faça
    print("Escolha uma opção: ")
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \nSua opção: "))
    print()
    if opcao == 1:
        print("Sacando...\n")
    elif opcao == 2:
        print("Exibindo o extrato...\n")
    elif opcao == 0:
        print("Finalizando...\n")
        opcao = 0   # atribui zero a variável opcao
    else:
        print("Opção inválida!\n")


# =========================================================================
print("\n============ Exemplo de while com else ============")

opcao = -1

while opcao != 0:   # Enquanto a opção for diferente de zero faça
    print("Escolha uma opção: ")
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \nSua opção: "))
    print()
    if opcao == 1:
        print("Sacando...\n")
    elif opcao == 2:
        print("Exibindo o extrato...\n")
    elif opcao == 0:
        print("Finalizando...")
        opcao = 0   # atribui zero a variável opcao
    else:
        print("Opção inválida!\n")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")


# =========================================================================
print("\n============ Exemplo de while com break ============")

while True:   # Loop infinito até cair no break
    print("Escolha uma opção: ")
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \nSua opção: "))
    print()
    if opcao == 1:
        print("Sacando...\n")
    elif opcao == 2:
        print("Exibindo o extrato...\n")
    elif opcao == 0:
        print("Finalizando...")
        print("Obrigado por usar nosso sistema bancário, até logo!")
        break
    else:
        print("Opção inválida!\n")

# =========================================================================
print("\n============ Exemplo de while com continue ============")

while True:

    numero = int(input("informe um número: "))
    
    if numero == 10:
        break
    elif numero % 2 == 0:
        continue

    print(numero)
