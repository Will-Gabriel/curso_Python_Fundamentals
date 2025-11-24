"""
Conhecendo alguns métodos de strings
"""

palavra = "pYtHon"
print(f"Palavra: {palavra}")


# =========================================================================
print("\n============ Exemplo com método upper() (Maiúscula) ============")
print(f"Método upper(): {palavra.upper()}")


# =========================================================================
print("\n============ Exemplo com método lower() (Minúscula) ============")
print(f"Método lower(): {palavra.lower()}")


# =========================================================================
print("\n============ Exemplo com método title() (Título) ============")
print(f"Método title(): {palavra.title()}")


# =========================================================================
print("\n\n============ Exemplo eliminando espaços ============")

palavra_2 = "    Python "
print(f"Palavra 2: ---{palavra_2}---")


# =========================================================================
print("\n============ Exemplo com método strip() (espaços de ambos os lados) ============")
print(f"Método strip(): ---{palavra_2.strip()}---")


# =========================================================================
print("\n============ Exemplo com método lstrip() (espaços à esquerda) ============")
print(f"Método lstrip(): ---{palavra_2.lstrip()}---")


# =========================================================================
print("\n============ Exemplo com método rstrip() (espaços à direita) ============")
print(f"Método rstrip(): ---{palavra_2.rstrip()}---")


# =========================================================================
print("\n============ Exemplo de junções e centralização ============")

palavra_3 = "Python"
print(f"Palavra 3: {palavra_3}")


# =========================================================================
print("\n============ Exemplo com método center() ============")
print(f"Método center(): {palavra_3.center(14, "#")}")


# =========================================================================
print("\n============ Exemplo com método join() ============")
print(f"Método join(): {".".join(palavra_3)}")
