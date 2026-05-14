import ctypes
class VetorDinamico:
    # Implementação educacional de vetor dinâmico com ctypes.
    def __init__(self):
        self._n = 0            # quantidade de elementos
        self._capacidade = 1   # capacidade inicial
        self._A = self._novo_array(self._capacidade)
    def __len__(self):
        return self._n
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("Índice fora do intervalo")
        return self._A[k]
    def append(self, obj):
        if self._n == self._capacidade:       # sem espaço?
            self._redimensionar(2 * self._capacidade)  # dobra!
        self._A[self._n] = obj
        self._n += 1
    def _redimensionar(self, nova_cap):
        B = self._novo_array(nova_cap)        # novo array maior
        for k in range(self._n):             # copia elementos
            B[k] = self._A[k]
        self._A = B                           # substitui referência
        self._capacidade = nova_cap
        print(f"  ↑ Realocado para capacidade {nova_cap}")
    def _novo_array(self, cap):
        return (cap * ctypes.py_object)()    # array de ponteiros C
# Teste
v = VetorDinamico()
for i in range(9):
    v.append(i * 10)
print(f"Tamanho: {len(v)}, Cap: {v._capacidade}")


