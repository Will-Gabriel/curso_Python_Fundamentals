"""
Objetos de Primeira Classe.

Em Python tudo é objeto, dessa forma funções também são objetos de primeira
classe. Com isso podemos atribuir funções a variáveis, passá-las como parâmetro
para funções, usá-las como valores em estruturas de dados (listas, tuplas, 
dicionários, etc) e usar como valor de retorno para uma função (closures).
"""

# =========================================================================
print("============ Exemplo de Função ============")

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)

    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar)     # O resultado da operação 10 + 10 = 20
exibir_resultado(15, 10, subtrair)     # O resultado da operação 15 + 10 = 20

operacao = somar
print(f"Operação: {operacao(1, 23)}")
