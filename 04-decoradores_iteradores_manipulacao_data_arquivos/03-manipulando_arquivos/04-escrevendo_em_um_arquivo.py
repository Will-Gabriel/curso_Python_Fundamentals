"""
Escrevendo em um arquivo
    Podemos usar "write()" ou "writelines()" para escrever em um arquivo.
    Lembre-se, no entanto, de abrir o arquivo no modo correto.
"""

import os
os.chdir(os.path.dirname(__file__))  # faz o script rodar na pasta onde está salvo


# =========================================================================
print("============ Exemplo ============")

# Abrir o arquivo para leitura e escrita (w+)
# Se o arquivo não existir na pasta ele irá criar
with open('exemplo2.txt', 'w+', encoding="UTF-8") as arquivo:
    
    arquivo.write("Olá, mundo! ")

    # Ler o conteúdo atual (opcional)
    arquivo.seek(0) # Volta ao início para ler tudo

    conteudo_atual = arquivo.read()
    print(f"Conteúdo atual:\n{conteudo_atual}\n")
    
    # Adicionar novo conteúdo (no final)
    # arquivo.write("\nEsta linha foi adicionada ao final")
    arquivo.writelines(["\nEsta ", "linha ", "foi ", "adicionada ", "ao final"])
    
    # Ler o conteúdo atualizado (opcional)
    arquivo.seek(0) # Volta ao início

    conteudo_final = arquivo.read()
    print(f"Conteúdo final:\n{conteudo_final}\n")
