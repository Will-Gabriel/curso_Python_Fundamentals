"""
Métodos de classe
    Métodos de classe estão ligados à classe e não ao objeto.
    Eles tem acesso ao estado da classe, pois recebem um parâmetro
    que aponta para a classe e nõa para a instância do objeto.

Métodos estáticos
    Um método estático não recebe um primeiro argumento explícito. Ele também
    é um método vinculado à classe e não ao objeto da classe. Este método
    não pode acessar ou modificar o estado da classe. Ele está presente 
    em uma classe porque faz sentido que o método esteja presente na classe.

Métodos de classe x Métodos estáticos
    - Um método de classe recebe um primeiro parâmetro que aponta para a classe,
    enquanto um método estático não.
    - Um método de classe pode acessar ou modificar o estado da classe enquanto
    um método estpático não pode acessá-los ou modificá-lo.

Quando utilizar método de classe ou estático
    - Geralmente usamos o método de classe para criar métodos de fábrica.
    - Geralmente usamos métodos estáticos para criar funções utilitárias.
"""

# ===========================================================================
print("\n============ Exemplo de métodos de classe e estáticos ============")

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_dt_nascimento(cls, ano, mes, dia, nome):
        # print(cls)
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

# p = Pessoa("Wilian", 26)
# print(p.nome, p.idade)

p2 = Pessoa.criar_de_dt_nascimento(1999, 7, 7, "Wilian")
print(f"Nome: {p2.nome}, Idade: {p2.idade}")

print(f"Maior idade: {Pessoa.maior_idade(18)}")
print(f"Maior idade: {Pessoa.maior_idade(17)}")
