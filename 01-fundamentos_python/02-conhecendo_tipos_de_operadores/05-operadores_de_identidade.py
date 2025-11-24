"""
Operadores de identidade são utilizados para comparar se os
dois objetos testados ocupam a mesma posição na memporia.
"""

# =========================================================================
print("====== Exemplo ======")

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

# Ambos utilizam a mesma região de memória?
print(f"{curso is nome_curso}")

# Ambos utilizam a mesma região de memória?
print(f"{curso is not nome_curso}")


print(f"{saldo is limite}")
