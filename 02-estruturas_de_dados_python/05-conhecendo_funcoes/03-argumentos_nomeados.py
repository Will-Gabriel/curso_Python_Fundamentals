"""
Argumentos Nomeados

Funções também podem ser chamadas usando argumentos nomeados dea forma chave=valor.
"""

# =========================================================================
print("============ Exemplo de Função ============")

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso: {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

print()

salvar_carro(
    marca = input("Digite a marca do carro: "),
    modelo = input("Digite o modelo do carro: "),
    ano = input("Digite o ano do carro: "),
    placa = input("Digite a placa do carro: ")
)
