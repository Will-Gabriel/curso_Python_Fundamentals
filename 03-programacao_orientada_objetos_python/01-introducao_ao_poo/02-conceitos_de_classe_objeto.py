"""
Classes e Objetos?

Uma classe define as características e comportamentos de um objeto, porém
nao conseguimos usá-las diretamente. Já os objetos podemos usá-los e eles
possuem as características e comportamentos que foram definidos nas classes.
"""

# =========================================================================
print("============ Exemplo de Classe ============")

class Cachorro:
    # Características
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Comportamento
    def latir(self):
        print("Auau")

    # Comportamento
    def dormir(self):
        self.acordado = False
        print("Zzzzz...")


# =========================================================================
print("\n============ Exemplo de Objeto ============")

cao_1 = Cachorro("Chappie", "amareloo", False)
cao_2 = Cachorro("Aladim", "branco e preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)
