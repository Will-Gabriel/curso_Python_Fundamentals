"""
Lendo um arquivo
    Python fornece várias maneiras de ler um arquivo. Podemos usar "read()",
    "readline()" ou "readlines()" dependendo de nossas necessidades.
"""

import os
os.chdir(os.path.dirname(__file__))  # faz o script rodar na pasta onde está salvo


# =========================================================================
print("============ Exemplo método read() ============")

arquivo = open("exemplo.txt", "r")

# Ler todo arquivo de uma vez
print(arquivo.read())

arquivo.close()


# =========================================================================
print("\n============ Exemplo método readline() ============")

arquivo = open("exemplo.txt", "r")

# Ler uma linha do arquivo por vez
# print(arquivo.readline())

while len(linha := arquivo.readline()):
    print(linha)


arquivo.close()


# =========================================================================
print("\n============ Exemplo método readlines() ============")

arquivo = open("exemplo.txt", "r")

# Retorna uma lista onde cada elemento é uma linha do arquivo
for linha in arquivo.readlines():
    print(linha)

arquivo.close()
