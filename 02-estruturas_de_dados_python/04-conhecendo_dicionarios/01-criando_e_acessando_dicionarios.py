"""
Criando e acessando Dicionários.

Um dicionário é conjunto não-ordenado de pares chave:valor, onde as chaves
são únicas em um dada instância do dicionário. Dicionários são delimitados
por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas.
"""


# =========================================================================
print("============ Criando Dicionários ============")

# Forma 1
pessoa = {
    "nome": "Wilian",
    "idade": 26,
}

# Forma 2
# pessoa = dict(nome="Wilian", idade=26)

# Adicionando nova chave ao dicionário
pessoa["telefone"] = "3333-3333"

print("Forma 1: pessoa = dict(nome='Wilian', idade=26)")
print("""
Forma 2: 
pessoa = {
    "nome": "Wilian",
    "idade": 26,
}
""")

print("Adicionado nova chave: pessoa['telefone'] = '3333-3333'\n")
print(f"Dicionário pessoa: {pessoa}")


# =========================================================================
print("\n============ Alterando os dados do Dicionário ============")

dados = {
    "nome": "Wilian",
    "idade": 26,
    "telefone": "3333-3333",
}

print(f"Dados antes da alteração: {dados}\n")

dados["nome"] = "Pâmela"
dados["idade"] = 27
dados["telefone"] = "3333-2222"

print(f"Dados após alteração: {dados}")


# =========================================================================
print("\n============ Acessando os dados do Dicionário ============")

print(f"Dados completos: {dados}\n")

print(f"Nome: {dados["nome"]}")
print(f"Idade: {dados["idade"]}")
print(f"Telefone: {dados["telefone"]}")
