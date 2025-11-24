"""
Dicionários Aninhados.

Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde 
que a chave para esse valor seja um objeto imutável como strings e números.
"""


# =========================================================================
print("============ Acessando os dados do Dicinário aninhado ============")

contatos = {
    "wilian@gmail.com": {
        "nome": "Wilian",
        "telefone": "3333-3333"
    },
    "pamela@gmail.com": {
        "nome": "Pâmela",
        "telefone": "3333-2222"
    }
}

print(f"Contatos: {contatos}\n")
print(f"Contato Pâmela: {contatos["pamela@gmail.com"]["telefone"]}")
