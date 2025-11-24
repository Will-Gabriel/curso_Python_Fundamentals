"""
Tuplas

Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença 
é que tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através 
da classe tuple, ou colocando os valores separados por vírgula dentro de parenteses.

Sempre adicionar uma vírgula a mais ao final para evitar que o Python se perca.
Ex: frutas = ("laranja", "pera", "uva",)
"""


# =========================================================================
print("============ Criando uma Tuplas ============")

frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)

print(f"frutas = ('laranja', 'pera', 'uva',)")
print(f"letras = tuple('python')")
print(f"numeros = tuple([1, 2, 3, 4])")
print(f"pais = ('Brasil',)")


# =========================================================================
print("\n============ Acessando uma Tupla ============")

print(f"Tupla frutas: {frutas}")
print(f"Tupla letras: {letras}")
print(f"Tupla numeros: {numeros}")
print(f"Tupla pais: {pais}")


# =========================================================================
print("\n============ Acessando direto em uma Tupla ============")

print(f"Indice 0 de frutas: {frutas[0]}")
print(f"Indice 1 de frutas: {frutas[1]}")
print(f"Indice -1 de frutas: {frutas[-1]}")
print(f"Indice -2 de frutas: {frutas[-2]}")

