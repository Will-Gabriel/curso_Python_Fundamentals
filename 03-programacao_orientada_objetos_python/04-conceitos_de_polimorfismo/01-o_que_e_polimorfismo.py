"""
Muitas formas!

A palavra polimorfismo significa ter muitas formas. Na programação, polimorfismo
significa o mesmo nome da função (mas assinaturas diferentes) sendo usado para
tipos diferentes.

O len é um exemplo clássico de polimorfismo em Python porque uma mesma função (mesmo nome) consegue funcionar com tipos diferentes, adaptando seu comportamento conforme o tipo do objeto recebido.

Por que len() é polimórfico?
Porque:
    Você usa uma única função: len()
    Mas ela funciona para múltiplos tipos diferentes: strings, listas, tuplas, dicionários, sets, etc.
    E retorna resultados diferentes conforme o objeto.
"""

# =========================================================================
print("\n============ Exemplo ============")

print(len("Olá"))          # 3 → tamanho da string
print(len([1, 2, 3, 4]))   # 4 → itens da lista
print(len((10, 20)))       # 2 → itens da tupla
print(len({"a": 1}))       # 1 → chaves no dicionário
