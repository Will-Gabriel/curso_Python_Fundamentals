"""
Atributos do objeto

Todos os objetos nascem com o memo número de atributos de classe e de instância.
Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia),
já os atributos de classe são compartilhados entre os objetos.
"""

# =========================================================================
print("\n============ Exemplo ============")

class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.escola}"


def mostrar_alunos(*alunos):
    for aluno in alunos:
        print(f"Aluno: {aluno}")

aluno_1 = Estudante("Wilian", 12345)
aluno_2 = Estudante("Pâmela", 54321)

mostrar_alunos(aluno_1, aluno_2)
