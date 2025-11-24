"""
Operadores de associação são usados para verificar
se um objeto está presente em uma sequência.
"""

# =========================================================================
print("====== Exemplo ======")

curso = "'Curso de Python'"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 1000]


print(f"curso - {curso}")
print(f"frutas - {frutas}")
print(f"saques - {saques}")

print(f"\nPython está em curso? {'Python' in curso}")
print(f"maçã está em frutas? {'maçã' not in curso}")
print(f"200 está em saques? {200 in saques}")
