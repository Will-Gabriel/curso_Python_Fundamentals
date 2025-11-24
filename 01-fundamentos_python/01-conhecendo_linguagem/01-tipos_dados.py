"""
Tipos de Dados
"""
# ==================================================================
# Tipo int
# ==================================================================
print("Exemplos do tipo INT:")
num_int = 10
num_int2 = 10 + 2
num_int3 = 10 - 2
num_int4 = 10 * 2
num_int5 = 10 // 3

print(f"- Número: {num_int} - Tipo {type(num_int)}")
print(f"- Soma: 10 + 2 = {num_int2} - Tipo {type(num_int2)}")
print(f"- Subtração: 10 - 2 = {num_int3} - Tipo {type(num_int3)}")
print(f"- Multiplicação: 10 * 2 = {num_int4} - Tipo {type(num_int4)}")
print(f"- Divisão Inteira: 10 // 3 = {num_int5} - Tipo {type(num_int5)}")

# ==================================================================
# Tipo float
# ==================================================================
print("\nExemplos do tipo FLOAT:")
num_float = 10.5
num_float2 = 10 + 2.5
num_float3 = 10 - 2.5
num_float4 = 10 * 2.5
num_int5 = 10 / 3

print(f"- Número: {num_float} - Tipo {type(num_float)}")
print(f"- Soma: 10 + 2.5 = {num_float2} - Tipo {type(num_float2)}")
print(f"- Subtração: 10 - 2.5 = {num_float3} - Tipo {type(num_float3)}")
print(f"- Multiplicação: 10 * 2.5 = {num_float4} - Tipo {type(num_float4)}")
print(f"- Divisão: 10 / 3 = {num_int5} - Tipo {type(num_int5)}")

# ==================================================================
# Tipo Boolean
# ==================================================================
print("\nExemplos do tipo BOOLEAN:")
falso = False
verdadeiro = True

print(f"- Falso: {falso} - Tipo {type(falso)}")
print(f"- Verdadeiro: {verdadeiro} - Tipo {type(verdadeiro)}")

# ==================================================================
# Tipo String
# ==================================================================
print("\nExemplos do tipo STRING:")
aspas_duplas = '"Isso é uma string"'
aspas_simples = "'Isso é uma string'"
tres_apas_duplas = '"""Isso é uma string"""' 
tres_apas_simples = "'''Isso é uma string'''"

print(f"- {aspas_duplas} - Tipo: {type(aspas_duplas)}")
print(f'- {aspas_simples} - Tipo: {type(aspas_simples)}')
print(f"- {tres_apas_duplas} - Tipo: {type(tres_apas_duplas)}")
print(f'- {tres_apas_simples} - Tipo: {type(tres_apas_simples)}')
