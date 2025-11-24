"""
Criando Sets

Um set é uma coleção que não possui ibjetos repetidos, usamos sets para
representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.
"""


# =========================================================================
print("============ Exemplo de criação de Sets ============")

numeros = set([1, 2, 3, 1, 3, 4])
numeros2 = {1, 2, 3, 1, 3, 4}
fruta = set("abacaxi")
carros = set(("palio", "gol", "celta", "palio"))

print("numeros = set([1, 2, 3, 1, 3, 4])")
print("numeros2 = {1, 2, 3, 1, 3, 4}")
print("fruta = set('abacaxi')")
print("carros = set(('palio', 'gol', 'celta', 'palio'))\n")

print(f"Set numeros: {numeros} - Tipo: {type(numeros)}")
print(f"Set numeros2: {numeros2} - Tipo: {type(numeros2)}")
print(f"Set fruta: {fruta} - Tipo: {type(fruta)}")
print(f"Set carros: {carros} - Tipo: {type(carros)}")
