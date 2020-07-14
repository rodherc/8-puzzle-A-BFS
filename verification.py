#verifica se o puzzle tem solução ou não
def puzzleVerification (puzzle):

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