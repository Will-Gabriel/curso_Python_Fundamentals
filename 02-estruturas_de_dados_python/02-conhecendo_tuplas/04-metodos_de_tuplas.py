"""
Métodos de tuplas
"""


# =========================================================================
print("============ Exemplo do método .count() ============")

cores = ("vermelho", "azul", "verde", "azul",)

print(f"Tupla cores: {cores}\n")

print(f"Qtd cor vermelha: {cores.count("vermelho")}")
print(f"Qtd cor azul: {cores.count("azul")}")
print(f"Qtd cor verde: {cores.count("verde")}")


# =========================================================================
print("\n============ Exemplo do método .index() ============")

linguagens = ("python", "js", "c", "java", "csharp",)

print(f"Tupla linguagens: {linguagens}\n")

print(f"Índice de Java: {linguagens.index("java")}")
print(f"Índice de Python: {linguagens.index("python")}")


# =========================================================================
print("\n============ Exemplo do método .len() ============")

linguagens = ("python", "js", "c", "java", "csharp",)

print(f"Tupla linguagens: {linguagens}\n")

print(f"Qtd de dados na tupla: {len(linguagens)}")
