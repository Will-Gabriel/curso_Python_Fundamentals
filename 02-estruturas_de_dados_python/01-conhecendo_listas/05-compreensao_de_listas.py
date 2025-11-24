"""
Compreensão de listas

A compreensão de listas oferece um sintaxe mais curta quando voçê deseja: criar 
uma nova lista com base nos valores de uma lista existente (filtro) ou gerar
uma nova lista aplicando alguma modificação nos elementos de uma lista existente.
"""


# =========================================================================
print("============ Exemplo 1 de filtro ============")

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

print(f"Lista de números: {numeros}")

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Lista de pares: {pares}")


# =========================================================================
print("\n============ Exemplo 2 de filtro ============")

numeros = [1, 30, 21, 2, 9, 65, 34]

print(f"Lista de números: {numeros}")

pares = [numero for numero in numeros if numero % 2 == 0]

print(f"Lista de pares: {pares}")


# =========================================================================
print("\n============ Exemplo 3 modificando valores ============")

numeros = [1, 30, 21, 2, 9, 65, 34]

print(f"Lista de números: {numeros}")

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(f"Lista de pares: {quadrado}")


# =========================================================================
print("\n============ Exemplo 4 modificando valores ============")

numeros = [1, 30, 21, 2, 9, 65, 34]

print(f"Lista de números: {numeros}")
        
quadrado = [numero ** 2 for numero in numeros]

print(f"Lista de pares: {quadrado}")
