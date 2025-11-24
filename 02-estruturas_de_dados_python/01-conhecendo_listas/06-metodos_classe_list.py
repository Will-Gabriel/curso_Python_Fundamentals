"""
Métodos de listas
"""

lista = []

# =========================================================================
print("============ Exemplo com método .append() ============")

print(f"Lista antes de aplicar o .append(): {lista}")

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(f"Lista depois de aplicar o .append(): {lista}")


# =========================================================================
print("\n============ Exemplo com método .clear() ============")

print(f"Lista antes de aplicar o .clear(): {lista}")

lista.clear()

print(f"Lista depois de aplicar o .clear(): {lista}")


# =========================================================================
print("\n============ Exemplo com método .copy() ============")

lista = [1, "Python", [40, 30, 20]]
lista2 = lista.copy()

print(f"Lista 1: {lista}")
print(f"Lista 2 depois de aplicar o .copy(): {lista2} - {id(lista2)}")
print(f"ID lista 1: {id(lista)}")
print(f"ID lista 2: {id(lista2)}")


# =========================================================================
print("\n============ Exemplo com método .count() ============")

cores = ["vermelho", "azul", "verde", "azul"]

vermelho = cores.count("vermelho")
azul = cores.count("azul")
verde = cores.count("verde")

print(f"Cores na lista: {cores}\n")
print(f"Qtd de vermelho na lista: {vermelho}")
print(f"Qtd de azul na lista: {azul}")
print(f"Qtd de verde na lista: {verde}")


# =========================================================================
print("\n============ Exemplo com método .extend() ============")

linguagens = ["Python", "Javascript", "Csharp"]

print(f"Lista antes de aplicar o .extend(): {linguagens}")

linguagens.extend(["Java", "C++"])

print(f"Lista depois de aplicar o .extend(): {linguagens}")


# =========================================================================
print("\n============ Exemplo com método .index() ============")

linguagens = ["Python", "Javascript", "Csharp", "Java", "C++"]

print(f"Linguagens: {linguagens}\n")
print(f"Index de Java: {linguagens.index("Java")}")
print(f"Index de Python: {linguagens.index("Python")}")


# =========================================================================
print("\n============ Exemplo com método .pop() ============")

linguagens = ["Python", "Javascript", "Csharp", "Java", "C++"]

print(f"Linguagens antes de aplicar .pop(): {linguagens}\n")

qtd_linguagens = len(linguagens)
i = 0

while qtd_linguagens:
    i += 1
    if len(linguagens) == 0:
        break
    else:
        linguagens.pop()
        print(f"Linguagens depois de aplicar .pop() {i} vez: {linguagens}")


# =========================================================================
print("\n============ Exemplo com método .remove() ============")

linguagens = ["Python", "Javascript", "Csharp", "Java", "C++"]

print(f"Lista antes de aplicar o .remove(): {linguagens}")

linguagens.remove("C++")

print(f"Lista depois de aplicar o .remove(): {linguagens}")


# =========================================================================
print("\n============ Exemplo com método .reverse() ============")

linguagens = ["Python", "Javascript", "Csharp", "Java", "C++"]

print(f"Lista antes de aplicar o .reverse(): {linguagens}")

linguagens.reverse()

print(f"Lista depois de aplicar o .reverse(): {linguagens}")


# =========================================================================
print("\n============ Exemplo com método .sort() ============")

linguagens = ["Python", "Js", "C", "Java", "C++"]

print(f"Lista antes de aplicar o .sort(): {linguagens}\n")

lista_teste = linguagens.copy()
lista_teste.sort(reverse=True)
print(f"Lista depois de aplicar o .sort() com reverse: {lista_teste}")

lista_teste2 = linguagens.copy()
lista_teste2.sort(key=lambda x: len(x))
print(f"Lista depois de aplicar o .sort() com lambda: {lista_teste2}")

lista_teste3 = linguagens.copy()
lista_teste3.sort(key=lambda x: len(x), reverse=True)
print(f"Lista depois de aplicar o .sort() com lambda e reverse: {lista_teste3}")


# =========================================================================
print("\n============ Exemplo com método .len() ============")

linguagens = ["Python", "Js", "C", "Java", "C++"]

print(f"Tamanho da lista com .len(): {len(linguagens)}")


# =========================================================================
print("\n============ Exemplo com método .sorted() ============")

linguagens = ["Python", "Js", "C", "Java", "C++"]

print(f"Lista antes de aplicar o .sorted(): {linguagens}\n")

lista_teste = linguagens.copy()
print(f"Lista depois de aplicar o .sorted() com lambda: {sorted(lista_teste, key=lambda x: len(x))}")

lista_teste2 = linguagens.copy()
print(f"Lista depois de aplicar o .sorted() com lambda e reverse: {sorted(lista_teste, key=lambda x: len(x), reverse=True)}")
