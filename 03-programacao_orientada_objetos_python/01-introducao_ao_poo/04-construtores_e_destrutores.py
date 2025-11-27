"""
Contrutores e Destrutores

Método construtor:
    O método contrutor sempre é executado quando uma nova instância da classe
    é criada. Nesse método inicializamos o estado do nosso objeto. Para declarar 
    o método construtor da classe, criamos um método com nome __init__.

Método destrutor:
    O método destrutor é sempre utilizado quando uma instância (objeto) é
    destruída. Destrutores em Python não são tão necessários quando em C++
    porque o Python tem um coletor de lixo que lida com o gerenciamento de
    memória automaticament. Para declarar o método destrutor da classe,
    criamos um método com o nome __del__.
"""

# ============ Exemplo de construtor ============
class Cachorro:
    # Inicializando a classe - construtor
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor 
        self.acordado = acordado

    # destrutor
    def __del__(self):
        print("Removendo a instância da classe")

    def latir(self):
        print("Auau")


c = Cachorro("Chappie", "amarelo")
c.latir()

print("Olá mundo")

del c

print("Olá mundo")
print("Olá mundo")
