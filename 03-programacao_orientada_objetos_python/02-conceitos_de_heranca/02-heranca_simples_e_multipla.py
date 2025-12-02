"""
O que é Herança simples?

Quando uma classe filha herda apenas uma classe pai,
ela é chamada de herança simples.

O que é Herança Múltipla?

Quando uma classe filha herda de várias classes pai, 
ela é chamada de herança múltipla
"""

# =========================================================================
print("============ Exemplo de Herança Simples ============")

class A:
    pass

class B(A):
    pass


# =========================================================================
print("============ Exemplo de Herança Multipla ============")

class A:
    pass

class B:
    pass

class C(A, B):
    pass
