"""
Métodos de Dicionários.
"""

contatos = {
    "wilian@gmail.com": {"nome": "Wilian", "telefone": "3333-3333"},
    "pamela@gmail.com": {"nome": "Pâmela", "telefone": "3333-2222"}
}

# =========================================================================
print("============ Exemplo método .clear() ============")

print(f"Antes de usar o .clear(): {contatos}\n")

contatos.clear()
print(f"Após usar o .clear(): {contatos}")


# =========================================================================
print("\n============ Exemplo método .copy() ============")

contatos = {
    "wilian@gmail.com": {"nome": "Wilian", "telefone": "3333-3333"},
    "pamela@gmail.com": {"nome": "Pâmela", "telefone": "3333-2222"}
}

print(f"Antes de usar o .copy(): {contatos}\n")

copia_contatos = contatos.copy()
print(f"Após usar o .copy(): {copia_contatos}")


# =========================================================================
print("\n============ Exemplo método .fromkeys() ============")

dicionario = dict.fromkeys(["nome", "telefone"])

print("dicionario = dict.fromkeys(['nome', 'telefone'])")
print(f"Após usar o .fromkeys(): {dicionario}\n")

dicionario2 = dict.fromkeys(['nome', 'telefone'], 'vazio')

print("dicionario2 = dict.fromkeys(['nome', 'telefone'], 'vazio')")
print(f"Após usar o .fromkeys(): {dicionario2}\n")


# =========================================================================
print("\n============ Exemplo método .get() ============")

print(f"Contatos: {contatos}\n")

print("contatos.get('chave')")
print(f"Contatos get: {contatos.get("chave")}\n")

print("contatos.get('chave', {})")
print(f"Contatos get: {contatos.get("chave", {})}\n")

print("contatos.get('wilian@gmail.com')")
print(f"Contatos get: {contatos.get("wilian@gmail.com")}")


# =========================================================================
print("\n============ Exemplo método .items() ============")

print(f"Contatos: {contatos}\n")

print("contatos.items()")
print(f"Contatos items: {contatos.items()}\n")


# =========================================================================
print("\n============ Exemplo método .keys() ============")

print(f"Contatos: {contatos}\n")

print("contatos.keys()")
print(f"Contatos keys: {contatos.keys()}\n")


# =========================================================================
print("\n============ Exemplo método .pop() ============")

contatos = {
    "wilian@gmail.com": {"nome": "Wilian", "telefone": "3333-3333"},
    "pamela@gmail.com": {"nome": "Pâmela", "telefone": "3333-2222"}
}

print(f"Contatos: {contatos}\n")

print("contatos.pop('wilian@gmail.com')")
print(f"Contatos pop: {contatos.pop("wilian@gmail.com")}\n")

print("contatos.pop('wilian@gmail.com', {})")
print(f"Contatos pop: {contatos.pop('wilian@gmail.com', {})}\n")


# =========================================================================
print("\n============ Exemplo método .popitem() ============")

contatos = {
    "wilian@gmail.com": {"nome": "Wilian", "telefone": "3333-3333"}
}

print(f"Contatos: {contatos}\n")

print("contatos.popitem()")
print(f"Contatos popitem: {contatos.popitem()}\n")

# print("contatos.popitem()")
# Descomente para ver o erro
# print(f"Contatos popitem: {contatos.popitem()}\n")


# =========================================================================
print("\n============ Exemplo método .setdefault() ============")

contatos = {
    "nome": "Wilian", "telefone": "3333-3333"
}

print(f"Contatos: {contatos}\n")

print("contatos.setdefault('nome', 'Pâmela')")
print(f"Contatos setdefault: {contatos.setdefault('nome', 'Pâmela')}\n")

print(f"Contatos: {contatos}\n")


print("contatos.setdefault('idade', 27)")
print(f"Contatos setdefault: {contatos.setdefault('idade', 27)}\n")

print(f"Contatos: {contatos}\n")


# =========================================================================
print("\n============ Exemplo método .update() ============")

contatos = {
    "wilian@gmail.com": {"nome": "Wilian", "telefone": "3333-3333"}
}

print(f"Contatos: {contatos}\n")

print("contatos.update('wilian@gmail.com': {'nome': 'Will'})")
contatos.update({"wilian@gmail.com": {"nome": "Will"}})

print(f"Contatos: {contatos}\n")

print("contatos.update('pamela@gmail.com': {'nome': 'Pâmela', 'idade': '3333-2222'})")
contatos.update({'pamela@gmail.com': {'nome': 'Pâmela', 'idade': '3333-2222'}})

print(f"Contatos: {contatos}\n")


# =========================================================================
print("\n============ Exemplo método .values() ============")

contatos = {
    "wilian@gmail.com": {"nome": "Wilian", "telefone": "3333-3333"},
    "pamela@gmail.com": {"nome": "Pâmela", "telefone": "3333-2222"}
}

print(f"Contatos: {contatos}\n")

print("contatos.values()")
print(f"Contatos values: {contatos.values()}\n")


# =========================================================================
print("\n============ Exemplo método 'in' ============")

contatos = {
    "wilian@gmail.com": {"nome": "Wilian", "telefone": "3333-3333"},
    "pamela@gmail.com": {"nome": "Pâmela", "telefone": "3333-2222"}
}

print(f"Contatos: {contatos}\n")

print("wilian@gmail.com in contatos")
print(f"Contato: {"wilian@gmail.com" in contatos}\n")

print("pamela@gmail.com in contatos")
print(f"Contato: {"pamela@gmail.com" in contatos}\n")

print("idade in contatos[wilian@gmail.com]")
print(f"Contato: {"idade" in contatos["wilian@gmail.com"]}\n")

print("telefone in contatos[wilian@gmail.com]")
print(f"Contato: {"telefone" in contatos["wilian@gmail.com"]}\n")


# =========================================================================
print("\n============ Exemplo método 'not in' ============")

contatos = {
    "wilian@gmail.com": {"nome": "Wilian", "telefone": "3333-3333"},
    "pamela@gmail.com": {"nome": "Pâmela", "telefone": "3333-2222"}
}

print(f"Contatos: {contatos}\n")

print("wilian@gmail.com not in contatos")
print(f"Contato: {"wilian@gmail.com" not in contatos}\n")

print("joazinho@gmail.com not in contatos")
print(f"Contato: {"joazinho@gmail.com" not in contatos}\n")


# =========================================================================
print("\n============ Exemplo método 'del' ============")

contatos = {
    "wilian@gmail.com": {"nome": "Wilian", "telefone": "3333-3333"},
    "pamela@gmail.com": {"nome": "Pâmela", "telefone": "3333-2222"}
}

print(f"Contatos: {contatos}\n")

print("del contatos['wilian@gmail.com']['telefone']")
del contatos['wilian@gmail.com']['telefone']
print(f"Contatos: {contatos}\n")

print("del contatos['wilian@gmail.com']")
del contatos['wilian@gmail.com']
print(f"Contatos: {contatos}\n")
