#fila utilizada na busca
from queue import PriorityQueue
from puzzle import Puzzle


def Astar_search(initial_state):
    count = 0
    #lista de noh ja exp´lorados
    explored = []
    #noh inicial
    start_node = Puzzle(initial_state, None, None, 0, True)
    #fila de prioridade
    q = PriorityQueue()
    #adiciono na fila a funcao de avaliacao f=g+h, contador, e meu noh
    # a priridade é pelo menor valor da funcao
    q.put((start_node.evaluation_function, count, start_node))
    #enquanto a fila nao for vazia
    while not q.empty():
        #pego os 3 itens da lista
        node = q.get()
        #seleciono o noh
        node = node[2]
        #adciono o noh a lista de explorados
        explored.append(node.state)
        #verifica se o noh atual é o objetivo
        if node.goal_test():
            return node.find_solution()
        #encontro todos so filhos do meu noh atual
        children = node.generate_child()
        #pra cada filho
        for child in children:
            #se n foi explorado
            if child.state not in explored:
                count += 1
                #adiciona novo noh na fila
                q.put((child.evaluation_function,count, child))
    return

