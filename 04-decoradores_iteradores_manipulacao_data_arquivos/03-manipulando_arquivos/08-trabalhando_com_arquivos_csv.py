"""
Lendo arquivos CSV
    Python oferece um módulo chamado "csv" para lidar facilmente com arquivos csv.

Escrevendo em arquivos CSV
    Da mesma forma podemos utilizar o módulo "csv" para escrever em arquivos csv.

Práticas recomendadas
    - Usar csv.reader e csv.writer para manipular arquivos CSV.
    - Fazer o tratamento correto das excessões.
    - Ao gravar arquivos CSV definir o argumento newline="" no método "open".
"""

import os
os.chdir(os.path.dirname(__file__))  # faz o script rodar na pasta onde está salvo

from pathlib import Path
ROOT_PATH = Path(__file__).parent

import csv


# =========================================================================
print("============ Exemplo - Escrevendo em arquivos CSV ============")

nome_arquivo = "exemplo.csv"

try:
    with open(ROOT_PATH / nome_arquivo, "w", encoding="UTF-8", newline="") as arquivo:
        escrever = csv.writer(arquivo)
        
        escrever.writerow(["ID", "Nome", "Idade"])
        escrever.writerow(["1", "Wilian", 26])
        escrever.writerow(["2", "Pâmela", 27])

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
except IOError as exc:
    print(f"Erro ao criar o arquivo: {exc}")


# =========================================================================
print("\n============ Exemplo - Lendo arquivos CSV ============")

try:
    with open(ROOT_PATH / nome_arquivo, "r", encoding="UTF-8") as arquivo:
        ler_arquivo = csv.reader(arquivo)

        for linha in ler_arquivo:
            print(linha)
except IOError as exc:
    print(f"Erro ao criar o arquivo: {exc}")


# =========================================================================
print("\n============ Exemplo - Lendo arquivos CSV ============")

COLUNA_ID = "ID"
COLUNA_NOME = "Nome"
COLUNA_IDADE = "Idade"

try:
    with open(ROOT_PATH / nome_arquivo, "r", encoding="UTF-8") as arquivo:
        ler_arquivo = csv.DictReader(arquivo)

        for linha in ler_arquivo:
            print(f"ID: {linha[COLUNA_ID]}")
            print(f"Nome: {linha[COLUNA_NOME]}")
            print(f"Idade: {linha[COLUNA_IDADE]}\n")

except IOError as exc:
    print(f"Erro ao criar o arquivo: {exc}")
