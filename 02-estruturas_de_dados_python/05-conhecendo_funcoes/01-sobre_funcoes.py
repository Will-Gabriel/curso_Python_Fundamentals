"""
Função é um bloco de código identificado por um nome e pode receber uma lista de
parâmetros, esses parâmetros odem ou não ter valores padrões. Usar funções torna
o código legível e possibilita o reaproveitamento de código. Programar baseado
em funções é o mesmo que dizer que estamos prgramando de maneira estruturada.
"""

# =========================================================================
print("============ Exemplo de Função ============")


def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo(a) {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo(a) {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Wilian")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
