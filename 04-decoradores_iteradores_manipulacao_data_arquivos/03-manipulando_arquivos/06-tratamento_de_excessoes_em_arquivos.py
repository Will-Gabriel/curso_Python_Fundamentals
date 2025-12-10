"""
Tratar erros é uma parte importante da manipulação de arquivos. Python
oferece uma variedade de excessões que nos permitem lidar com erros comuns.

Exemplos de excessões mais comuns
    - FileNotFoundError: lançada quando o arquivo que está sendo aberto não
    pode ser encontrado no diretório especificado.
    - PermissionError: lançada quando ocorre uma tentativa de abrir um 
    arquivo sem as permissões adequadas para leitura ou gravação.
    - IOError: lançada quando ocorre um erro geral de E/S (entrada/saída)
    ao trabalhar com arquivos, como problemas de permissão, falta de espaço 
    em disco, entre outros.
    - UnicodeDecodeError: lançada quando ocorre um erro ao tentar decodificar
    os dados de um arquivo de texto usando uma codificação inadequada.
    - IsADirectoryError: lançada quando é feita uma tentativa de abrir um
    diretório em vez de um arquivo de texto.
"""

import os
os.chdir(os.path.dirname(__file__))  # faz o script rodar na pasta onde está salvo

from pathlib import Path
ROOT_PATH = Path(__file__).parent

# =========================================================================
print("============ Exemplo - Tentando abrir arquivo que não existe ============")

try:
    arquivo = open("nao_existe.txt", "r")
except FileNotFoundError as error:
    print(f"Arquivo não encontrado: {error}")
except IsADirectoryError as error:
    print("Pasta não encontrado!")


# # =========================================================================
# print("\n============ Exemplo - Tentando abrir pasta que não existe ============")

# try:
#     pasta = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as error:
#     print("Pasta não encontrado!")s
#     # print(error)
# except FileNotFoundError as error:
#     print("Não foi possível abrir o arquivo!")
#     # print(error)
