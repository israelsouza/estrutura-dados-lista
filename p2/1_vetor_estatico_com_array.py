import array

# Criando um vetor estático de inteiros com tamanho definido
# Typecode 'i' = inteiro com sinal (4 bytes por elemento)
vetor_estatico = array.array('i', [0] * 5)  # 5 posições, todas zeradas

# Atribuindo valores por índice
vetor_estatico[0] = 10
vetor_estatico[1] = 20
vetor_estatico[2] = 30
vetor_estatico[3] = 40
vetor_estatico[4] = 50

# Acesso por índice — O(1)
print(f"Elemento no índice 2: {vetor_estatico[2]}")   # Saída: 30
print(f"Tamanho: {len(vetor_estatico)}")               # Saída: 5

# ERRO: tipo incompatível — vetores estáticos são homogêneos
try:
    vetor_estatico[0] = 3.14  # TypeError: inteiro esperado
except TypeError as e:
    print(f"Erro de tipo: {e}")

# ERRO: índice fora dos limites
try:
    vetor_estatico[50] = 99  # IndexError
except IndexError as e:
    print(f"Erro de índice: {e}")

