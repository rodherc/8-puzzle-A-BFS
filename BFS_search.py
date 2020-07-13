from queue import Queue
from puzzle import Puzzle


def breadth_first_search(initial_state):
    #no inicial
    start_node = Puzzle(initial_state, None, None, 0)
    #verifica se o noh é o final
    if start_node.goal_test():
        #se sim volta pra encontrar a solucao
        return start_node.find_solution()
    #fila pra auxilar na vusca do bfs
    q = Queue()
    #inicia com o noh inicial
    q.put(start_node)
    #lista de noh ja explorados
    explored = []
    #enquanto existir nohs na fila
    while not(q.empty()):
        #pega o primeiro noh da fila
        node = q.get()
        #adicionada o noh na lista de explorados
        explored.append(node.state)
        #pego todos on noh filhos do meu noh atual
        children=node.generate_child()
        #pra cada filho na lista eu faço
        for child in children:
            #verifico se o filho encontrado ja foi explorado
            if child.state not in explored:
                #verifico se esse filho é meu objetivo
                if child.goal_test():
                    return child.find_solution()
                #adiciono o filho na lista de noh para explorar
                q.put(child)
    return
