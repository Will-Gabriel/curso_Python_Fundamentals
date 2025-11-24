"""
São estruturas utilizadas para repetir um trecho de código um determinado
número de vezes. Esse número pode ser conhecido previamente ou determinado
através de uma expressão lógica.

for - é usado para percorrer um objeto iterável. Faz sentido usar quando
sabemos o número extato de vezes que nosso bloco de código deve ser executado,
ou quando queremos percorrer um objeto iterável.]

função range - uma função built-in do Python, ela é usada para produzir uma 
sequência de números inteiros a partir de um ínicio (inclusivo) para 
um fim (exclusivo). Se usarmos range(i, j) será reproduzido:
    i, i+1, i+2, i+3, ..., j-1
Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional).
"""

# =========================================================================
print("\n====== Exemplo sem repetição ======")

numero = int(input("Informe um número inteiro: "))
print(numero)

numero += 1
print(numero)

numero += 1
print(numero)

# =========================================================================
print("\n====== Exemplo com repetição com for ======")

texto = input("Informe um texto: ").strip().upper()
VOGAIS = "AEIOU"

print("\nVogais no texto informado:")
for letra in texto:
    if letra in VOGAIS:
        print(f"{letra}", end=" ")

print()

# =========================================================================
print("\n====== Exemplo com for com else ======")

texto = input("Informe um texto: ").strip().upper()
VOGAIS = "AEIOU"

print("\nVogais no texto informado:")
for letra in texto:
    if letra in VOGAIS:
        print(f"{letra}", end=" ")
else:
    print("Acabou o for!")

# =========================================================================
print("\n====== Exemplo com for com range ======")

for numero in range(0, 11):
    print(f"Número: {numero}")

# Exibindo a tabuada do 5
i = 0
for numero in range(0, 51, 5):
    print(f"5 x {i} = {numero}")
    i += 1
