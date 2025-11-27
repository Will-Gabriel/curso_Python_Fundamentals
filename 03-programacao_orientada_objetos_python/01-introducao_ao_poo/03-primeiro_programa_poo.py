"""
João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
Crie um programa onde Jão informe: cor, modelo, ano e valor da bicicleta vendida.
Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!
"""

# "============ Classe Bicicleta ============"

class Bicicleta:
    # Características
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Comportamento
    def buzinar(self):
        print("\nBibibi")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmm...")
        
    def __str__(self):
        return f"\n{self.__class__.__name__}:\n{"\n".join([f"{chave}: {valor}" for chave, valor in self.__dict__.items()])}"


# "============ Objeto Bicicleta ============"
print("\n============ Informações sobre a Bicicleta ============")

cor_bicicleta = input("Informe a cor da bicicleta: ")
modelo_bicicleta = input("Informe o modelo da bicicleta: ")
ano_bicicleta = input("Informe o ano da bicicleta: ")
valor_bicicleta = input("Informe o valor da bicicleta: ")


bicicleta_1 = Bicicleta(cor_bicicleta, modelo_bicicleta, ano_bicicleta, valor_bicicleta)

print(bicicleta_1)

bicicleta_1.buzinar()   # Bicicleta.buzinar(bicicleta_1)
bicicleta_1.correr()
bicicleta_1.parar()
