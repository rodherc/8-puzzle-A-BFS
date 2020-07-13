class Puzzle:
    #estado final do jogo
    goal_state = [1,2,3,8,0,4,7,6,5]
    #guarda a heuristica
    heuristic = None
    #guarda o valor da funcao de avaliacao
    evaluation_function = None
    #variavel auxilar pra ver se é o bfs ou A*
    needs_hueristic = False
    #guarda o numero de instancias
    num_of_instances = 0

    #contrutor
    def __init__(self, state, parent, action, path_cost, needs_hueristic = False):
        self.parent = parent
        self.state = state
        self.action = action
        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost
        if needs_hueristic:
            self.needs_hueristic = True
            self.generate_heuristic()
            self.evaluation_function = self.heuristic+self.path_cost
        Puzzle.num_of_instances +=1

    def __str__(self):
        #retorna 0s 3 primeiros    retorna os 3 do meio e    retorna os 3 ultimos
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])

    #funcao que gera a heuristica
    def generate_heuristic(self):
        self.heuristic = 0
        for num in range(1,9):
            #LISTA.INDEX(X) RETORNA A POSICAO DO X
            distance = abs(self.state.index(num) - self.goal_state.index(num))
            i = int(distance / 3)
            j = int(distance % 3)
            self.heuristic = self.heuristic + i + j

    #verifica se a noh atualç é igual ao objetivo
    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False

    #Encontra as acoes possiveis para os movimentos
    @staticmethod
    def find_legal_actions(i,j):
        legal_action = ['U', 'D', 'L', 'R']
        #se for a primeira linha não é possivel ir para UP
        if i == 0:  # up is disable
            legal_action.remove('U')
        #se for a ultima linha não é possivel ir para DOWN
        elif i == 2:  # down is disable
            legal_action.remove('D')
        #se for a primeira coluna nçao é possivel ir para LEFT
        if j == 0:
            legal_action.remove('L')
        #se for a ultima coluna não é possivel ir para RIGHT
        elif j == 2:
            legal_action.remove('R')
        #retorna todas as açoes possiveis
        return legal_action

    #Função que faz todos os movimentos possiveis para um noh, encontrando seus filhos
    def generate_child(self):
        #lista de filhos
        children = []
        x = self.state.index(0)
        i = int(x / 3)
        j = int(x % 3)
        legal_actions=self.find_legal_actions(i,j)
       
       #repetição para fazer todas as acoes
        for action in legal_actions:
            new_state = self.state.copy()
            if action is 'U':
                # na matriz 3x3 o movimento de UP é so subtrair 3
                new_state[x], new_state[x - 3] = new_state[x - 3], new_state[x]
            elif action is 'D':
                 # na matriz 3x3 o movimento de UP é so somar 3
                new_state[x], new_state[x + 3] = new_state[x + 3], new_state[x]
            elif action is 'L':
                # pra voltar é so subtair 1
                new_state[x], new_state[x - 1] = new_state[x - 1], new_state[x]
            elif action is 'R':
                #pra ir pra direita é so somar 1
                new_state[x], new_state[x + 1] = new_state[x + 1], new_state[x]
            #adiciona o novo filho encontrado na lista de filhos
            children.append(Puzzle(new_state,self,action,1,self.needs_hueristic))
        #retorna a lista de filhos
        return children

    #Quando se encontra a solucao, é necessario voltar no caminho feito ate chegar no inicial
    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution
