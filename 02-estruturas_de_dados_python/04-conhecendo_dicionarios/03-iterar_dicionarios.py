"""
Iterar Dicionários.

A forma mais comum para percorrer os dados de um 
dicionário é utilizando o laço for.
"""


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

# =========================================================================
print("============ Iterar Dicinários ============")

for chave in contatos:
    print(f"Chave: {chave} \n- Dados: {contatos[chave]}\n")



# =========================================================================
print("============ Iterar Dicinários com .items() ============")

for chave, valor in contatos.items():
    print(f"Chave: {chave} \n- Dados: {valor}\n")

