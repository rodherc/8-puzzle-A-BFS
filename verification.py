#verifica se o puzzle tem solução ou não
def puzzleVerification (puzzle):
    
    if(len(puzzle)!= 9):
        return False

    column = 3
    mat = [0] * column

    k = 0
        
    for i in range(column):
        mat[i] = [0] * column

        for j in range(column):
            mat[i][j] = puzzle[k]
            k += 1
    
    listAux = []
    for i in range(column):
        for j in range(column):
            if(j >= i and mat[i][j] != 0 and (i != 1 or j != 1)):
                listAux.append(mat[i][j])
    
    for i in range(column - 1, -1, -1):
        for j in range(column - 1, -1, -1):
            if(i > j and mat[i][j] != 0):
                listAux.append(mat[i][j])
    
    listAux.append(mat[1][1])

    #print(listAux)

    inversions = 0
    for i in range(len(listAux)):
        for j in range(i+1, len(listAux)):
            if(listAux[i] > listAux[j]):
                inversions += 1
    
    #print(inversions)

    return (inversions % 2 == 0)

    
def printPuzzle(puzzle, legal_actions):
    
    new_state = puzzle
    printPuzzleAux(new_state)
    for action in legal_actions:
        x = puzzle.index(0)

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
    
        #Printa o estado atual
        print("Movimento: "+"["+ action+"]")
        printPuzzleAux(new_state)
        
#funcao que auxilia na impressao dos dados
def printPuzzleAux(puzzle):
    aux = 0
    for i in range(3):
        for j in range(3):
            print(str(puzzle[aux]) + " ", end="") # end="" pra nao ter quebra de linha
            aux+=1
        print()
    print()