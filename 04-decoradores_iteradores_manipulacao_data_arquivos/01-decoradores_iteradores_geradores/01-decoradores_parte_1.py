"""
Inner functions
    É possível definir funções dentro de outras funções. Tais funções são
    chamadas de funções internas.

Decorador simples
"""

# =========================================================================
print("\n============ Exemplo 1 de decoradores simples ============")

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")

    return envelope


def ola_mundo():
    print("Olá mundo!")


ola_mundo = meu_decorador(ola_mundo)
ola_mundo()


# =========================================================================
print("\n============ Exemplo 2 de decoradores simples ============")

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")

    return envelope

@meu_decorador
def ola_mundo():
    print("Olá mundo!")


ola_mundo()


# =========================================================================
print("\n============ Exemplo - Inner functions ============")

def pai():
    print("Escrevendo da função pai()")

    def filho_1():
        print("Escrevendo da função filho_1()")

    def filho_2():
        print("Escrevendo da função filho_2()")

    filho_2()
    filho_1()


pai()


# =========================================================================
print("\n============ Exemplo - Retornando funções de funções ============")

def calcular(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    if operacao == "+":
        return somar
    else:
        return subtrair


resultado = calcular("+")(1, 3)
print(f"Resultado: {resultado}")
