import ctypes
class DynamicArray:
    """Vetor dinâmico similar à list do Python."""
    def __init__(self):
        self._n = 0          # elementos reais
        self._capacity = 1   # capacidade inicial
        self._A = self._make_array(self._capacity)
    def __len__(self):
        return self._n
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('índice inválido')
        return self._A[k]
    def _make_array(self, c):
        """Aloca array de capacidade c usando ctypes."""
        return (c * ctypes.py_object)()
    
    def _resize(self, c):
        """
        Realoca o array interno para nova capacidade c.
        Complexidade: O(n) — copia todos os elementos.
        """
        B = self._make_array(c)          # novo array maior
        for k in range(self._n):         # copia elementos
            B[k] = self._A[k]
        self._A = B                       # substitui referência
        self._capacity = c                # atualiza capacidade

    @property
    def capacity(self):
        return self._capacity
    
    def append(self, obj):
        """
        Insere elemento no final.
        Amortizado: O(1)
        Pior caso: O(n) quando resize
        """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def remove(self, value):
        """
        Remove a primeira ocorrência de value.
        Complexidade: O(n) — busca + deslocamento.
        Lança ValueError se não encontrado.
        """
        for k in range(self._n):
            if self._A[k] == value:
                if self._A[k] == value:
                    for j in range(k, self._n - 1):
                        self._A[j] = self._A[j + 1]
                    self._A[self._n - 1] = None  # libera referência
                    self._n -= 1
                    # Opcional: encolher se uso < 25%
                    if 0 < self._n < self._capacity // 4:
                        self._resize(self._capacity // 2)
                    return
        raise ValueError(f'{value} not found')
    
    class Aluno:
        def __init__(self, nome, matricula):
            self.nome = nome
            self.matricula = matricula
        def __repr__(self):
            return f'Aluno({self.nome}, {self.matricula})'
        
# Vetor de objetos
turma = DynamicArray()
# Note: como Aluno está dentro de DynamicArray, acessamos assim:
turma.append(DynamicArray.Aluno('Ana', '2024001'))
turma.append(DynamicArray.Aluno('Bruno', '2024002'))
turma.append(DynamicArray.Aluno('Carla', '2024003'))
# # Acesso e modificação
print(turma[0])           # Aluno(Ana, 2024001)
turma[0].nome = 'Anaís'  # modifica objeto original
print(turma[0])           # Aluno(Anaís, 2024001)
