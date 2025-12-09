"""
Funções de decoração com argumentos
    Podemos usar *args e **kwargs na função interna, com isso ele aceitará
    um número arbitrário de argumentos posicionais e palavras-chave.

Introspecção
    Introspecção é a capacidade de um objeto saber sobre seus próprios
    atributos em tempo de execução.
"""

# =========================================================================
print("============ Exemplo de decoradores simples ============")

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")

    return envelope


@meu_decorador
def ola_mundo():
    print(f"Olá mundo!")


ola_mundo()


# =========================================================================
print("\n============ Exemplo 1 de decoradores com argumentos ============")

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a função.")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar a função.")

    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo! {nome}")


ola_mundo("Wilian")


# =========================================================================
print("\n============ Exemplo 2 de decoradores com argumentos ============")

def meu_decorador(func):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a função.")
        resultado = func(*args, **kwargs)
        print("Faz algo depois de executar a função.")
        return resultado

    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo! {nome}")
    return nome.upper()


resultado = ola_mundo("Wilian")
print(resultado)


# =========================================================================
print("\n============ Exemplo 3 de decoradores com argumentos e intrsopecção ============")

import functools

def meu_decorador(func):

    @functools.wraps(func)
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a função.")
        resultado = func(*args, **kwargs)
        print("Faz algo depois de executar a função.")
        return resultado

    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo! {nome}")


ola_mundo("Wilian")
print(ola_mundo)
print(ola_mundo.__name__)