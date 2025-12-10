"""
Gerenciando arquivos e diretórios
    Python também oferece funções para gerenciar arquivos e diretórios. Podemos
    criar, renomear e excluir arquivos e diretórios usando os módulos "os" e "shutil".


"""

import os
import shutil
os.chdir(os.path.dirname(__file__))  # faz o script rodar na pasta onde está salvo


# =========================================================================
print("============ Exemplo criação de diretório com uso do path ============")

from pathlib import Path
ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / "novo-diretorio")

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")
# os.remove(ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "alterado.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")

# =========================================================================
print("\n============ Exemplo mkdir ============")

# Cria um diretório no diretório de trabalho atual
os.mkdir("minha_nova_pasta") 

# Cria um diretório em um caminho específico
# os.mkdir("/home/usuario/documentos/projetos") 


# =========================================================================
print("\n============ Exemplo makedirs ============")

# Cria 'pasta_pai' e 'subpasta' dentro dela, se não existirem
os.makedirs("pasta_pai/subpasta") 

# Cria 'outra_pasta' e não dá erro se já existir
os.makedirs("outra_pasta", exist_ok=True) 


# =========================================================================
print("\n============ Exemplo renomear um arquivo ============")

arq_old = open("old.txt", "w")

arq_old.close()

# Renomear um arquivo
os.rename("old.txt", "new.txt")


# =========================================================================
print("\n============ Exemplo remover um arquivo ============")

# Remover um arquivo
os.makedirs("unwanted.txt")


# =========================================================================
# print("\n============ Exemplo mover ============")

# Mover um arquivo
# shutil.move("source.txt", "destination.txt")
