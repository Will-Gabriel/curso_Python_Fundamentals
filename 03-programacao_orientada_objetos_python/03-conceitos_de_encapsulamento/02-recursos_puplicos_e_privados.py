"""
Modificadores de acesso:
    Em linguagens como Java e C++, existem palavras reservadas para definir o 
    nível de acesso aos atributos e métodos da classe. Em Python não temos
    palavras reservadas, porém usamos convenções no nome do recurso, para 
    definir se a variável é pública ou privada.

Definição:
    - Público: Pode ser acessado de fora da classe.
    - Privado: Só pode ser acessado pela classe.

Público/Privado:
    Todos os recursos são públicos, a menos que o nome inicie com underline. 
    Ou seja, o interpretador Python não irá garantir a proteção do recurso,
    mas por ser uma convenção amplamente adotada na comunidade, quando
    encontramos uma variável e/ou método com nome iniciado por underline,
    sabemos que não deveriamos manipular o seu valor diretamente, ou invocar
    o método fora do escopo da classe.
"""

# =========================================================================
print("============ Exemplo de Encapsulamento ============")

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0001", 100)
# conta.depositar(100)

print(f"Número da agência: {conta.nro_agencia}")
print(f"Saldo da conta: {conta.mostrar_saldo()}")
