## Questões e minhas resoluções

Questão 1:

Um sistema de gerenciamento de tarefas precisa processar solicitações de forma ordenada, onde a primeira solicitação a chegar é a primeira a ser atendida. Além disso, para exibir uma lista de itens em um painel, é necessário organizar esses itens realizando comparações e trocas sucessivas entre elementos adjacentes até que a lista esteja completamente ordenada.

Descreva as operações fundamentais para adicionar e remover elementos da estrutura que gerencia as solicitações e explique o princípio básico do algoritmo de ordenação que realiza trocas adjacentes.

R:

```python

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, dado):
        self.items.insert(0, dado)

    def dequeue(self):
        self.items.pop()

```

O método de ordenação mencionado é o bubble sort. Ao executar, ele garante que a cada iteração o maior peso da lista fique na ultima posição, e por isso, não compara ela na próxima iteração. O maior problema é caso a lista esteja inversamente ordenada, pois é o pior cenário para esse algoritmo.

---

Questão 2:

Um sistema de edição de texto mantém um histórico das últimas ações realizadas pelo usuário, permitindo que ele desfaça operações na ordem inversa em que foram executadas. Para otimizar a exibição de grandes conjuntos de dados, um módulo de ordenação é utilizado, que divide a lista em sublistas menores, ordena-as e depois as combina.

Descreva a estrutura de dados mais adequada para o histórico de ações e as operações básicas para adicionar e remover ações. Em seguida, explique o processo de combinação de sublistas ordenadas no algoritmo de ordenação mencionado.

R:

```python

class Stack:
    def __init__(self):
        self.items = []
    def push(self,dado):
        self.items.append(dado)
    def pop(self):
        self.items.pop()

```

O algoritmo mencionado é o merge sort. Ele divide a lista em duas partes e recursivamente vai dividindo a metade de cada uma até ficarem indivisíveis, nesse momento ocorre o processo de estar comparando uma parte com a outra, estar ordenando e só depois unindo novamente, realizando esse processo em cascada até a ordenação completa da lista.

---

Questão 3:

Em um sistema de gerenciamento de documentos, é comum que arquivos sejam adicionados para processamento e devam ser tratados na ordem em que foram recebidos. Além disso, para manter um registro de acesso rápido aos últimos documentos abertos, uma estrutura que permite adicionar e remover itens de forma sequencial é utilizada.

Explique como a estrutura de dados que processa os documentos garante que o primeiro a entrar seja o primeiro a sair e como a estrutura de registro de acesso rápido pode ser implementada usando uma lista em Python, demonstrando as operações de adição e remoção.

R:
A estrutura de dados aplicada deverá ser a fila, onde os dados que chegam são adicionados no fim da fila e são retirados do inicio, tornando possível, o processamento na ordem inserida.

A maneira mais simples de se obter um registro ou acesso fácil é por meio de uma lista simples, onde basta obter o valor do índice a se consultar, podendo ser realizado da seguinte forma:

```python

class List:
    def __init__(self):
        self.items = []
    def push(self, dado):
        self.items.push(dado)
    def pop(self, i):
        self.items.pop(i)

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, dado):
        self.items.insert(0, dado)
    def dequeue(self):
        self.items.pop()

l = List()

l.push('dado de valor 0') # vai ser apagado ao usar o l.pop()
l.push('outro valor de valor 1')
l.pop(0)

```

Enquanto a `Queue` é responsável pelo gerenciamento de documentos, a `List` fica responsável pela criação de uma lista que vai sempre adicionando os items no final e para remover algo, basta ter o valor do índice a se excluir.

---

Questão 4:

Em um sistema de controle de estoque, os produtos são armazenados em uma lista e, periodicamente, essa lista precisa ser organizada para facilitar a localização. Um método de organização envolve percorrer a lista e, em cada passo, encontrar o menor elemento restante e colocá-lo na posição correta. Além disso, o sistema precisa gerenciar uma sequência de operações de entrada e saída de produtos, onde a ordem de chegada é crucial para o processamento.

Explique o processo de encontrar e posicionar o menor elemento no algoritmo de ordenação e como a estrutura de dados que gerencia as operações de entrada e saída garante a ordem de processamento.

R:

```python

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]
                min_index = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

```

O selection sort é como se fosse um baralho de cartas, onde é necessário percorrer todo o baralho procurando o menor valor, e quando encontrar mover ao inicio das cartas e depois fazer o mesmo para a segunda carta em diante. Esse processo acaba sendo não muito eficiente em um cenário em que já tem uma quantidade de itens ordenados.

Onde a ordem de chegada é crucial, a estrutura para o contexto é uma fila, ela garante que as operações que chegarem primeiro vão ser processadas primeiro, pois segue o principio de FIFO.

---

Questão 5:

Um sistema de gerenciamento de chamados de suporte técnico processa as solicitações na ordem de chegada. Para organizar uma lista de clientes, um algoritmo de ordenação insere cada elemento em sua posição correta na parte já ordenada da lista.

Qual operação é utilizada para adicionar um novo chamado ao sistema de suporte?

A) A operação enqueue adiciona o novo chamado ao final da fila.

B) A operação push insere o novo chamado no topo da pilha.

C) A operação dequeue remove o chamado mais antigo do início.

D) A operação pop extrai o último chamado inserido da pilha.

E) A operação sort organiza todos os chamados em ordem alfabética.

Questão 6:

Um navegador web mantém um histórico de páginas visitadas, permitindo que o usuário retorne à página anterior. Para otimizar a exibição de grandes listas de resultados de busca, um algoritmo de ordenação divide a lista em duas metades, ordena cada metade e depois as combina.

Qual operação é utilizada para adicionar uma nova página ao histórico do navegador?

A) A operação push insere a nova página no topo da estrutura de histórico.

B) A operação enqueue adiciona a nova página ao final da sequência de histórico.

C) A operação pop remove a página mais recente do topo do histórico.

D) A operação dequeue extrai a página mais antiga do início da sequência.

E) A operação partition reorganiza as páginas em torno de um pivô.

Questão 7:

Um sistema de filas de atendimento em um banco processa os clientes na ordem de chegada. Para exibir uma lista de transações, o sistema precisa organizá-las, e para isso, utiliza um algoritmo que encontra o menor elemento em cada iteração e o coloca na posição correta.

Qual estrutura de dados é mais adequada para gerenciar a fila de clientes no banco?

A) A estrutura de Fila, pois processa os clientes na ordem de chegada.

B) A estrutura de Pilha, pois atende o último cliente que chegou primeiro.

C) A estrutura de Lista, pois permite acesso aleatório a qualquer cliente.

D) A estrutura de Árvore, pois organiza os clientes em uma hierarquia.

E) A estrutura de Grafo, pois representa as conexões entre os clientes.

Questão 8:

Um sistema de controle de acesso a um recurso compartilhado permite que apenas o último processo a solicitar o recurso o utilize primeiro. Para organizar uma lista de tarefas, o sistema utiliza um algoritmo que encontra o menor elemento em cada iteração e o coloca na posição correta.

Qual operação é utilizada para remover o processo que está atualmente utilizando o recurso?

A) A operação pop remove o último processo que foi adicionado à pilha.

B) A operação dequeue extrai o processo mais antigo que foi adicionado.

C) A operação push insere um novo processo no topo da estrutura.

D) A operação enqueue adiciona um novo processo ao final da fila.

E) A operação select escolhe um processo aleatoriamente da lista.

---

Questão 9:

Em um sistema de processamento de dados, uma lista de números precisa ser organizada. Um algoritmo de ordenação realiza a divisão da lista em duas metades, ordena cada metade de forma independente e, em seguida, combina as sublistas ordenadas.

Qual é a etapa fundamental que ocorre após a divisão da lista em sublistas no algoritmo de ordenação?

A) A etapa de mesclagem combina as sublistas ordenadas em uma única lista.

B) A etapa de particionamento reorganiza elementos em torno de um pivô.

C) A etapa de troca move elementos adjacentes para suas posições corretas.

D) A etapa de inserção coloca cada elemento em sua posição final.

E) A etapa de seleção encontra o menor elemento e o posiciona.

---

Questão 10:

Um sistema de processamento de eventos em tempo real precisa lidar com eventos na ordem exata em que ocorrem. Para manter um registro temporário de eventos recentes, uma estrutura que permite adicionar e remover itens de forma sequencial é utilizada.

Qual operação é utilizada para adicionar um novo evento a essa estrutura de registro temporário?

A) A operação append adiciona o novo evento ao final da lista de registros.

B) A operação insert coloca o evento em uma posição específica da lista.

C) A operação pop remove o último evento que foi adicionado à lista.

D) A operação remove exclui um evento específico da lista de registros.

E) A operação sort organiza todos os eventos em ordem cronológica.

---

Questão 11:

Um sistema de gerenciamento de processos em um sistema operacional precisa lidar com a execução de tarefas, onde algumas tarefas têm prioridade sobre outras. No entanto, para garantir que tarefas de mesma prioridade sejam executadas na ordem de chegada, uma fila é utilizada. Para otimizar a organização de grandes volumes de dados, um algoritmo de ordenação é empregado, que divide a lista em sublistas, ordena-as recursivamente e depois as combina.

Descreva como uma fila pode ser implementada em Python para gerenciar tarefas de mesma prioridade, garantindo a ordem de chegada, e explique o processo recursivo de divisão da lista no algoritmo de ordenação.


R:
Tendo em mente que na fila haverá a execução por prioridade, é necessário modificar um pouco os métodos de `enqueue` e `dequeue` para garantir que além de estar tendo o comportamento de um fila, possua uma adição e subtração dos processos. 

Para tal, precisaremos de uma estrutura auxiliar para armazenar o nome do processo e a prioridade. A qual vai ser utilizada no método `enqueue`.

```python

class Element:
    def __init__(self, valor, prioridade):
        self.item = valor
        self.prioridade = prioridade


class PriorityQueue:
    def __init__(self):
        self.items = []
    def enqueue(self, item, prioridade):
        ele = Element(item, prioridade)
        self.items.insert(0, ele)
        print("Elemento inserido")
    def dequeue(self):
        if self.items == []:
            print("Lista vazia. Preencha primeiro.")
            return
        posicao = 0
        menor = self.items[posicao].prioridade
        for i in range( len(self.items) ):
            if self.items[i].prioridade <= menor:
                posicao = i
                menor = self.items[i].prioridade
        removido = self.items.pop(posicao)
        print("Elemento removido: ", removido.item)        

```

Dessa maneira, já é possível estar tendo o comportamento de fila com prioridade.


O algoritmo mencionado é o merge sort, o qual divide uma lista no meio e vai fazendo esse processo recursivamente até só restar um elemento. 
Exemplo ( [quantidade de elementos] 8 -> 4 - 4 -> 2 - 2 -- 2 - 2 -> 1 - 1 -- 1 - 1 --- 1 - 1 -- 1 - 1)

Após a ultima etapa de divisão, ocorre a comparação com o seu respectivo par, a ordenação se necessário e por fim a junção, e esse processo ocorre em cascata também devido a natureza da recursividade.



---

Questão 12:

Um sistema de controle de versão de software utiliza uma estrutura para armazenar as diferentes versões de um arquivo, permitindo que o desenvolvedor retorne a qualquer versão anterior. Para otimizar a organização de uma lista de arquivos por nome, um algoritmo de ordenação é empregado, que percorre a lista várias vezes, comparando e trocando elementos adjacentes.

Descreva como uma Pilha pode ser implementada em Python para gerenciar as versões de um arquivo, incluindo as operações de adicionar e recuperar a versão mais recente. Em seguida, explique o processo de troca de elementos adjacentes no algoritmo de ordenação.

---

Questão 13:

Um sistema de processamento de imagens precisa organizar uma coleção de imagens por tamanho. Para isso, utiliza um algoritmo de ordenação que divide a coleção em subconjuntos, ordena cada um e depois os combina. Além disso, o sistema mantém um registro de operações recentes, onde a ordem de execução é importante para auditoria.

Explique o papel do pivô no processo de particionamento de um algoritmo de ordenação que divide a lista em sublistas e como uma lista em Python pode ser utilizada para manter um registro de operações recentes, demonstrando a adição e remoção de operações.

R:
O pivô serve como ponto de partida para encontrar valores menores e maiores que o escolhido. Após isso, os menores ficam de um lado e são comparados entre si com outro pivô até serem ordenados. Após o retorno, o outro lado é comparado, ordenado e, por fim, a lista é juntada.


Os registros podem ser armazenados em uma lista ligada, como a seguinte:

```python

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class ListaLigada:
    def __init__(self):
        self.inicio_lista = None
        self.fim_lista = None
    
    def esta_vazia(self):
        return self.inicio_lista == None
    
    def adicionar_fim(self, dado):
        no = Node(dado)
        if self.esta_vazia():
            self.inicio_lista = no
            self.fim_lista = no
        else:
            self.fim_lista.proximo = no
            self.fim_lista = no

    def adicionar_inicio(self, dado):
        no = Node(dado)
        if self.esta_vazia():
            self.inicio_lista = no
            self.fim_lista = no
        else:
            self.inicio_lista.proximo = no        
            self.inicio_lista = no        
            
    def remover_inicio(self):
        if self.esta_vazia():
            return
        self.inicio_lista = self.inicio_lista.proximo
        if self.inicio_lista == None:
            self.fim_lista == None
    
    def remover_fim(self):
        if self.esta_vazia():
            return
        if self.inicio_lista == self.fim_lista:
            self.inicio_lista = None
            self.fim_lista = None
        else:
            atual = self.inicio_lista
            while atual and atual.proximo != self.fim_lista:
                atual = atual.proximo
            atual.proximo = None
            self.fim_lista = atual

```

---

Questão 14:

Um sistema de gerenciamento de documentos precisa manter um histórico das últimas modificações realizadas em um arquivo, permitindo que o usuário visualize a sequência de alterações. Para otimizar a exibição de grandes listas de documentos, um algoritmo de ordenação é empregado, que percorre a lista e, em cada passo, insere o elemento atual em sua posição correta na parte já ordenada da lista.

Descreva como uma Pilha pode ser implementada em Python para gerenciar o histórico de modificações, incluindo as operações de adicionar e consultar a modificação mais recente. Em seguida, explique o processo de inserção de um elemento em sua posição correta no algoritmo de ordenação.

R:

```python

class Pilha:
    def __init__(self):
        self.historico = []
    def pop(self):
        self.historico.pop()
    def push(self, doc):
        self.historico.append(doc)
    def esta_vazia(self):
        return self.historico == []
    def peek(self):
        return self.historico[ len(self.historico) - 1 ]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

```

Questão 15:

Um sistema de processamento de dados precisa organizar uma lista de registros. Para isso, utiliza um algoritmo que divide a lista em sublistas, ordena cada uma recursivamente e depois as combina. Em um cenário de gerenciamento de tarefas, é necessário que as tarefas sejam executadas na ordem de chegada.

Qual é a operação que combina as sublistas ordenadas no algoritmo de ordenação?

A) A operação de mesclagem combina as sublistas ordenadas em uma única lista.

B) A operação de particionamento reorganiza elementos em torno de um pivô.

C) A operação de troca move elementos adjacentes para suas posições corretas.

D) A operação de inserção coloca cada elemento em sua posição final.

E) A operação de seleção encontra o menor elemento e o posiciona.

Questão 16:

Um sistema de processamento de eventos precisa registrar a sequência de ocorrências, permitindo que o último evento registrado seja o primeiro a ser analisado. Para organizar uma lista de eventos por data, um algoritmo de ordenação percorre a lista e, em cada passo, encontra o menor elemento restante e o coloca na posição correta.

Qual operação é utilizada para adicionar um novo evento a essa estrutura de registro?

A) A operação push insere o novo evento no topo da estrutura de registro.

B) A operação enqueue adiciona o novo evento ao final da sequência de registro.

C) A operação pop remove o evento mais recente do topo do registro.

D) A operação dequeue extrai o evento mais antigo do início da sequência.

E) A operação find localiza um evento específico dentro da lista.

Questão 17:

Um sistema de gerenciamento de tarefas precisa processar as tarefas na ordem de chegada. Para otimizar a organização de uma lista de tarefas, um algoritmo de ordenação divide a lista em sublistas, ordena cada uma recursivamente e depois as combina.

Qual é a operação que remove a próxima tarefa a ser processada do sistema?

A) A operação dequeue remove a próxima tarefa do início da fila.

B) A operação pop extrai a última tarefa adicionada do topo da pilha.

C) A operação enqueue adiciona uma nova tarefa ao final da fila.

D) A operação push insere uma nova tarefa no topo da pilha.

E) A operação merge combina duas listas de tarefas ordenadas.

Questão 18:

Um sistema de controle de estoque precisa organizar uma lista de produtos por código. Para isso, utiliza um algoritmo de ordenação que percorre a lista e, em cada passo, encontra o menor elemento restante e o coloca na posição correta. Além disso, o sistema mantém um registro de operações recentes, onde a ordem de execução é importante para auditoria.

Qual é a etapa fundamental do algoritmo de ordenação que encontra o menor elemento?

A) A etapa de seleção encontra o menor elemento na parte não ordenada da lista.

B) A etapa de particionamento reorganiza elementos em torno de um pivô.

C) A etapa de troca move elementos adjacentes para suas posições corretas.

D) A etapa de inserção coloca cada elemento em sua posição final.

E) A etapa de mesclagem combina as sublistas ordenadas em uma única lista.

Questão 19:

Um sistema de gerenciamento de documentos precisa organizar uma lista de arquivos por nome. Para isso, utiliza um algoritmo de ordenação que divide a lista em sublistas, ordena cada uma recursivamente e depois as combina. Em um cenário de processamento de dados, é necessário que os dados sejam processados na ordem de chegada.

Qual é a operação que reorganiza os elementos em torno de um pivô no algoritmo de ordenação?

R:


---

Questão 20:

Um sistema de gerenciamento de tarefas precisa processar as tarefas na ordem de chegada. Para otimizar a organização de uma lista de tarefas, um algoritmo de ordenação insere cada elemento em sua posição correta na parte já ordenada da lista.

Qual é a operação que adiciona uma nova tarefa ao sistema de gerenciamento?

A) A operação enqueue adiciona a nova tarefa ao final da fila de tarefas.

B) A operação push insere a nova tarefa no topo da pilha de tarefas.

C) A operação dequeue remove a tarefa mais antiga do início da fila.

D) A operação pop extrai a última tarefa adicionada do topo da pilha.

E) A operação merge combina duas listas de tarefas ordenadas.

Questão 21:

Um sistema de processamento de transações financeiras precisa garantir que as transações sejam executadas na ordem exata em que foram recebidas, mesmo sob alta carga. Para otimizar a organização de grandes volumes de dados de transações, um algoritmo de ordenação é empregado, que divide a lista em sublistas, ordena-as recursivamente e depois as combina.

Proponha uma implementação em Python para uma Fila de transações que suporte operações de adição e remoção eficientes, utilizando collections.deque. Em seguida, detalhe o processo de mesclagem de duas sublistas ordenadas no algoritmo de ordenação, incluindo um exemplo de como dois arrays ordenados seriam combinados.

Questão 22:

Um sistema de controle de acesso a um servidor mantém um registro das últimas 10 tentativas de login falhas, permitindo que o administrador visualize as tentativas mais recentes. Para otimizar a organização de uma lista de usuários, um algoritmo de ordenação é empregado, que percorre a lista e, em cada passo, insere o elemento atual em sua posição correta na parte já ordenada da lista.

Proponha uma implementação em Python para uma Pilha de tentativas de login falhas com capacidade limitada, utilizando uma lista padrão, e detalhe o processo de inserção de um elemento em sua posição correta no algoritmo de ordenação, incluindo um exemplo de como um elemento seria inserido em um array parcialmente ordenado.

Questão 23:

Um sistema de gerenciamento de recursos em nuvem precisa alocar máquinas virtuais de forma eficiente. Para isso, mantém uma fila de requisições de alocação, onde a primeira requisição a chegar é a primeira a ser atendida. Para otimizar a organização de uma lista de máquinas virtuais por ID, um algoritmo de ordenação é empregado, que divide a lista em sublistas, ordena-as recursivamente e depois as combina.

Proponha uma implementação em Python para uma Fila de requisições de alocação, utilizando collections.deque, e detalhe o processo de particionamento de uma lista no algoritmo de ordenação, incluindo um exemplo de como um array seria particionado ao redor de um pivô.

Questão 24:

Um sistema de monitoramento de rede precisa processar eventos de segurança na ordem exata em que foram detectados. Para otimizar a organização de uma lista de dispositivos conectados, um algoritmo de ordenação é empregado, que percorre a lista e, em cada passo, encontra o menor elemento restante e o coloca na posição correta.

Proponha uma implementação em Python para uma Fila de eventos de segurança, utilizando collections.deque, e detalhe o processo de seleção do menor elemento e sua troca para a posição correta no algoritmo de ordenação, incluindo um exemplo de como um array seria ordenado usando esse método.

Questão 25:

Um sistema de gerenciamento de pedidos em um e-commerce precisa processar os pedidos na ordem de chegada. Para otimizar a organização de uma lista de produtos, um algoritmo de ordenação é empregado, que divide a lista em sublistas, ordena cada uma recursivamente e depois as combina.

Proponha uma implementação em Python para uma Fila de pedidos, utilizando collections.deque, e detalhe o processo de mesclagem de duas sublistas ordenadas no algoritmo de ordenação, incluindo um exemplo de como dois arrays ordenados seriam combinados.

Questão 26:

Um sistema de gerenciamento de processos em um sistema operacional precisa lidar com a execução de tarefas, onde algumas tarefas têm prioridade sobre outras. No entanto, para garantir que tarefas de mesma prioridade sejam executadas na ordem de chegada, uma fila é utilizada. Para otimizar a organização de grandes volumes de dados, um algoritmo de ordenação é empregado, que divide a lista em sublistas, ordena-as recursivamente e depois as combina.

Proponha uma implementação em Python para uma Fila de tarefas que suporte operações de adição e remoção eficientes, utilizando collections.deque. Em seguida, detalhe o processo de mesclagem de duas sublistas ordenadas no algoritmo de ordenação, incluindo um exemplo de como dois arrays ordenados seriam combinados.

Questão 27:

Um sistema de gerenciamento de dados precisa organizar uma lista de registros. Para isso, utiliza um algoritmo de ordenação que divide a lista em sublistas, ordena cada uma recursivamente e depois as combina. Em um cenário de processamento de dados, é necessário que os dados sejam processados na ordem de chegada.

Proponha uma implementação em Python para uma Fila de dados que suporte operações de adição e remoção eficientes, utilizando collections.deque. Em seguida, detalhe o processo de mesclagem de duas sublistas ordenadas no algoritmo de ordenação, incluindo um exemplo de como dois arrays ordenados seriam combinados.

Questão 28:

Um sistema de gerenciamento de processos em um sistema operacional precisa lidar com a execução de tarefas, onde algumas tarefas têm prioridade sobre outras. No entanto, para garantir que tarefas de mesma prioridade sejam executadas na ordem de chegada, uma fila é utilizada. Para otimizar a organização de grandes volumes de dados, um algoritmo de ordenação é empregado, que divide a lista em sublistas, ordena-as recursivamente e depois as combina.

Qual é a operação que combina as sublistas ordenadas no algoritmo de ordenação?

A) A operação de mesclagem combina as sublistas ordenadas em uma única lista.

B) A operação de particionamento reorganiza elementos em torno de um pivô.

C) A operação de troca move elementos adjacentes para suas posições corretas.

D) A operação de inserção coloca cada elemento em sua posição final.

E) A operação de seleção encontra o menor elemento e o posiciona.

Questão 29:

Um sistema de controle de acesso a um servidor mantém um registro das últimas 10 tentativas de login falhas, permitindo que o administrador visualize as tentativas mais recentes. Para otimizar a organização de uma lista de usuários, um algoritmo de ordenação é empregado, que percorre a lista e, em cada passo, insere o elemento atual em sua posição correta na parte já ordenada da lista.

Qual operação é utilizada para adicionar uma nova tentativa de login falha a essa estrutura de registro?

A) A operação append adiciona a nova tentativa ao final da lista de registros.

B) A operação insert coloca a tentativa em uma posição específica da lista.

C) A operação pop remove a última tentativa que foi adicionada à lista.

D) A operação remove exclui uma tentativa específica da lista de registros.

E) A operação sort organiza todas as tentativas em ordem cronológica.

Questão 30:

Um sistema de gerenciamento de recursos em nuvem precisa alocar máquinas virtuais de forma eficiente. Para isso, mantém uma fila de requisições de alocação, onde a primeira requisição a chegar é a primeira a ser atendida. Para otimizar a organização de uma lista de máquinas virtuais por ID, um algoritmo de ordenação é empregado, que divide a lista em sublistas, ordena-as recursivamente e depois as combina.

Qual é a operação que remove a próxima requisição a ser atendida do sistema?

A) A operação dequeue remove a próxima requisição do início da fila.

B) A operação pop extrai a última requisição adicionada do topo da pilha.

C) A operação enqueue adiciona uma nova requisição ao final da fila.

D) A operação push insere uma nova requisição no topo da pilha.

E) A operação merge combina duas listas de requisições ordenadas.

Questão 31:

Um sistema de monitoramento de rede precisa processar eventos de segurança na ordem exata em que foram detectados. Para otimizar a organização de uma lista de dispositivos conectados, um algoritmo de ordenação é empregado, que percorre a lista e, em cada passo, encontra o menor elemento restante e o coloca na posição correta.

Qual é a etapa fundamental do algoritmo de ordenação que encontra o menor elemento?

A) A etapa de seleção encontra o menor elemento na parte não ordenada da lista.

B) A etapa de particionamento reorganiza elementos em torno de um pivô.

C) A etapa de troca move elementos adjacentes para suas posições corretas.

D) A etapa de inserção coloca cada elemento em sua posição final.

E) A etapa de mesclagem combina as sublistas ordenadas em uma única lista.

Questão 32:

Um sistema de gerenciamento de dados precisa organizar uma lista de registros. Para isso, utiliza um algoritmo de ordenação que divide a lista em sublistas, ordena cada uma recursivamente e depois as combina. Em um cenário de processamento de dados, é necessário que os dados sejam processados na ordem de chegada.

Qual é a operação que reorganiza os elementos em torno de um pivô no algoritmo de ordenação?

A) A operação de particionamento reorganiza elementos em torno de um pivô.

B) A operação de mesclagem combina as sublistas ordenadas em uma única lista.

C) A operação de troca move elementos adjacentes para suas posições corretas.

D) A operação de inserção coloca cada elemento em sua posição final.

E) A operação de seleção encontra o menor elemento e o posiciona.
