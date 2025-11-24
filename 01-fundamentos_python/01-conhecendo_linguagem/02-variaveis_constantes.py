"""
Variáveis podem sofre alteração durante a execução do programa

Constante não podem sofrer alterações durante a execução do programa
"""

print("====== Variáveis ======")
age = 26
name = "Wilian"
print(f"- Meu nome é {name} e eu tenho {age} ano(s) de idades.")


age, name = (27, "Pâmela")
print(f"- Meu nome é {name} e eu tenho {age} ano(s) de idades.")


print("\n====== Constantes ======")
ABS_PATH = "/home/wilian/Documents/python_curso"
DEBUG = True
STATES = [
    "SC",
    "RS",
    "PR"
]
AMOUNT = 3.2
 