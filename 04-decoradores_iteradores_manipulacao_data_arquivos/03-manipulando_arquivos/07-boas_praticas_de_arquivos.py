"""
Bloco with
    Use o gerenciamento de contexto (context manager) com a declaração "with".
    O gerenciamento de contexto permite trabalhar com arquivos de forma segura,
    garantindo que eles sejam fechados corretamente, mesmo em caso de excessões.

Verificar se o arquivo foi aberto com sucesso
    É recomendado verificar se o arquivo foi aberto corretamente antes de executar
    operações de leitura ou gravação nele.

Use a codificação correta
    Certifique-se de usar a codificação correta ao ler ou gravar arquivos de texto.
    O argumento "encoding" da função "open()" permite especificar a codificação.
"""

import os
os.chdir(os.path.dirname(__file__))  # faz o script rodar na pasta onde está salvo

from pathlib import Path
ROOT_PATH = Path(__file__).parent

# =========================================================================
print("============ Exemplo com bloco with ============")

with open(ROOT_PATH / "exemplo3.txt", "r") as arquivo:
    print("Trabalhando com o arquivo...")

# print(arquivo.read())


# =========================================================================
print("\n============ Exemplo - Verificar se o arquivo foi aberto corretamente ============")

try:
    with open(ROOT_PATH / "exemplo33333.txt", "r") as arquivo:
        print("Trabalhando com o arquivo...")
except IOError as error:
    print(f"Não foi possível abrir o arquivo: {error}")


# =========================================================================
print("\n============ Exemplo - Uso do encoding ============")

try:
    with open(ROOT_PATH / "exemplo3.txt", "r", encoding="UTF-8") as arquivo:
        print("Trabalhando com o arquivo...")
except IOError as error:
    print(f"Não foi possível abrir o arquivo: {error}")
