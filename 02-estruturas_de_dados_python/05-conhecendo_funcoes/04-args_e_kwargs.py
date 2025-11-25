"""
Args e Kwargs

Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses
são definidos (*args e **kwargs), o método recebe os valores como tupla
e dicinário respectivamente.
"""

# =========================================================================
print("============ Exemplo de Função ============")

# Define a função exibir_poema, que recebe:
# - data_extenso: uma string (ex: título ou data)
# - *args: várias linhas de texto (do poema)
# - **kwargs: metadados como autor, ano etc.
def exibir_poema(data_extenso, *args, **kwargs):

    # Junta todas as linhas do poema (args) em uma única string, separando cada linha com uma quebra de linha.
    texto = "\n".join(args)

    # Monta uma string com os metadados (kwargs). Cada chave será capitalizada (ex: "autor" → "Autor") e associada ao seu respectivo valor.
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])

    # Monta a mensagem final contendo: - data ou título - o corpo do poema - os metadados formatados
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"

    # Exibe a mensagem final na tela
    print(mensagem)


# Chamada da função, passando: 
exibir_poema(
    # - A data por extenso
    "Segunda-Feira, 24 de Novembro 2025",

    # - O título "Zen of Python"
    "Zen of Python",

    # - Uma linha de poema como argumento posicional
    "Beutiful is better than ugly.",

    # - Autor e ano como argumentos nomeados (metadados)
    autor="Tim Peters",
    ano=1999)
