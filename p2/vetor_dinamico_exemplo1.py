"""
implemente uma função que receba um vetor dinâmico (list) e retorne o número de realocações necessárias para inserir nelementos, assumindo que 
a capacidade dobra a cada realocação. Calcule também a complexidade total de cópias realizadas.
"""

import math
def contar_realocacoes(n: int, capacidade_inicial: int = 1) -> dict:
    """
    Conta realocações e cópias ao inserir n elementos.
    Retorna dicionário com estatísticas completas.
    """
    capacidade = capacidade_inicial
    realocacoes = 0
    total_copias = 0
    historico = []
    while capacidade < n:
        total_copias += capacidade   # copia todos os elementos atuais
        capacidade *= 2              # dobra a capacidade
        realocacoes += 1
        historico.append(capacidade)
    return {
        "realocacoes": realocacoes,
        "total_copias": total_copias,
        "capacidade_final": capacidade,
        "historico": historico
    }
# Testando para n = 100 elementos
resultado = contar_realocacoes(100)
print(f"Realocações: {resultado['realocacoes']}")     # 7
print(f"Total cópias: {resultado['total_copias']}")   # 127
print(f"Capacidade final: {resultado['capacidade_final']}") # 128
print(f"Histórico: {resultado['historico']}")
# Prova matemática: total cópias = 2^k - 1 ≈ n → O(n) amortizado


# O número de realocações é log₂(n). O total de cópias é sempre < 2n, provando que o custo amortizado de inserção é O(1).
