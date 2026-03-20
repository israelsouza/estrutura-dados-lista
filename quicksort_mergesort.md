## Enunciado (10 questões)

1. Implemente o algoritmo Quick Sort para ordenar uma lista de números inteiros em ordem crescente. Utilize o último elemento como pivô. 

2. Implemente o algoritmo Merge Sort para ordenar uma lista de números inteiros em ordem crescente. 

3. Modifique a implementação do Quick Sort para escolher um pivô aleatoriamente. 

4. Implemente o Merge Sort para ordenar uma lista encadeada simples. A função deve receber o nó cabeça da lista e retornar o nó cabeça da lista ordenada. 

5. Crie uma classe Produto com atributos nome (string) e preco (float). Implemente o Quick Sort para ordenar uma lista de objetos Produto primeiramente por preco (crescente) e, em caso de preços iguais, por nome (alfabética crescente). 

6. Implemente o Merge Sort para ordenar uma lista de strings em ordem alfabética crescente. 

7. Implemente o Quick Sort utilizando a "mediana de três" como estratégia para escolher o pivô. Isso envolve selecionar o elemento do meio, o primeiro e o último, e usar a mediana desses três como pivô, trocando-o para a posição final antes do particionamento. 

8. Ordene uma lista de tuplas (idade, nome) usando Merge Sort. A ordenação deve ser primariamente por idade (crescente) e secundariamente por nome (alfabética crescente) para idades iguais. 

9. Implemente o Quick Sort de forma iterativa (não recursiva) usando uma pilha explícita para gerenciar as chamadas de partição. Isso pode ajudar a evitar estouro de pilha para listas muito grandes. 

10. Simule a ordenação de um arquivo muito grande que não cabe na memória RAM. Implemente uma versão simplificada de Merge Sort externo que lê blocos do arquivo, os ordena na memória e os grava em arquivos temporários, para depois mesclar esses arquivos temporários. 