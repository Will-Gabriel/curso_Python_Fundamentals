"""
Escopo Global e Local.

Python trabalha com escopo local e global, dentro do bloco da função o escopo
é local. POrtanto alterações ali feitas em objetos imutáveis serão perdidas
quando o método terminar de ser executado. Para usar objetos globais utilizamos
a palvra-chave global, que informa ao interpretador que a variável que está 
sendo manipulada no escopo local é global. 

Essa não é uma boa prática e deve ser evitada.
"""

# =========================================================================
print("============ Exemplo de Função ============")

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


print(f"Salario + bonus: R$ {salario_bonus(500)}")
