"""
Conhecendo a interpolação de variáveis
"""

nome = "Wilian"
idade = 26
profissao = "Analista de Dados"
linguagem = "Python"

# =========================================================================
print("\n============ Exemplos de Interpolação Old Style % ============")

# Devemos cuidar a ordem para exibir corretamente
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))


# =========================================================================
print("\n============ Exemplos de Interpolação com .format ============")

# Devemos cuidar a ordem para exibir corretamente
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

pessoa = {
    "nome": "Wilian",
    "idade": 26,
    "profissao": "Analista de Dados",
    "linguagem": "Python"
}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))


# =========================================================================
print("\n============ Exemplos de Interpolação com f-strings (melhor forma) ============")

# Devemos cuidar a ordem para exibir corretamente
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")


# =========================================================================
print("\n============ Exemplos de formatação com f-strings ============")

PI = 3.14159

print(f"Valor de PI sem formatação: {PI}")

print(f"Valor de PI com formatação: {PI:.2f}")

print(f"Valor de PI com formatação: {PI:10.2f}")
