#==========================================
print("\n====== Inteiro para Float ======")
preco = 10
print(preco, type(preco))

preco = float(preco)
print(preco, type(preco))

preco = 10 / 2
print(preco, type(preco))

#==========================================
print("\n====== Float para Inteiro ======")
preco = 10.0
print(preco, type(preco))

preco = int(preco)
print(preco, type(preco))

preco = 10 // 2
print(preco, type(preco))

#==========================================
print("\n====== Float para Str ======")
preco = 10.50
idade = 26

print(preco, type(preco))
print(idade, type(preco))

preco = str(preco)
idade = str(idade)

print(preco, type(preco))
print(idade, type(idade))


#==========================================
print("\n====== Str para Int e Float ======")
preco = "10.50"
idade = "26"

print(preco, type(preco))
print(idade, type(preco))

preco = float(preco)
idade = int(idade)

print(preco, type(preco))
print(idade, type(idade))
