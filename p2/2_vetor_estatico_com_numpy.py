import numpy as np
# Criando vetor estático com numpy — dtype fixo, shape controlado
vetor_np = np.zeros(5, dtype=np.int32)  # 5 inteiros de 32 bits
print(f"Shape: {vetor_np.shape}")       # (5,)
print(f"Dtype: {vetor_np.dtype}")       # int32
print(f"Bytes totais: {vetor_np.nbytes}") # 20 bytes (5 x 4)

# Atribuição por índice — O(1)
vetor_np[0] = 100
vetor_np[1] = 200
vetor_np[4] = 500
print(vetor_np)  # [100 200   0   0 500]

# Fatiamento (slicing) — retorna view, não cópia
fatia = vetor_np[1:4]
print(fatia)     # [200   0   0]

# Operações vetorizadas — muito mais rápidas que laços
vetor_np2 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
resultado = vetor_np2 * 2
print(resultado)  # [2 4 6 8 10]

# Tentativa de redimensionar — shape fixo
# vetor_np.resize((10,)) — levanta erro em views
vetor_np_fixo = vetor_np.copy()
vetor_np_fixo.flags.writeable = True  # controle de imutabilidade
