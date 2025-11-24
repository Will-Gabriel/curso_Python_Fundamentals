"""
Métodos do sets.
"""

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# =========================================================================
print("============ Exemplo método .union() ============")

# conjunto_c = conjunto_a.union(conjunto_b)

print(f"conjunto_a = {conjunto_a}")
print(f"conjunto_b = {conjunto_b}\n")
print(f"conjunto_a.union(conjunto_b) = {conjunto_a.union(conjunto_b)}")


# =========================================================================
print("\n============ Exemplo método .intersection() ============")

print(f"conjunto_a = {conjunto_a}")
print(f"conjunto_b = {conjunto_b}\n")
print(f"conjunto_a.intersection(conjunto_b) = {conjunto_a.intersection(conjunto_b)}")


# =========================================================================
print("\n============ Exemplo método .difference() ============")

print(f"conjunto_a = {conjunto_a}")
print(f"conjunto_b = {conjunto_b}\n")
print(f"conjunto_a.difference(conjunto_b) = {conjunto_a.difference(conjunto_b)}")
print(f"conjunto_b.difference(conjunto_a) = {conjunto_b.difference(conjunto_a)}")


# =========================================================================
print("\n============ Exemplo método .symmetric_difference() ============")

print(f"conjunto_a = {conjunto_a}")
print(f"conjunto_b = {conjunto_b}\n")
print(f"conjunto_a.symmetric_difference(conjunto_b) = {conjunto_a.symmetric_difference(conjunto_b)}")


# =========================================================================
print("\n============ Exemplo método .issubset() ============")

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(f"conjunto_a = {conjunto_a}")
print(f"conjunto_b = {conjunto_b}\n")
print(f"conjunto_a.issubset(conjunto_b) = {conjunto_a.issubset(conjunto_b)}")
print(f"conjunto_b.issubset(conjunto_a) = {conjunto_b.issubset(conjunto_a)}")


# =========================================================================
print("\n============ Exemplo método .issuperset() ============")

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(f"conjunto_a = {conjunto_a}")
print(f"conjunto_b = {conjunto_b}\n")
print(f"conjunto_a.issuperset(conjunto_b) = {conjunto_a.issuperset(conjunto_b)}")
print(f"conjunto_b.issuperset(conjunto_a) = {conjunto_b.issuperset(conjunto_a)}")


# =========================================================================
print("\n============ Exemplo método .isdisjoint() ============")

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(f"conjunto_a = {conjunto_a}")
print(f"conjunto_b = {conjunto_b}")
print(f"conjunto_c = {conjunto_c}\n")
print(f"conjunto_a.isdisjoint(conjunto_b) = {conjunto_a.isdisjoint(conjunto_b)}")
print(f"conjunto_a.isdisjoint(conjunto_c) = {conjunto_a.isdisjoint(conjunto_c)}")


# =========================================================================
print("\n============ Exemplo método .add() ============")

sorteio = {1, 23}

print(f"sorteio = {sorteio}\n")

sorteio.add(25)
print(f"sorteio.add(25) = {sorteio}")

sorteio.add(42)
print(f"sorteio.add(42) = {sorteio}")

sorteio.add(25)
print(f"sorteio.add(25) = {sorteio}")


# =========================================================================
print("\n============ Exemplo método .clear() ============")

sorteio = {1, 23}

print(f"sorteio = {sorteio}\n")

sorteio.clear()
print(f"sorteio.clear() = {sorteio}")



# =========================================================================
print("\n============ Exemplo método .copy() ============")

sorteio = {1, 23}

print(f"sorteio = {sorteio}\n")

sorteio2 = sorteio.copy()
print(f"sorteio2 = sorteio.copy() = {sorteio2}")


# =========================================================================
print("\n============ Exemplo método .discard() ============")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(f"numeros = {numeros}\n")

numeros.discard(1)
print(f"numeros.discard(1) = {numeros}")

numeros.discard(45)
print(f"numeros.discard(45) = {numeros}")


# =========================================================================
print("\n============ Exemplo método .pop() ============")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(f"numeros = {numeros}\n")

numeros.pop()
print(f"numeros.pop() = {numeros}")

numeros.pop()
print(f"numeros.pop() = {numeros}")


# =========================================================================
print("\n============ Exemplo método .remove() ============")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(f"numeros = {numeros}\n")
print(f"numeros.remove(0) = {numeros.remove(0)}")


# =========================================================================
print("\n============ Exemplo método .len() ============")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(f"numeros = {numeros}\n")
print(f"numeros.len(numeros) = {len(numeros)}")


# =========================================================================
print("\n============ Exemplo método 'in' ============")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(f"numeros = {numeros}\n")
print(f"1 in numeros = {1 in numeros}")
print(f"10 in numeros = {10 in numeros}")


# =========================================================================
print("\n============ Exemplo método 'not in' ============")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(f"numeros = {numeros}\n")
print(f"1 in numeros = {1 not in numeros}")
print(f"10 in numeros = {10 not in numeros}")

