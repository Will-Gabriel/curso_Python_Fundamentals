"""
Listas em Python podem armazenar de maneira sequencial qualquer tipo de
objeto. Podemos criar listas utilizando o construtor list, a função range
ou colocando valores separados por vírgula dentro de colchetes. Listas
são objetos mutáveis, portanto podemos alterar seus valores após a criação.

Acesso direto:
A lista é uma sequência, portanto podemos acessar seus dados utilizando índices.
Contamos o índice de determinada sequência a partir do índice zero.
"""

# =========================================================================
print("============ Criando lista frutas ============")

print(f"frutas = ['laranja', 'maçã', 'uva']\n")

frutas = ["laranja", "maçã", "uva"]
print(f"Dados da lista frutas: {frutas}\n")


# =========================================================================
print("============ Criando lista frutas2 ============")

print("frutas2 = []\n")

frutas2 = []
print(f"Dados da lista frutas2: {frutas2}\n")


# =========================================================================
print("============ Criando lista letras ============")

print('letras = list("python")\n')

letras = list("python")
print(f"Dados da lista letras: {letras}\n")


# =========================================================================
print("============ Criando lista numeros ============")

print("numeros = list(range(10))\n")

numeros = list(range(10))
print(f"Dados da lista numeros: {numeros}\n")


# =========================================================================
print("============ Criando lista carro ============")

print('carro = ["Gol", "G4", 23.000, 2011, 150000, "Chapecó", True]\n')

carro = ["Gol", "G4", 23.000, 2011, 150000, "Chapecó", True]
print(f"Dados da lista carro: {carro}\n")
