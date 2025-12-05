"""
Para que srevem?

Com o property() do Python, podemos criar atributos gerenciados em nossas classes.
Podemos usar atributos gerenciados, também conhecidos como propriedade, quando
precisar modificar sua implementação interna sem alterar a API pública da classe.
"""

# =========================================================================
print("============ Exemplo Foo ============")

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value

    @x.deleter
    def x(self):
        self._x = -1


foo = Foo(10)
print(foo.x)

foo.x = 10
print(foo.x)

del foo.x
print(foo.x)


# =========================================================================
print("\n============ Exemplo Pessoa ============")

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa("Wilian", 1999)

print(f"Nome: {pessoa.nome} - Idade: {pessoa.idade}")
