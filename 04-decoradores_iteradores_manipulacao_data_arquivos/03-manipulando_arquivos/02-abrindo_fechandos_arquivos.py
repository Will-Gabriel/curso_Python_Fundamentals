"""
Por que precisamos manipular arquivos?
    Para mianupular arquivos em Python, primeiro precisamos abrilos.
    Usamos a funçao "open()" para isso. Quando terminamos de trabalhar com
    o arquivo, usamos a função "close()" para liberar recursos.

Modos de abertura de arquivo
    Existem diferentes modos para abrir um arquivo, como somente leitura ("r"),
    gravação ("w") e anexar ("a"). O modo de abertura deve ser escolhido de
    acordo com a operação que iremos realizar no mesmo.
"""

# =========================================================================
print("============ Exemplo ============")

file = open("exemplo.txt", "r")

file.close()
