"""
and - Todas as condições precisam ser verdadeiras para retornar True caso contrário retorna False.
or - Pelo menos uma das condições deve ser verdadeira para retornar True caso contrário retorna False.
not - O operador not inverte os valores, o que é False se torna True e vice-versa.
"""

# =========================================================================
print("====== Operador E (and) ======")
saldo = 1000
saque = 200
limite = 100

saque_usuario = (saldo >= saque) and (saque <= limite)
print(f"(Saldo >= Saque) and (Saque <= Limite): {saque_usuario}")

# =========================================================================
print("\n====== Operador OU (or) ======")
saldo = 1000
saque = 200
limite = 100

saque_usuario = (saldo >= saque) or (saque <= limite)
print(f"(Saldo >= Saque) or (Saque <= Limite): {saque_usuario}")

# =========================================================================
print("\n====== Operador Negação (not) ======")
contatos_emergencia = []

print(f"Contatos emergência vazio?: {not contatos_emergencia}")

print(f"1000 > 1500? {not 1000 > 1500}")
