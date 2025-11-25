"""
Parâmetros especiais

Por padrão, argumentos podem ser passados para uma função Python tanto por
posição quanto explicitamente pelo nome. Para uma melhor legiubilidade e 
desempenho, faz sentido restringir a maneira pelo qual argumetnos possam ser
passados, assim um desenvolvedor precisa apenas olhar para a definição da 
função para determinar se os itens são passados por posição, por posição e
nome, ou por nome.
"""

# =========================================================================
print("============ Exemplo de Função Positional Only ============")
# Argumentos definidos antes da barra / só podem ser passados pela posição, nunca pelo nome.
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(f"Modelo: {modelo}\nAno: {ano}\nPlaca: {placa}\nMarca: {marca}\nMotor: {motor}\nCombustivel: {combustivel}")


# Válido
criar_carro(
    "Palio",
    1999,
    "ABC-1234",
    marca="Fiat",
    motor="1.0",
    combustivel="Gasolina"
)

# Inválido descomente o código abaixo para ver o erro
# criar_carro(
#     modelo="Uno",
#     ano=1999,
#     placa="ABC-5678",
#     marca="Fiat",
#     motor="1.0",
#     combustivel="Gasolina"
# )


# =========================================================================
print("\n============ Exemplo de Função Keyword Only ============")
# Argumentos definidos depois do asterisco * só podem ser passados pelo nome.
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(f"Modelo: {modelo}\nAno: {ano}\nPlaca: {placa}\nMarca: {marca}\nMotor: {motor}\nCombustivel: {combustivel}")


# Válido
criar_carro(
    modelo="Uno",
    ano=1999,
    placa="ABC-5678",
    marca="Fiat",
    motor="1.0",
    combustivel="Gasolina"
)

# Inválido descomente o código abaixo para ver o erro
# criar_carro(
#     "Palio",
#     1999,
#     "ABC-1234",
#     marca="Fiat",
#     motor="1.0",
#     combustivel="Gasolina"
# )


# =========================================================================
print("\n============ Exemplo de Função Keyword e Positional Only ============")
# Argumentos definidos depois do asterisco * só podem ser passados pelo nome.
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(f"Modelo: {modelo}\nAno: {ano}\nPlaca: {placa}\nMarca: {marca}\nMotor: {motor}\nCombustivel: {combustivel}")


# Válido
criar_carro(
    "Palio",
    1999,
    "ABC-1234",
    marca="Fiat",
    motor="1.0",
    combustivel="Gasolina"
)

# Inválido descomente o código abaixo para ver o erro
# criar_carro(
#     modelo="Uno",
#     ano=1999,
#     placa="ABC-5678",
#     marca="Fiat",
#     motor="1.0",
#     combustivel="Gasolina"
# )
