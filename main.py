from time import time
from BFS_search import breadth_first_search
from Astar_search import Astar_search
from puzzle import Puzzle
from verification import puzzleVerification


'''state=[[1, 3, 4,
        8, 6, 2,
        7, 0, 5],

       [2, 8, 1,
        0, 4, 3,
        7, 6, 5],

       [2, 8, 1,
        4, 6, 3,
        0, 5, 7]]'''

continuar = True
while(continuar):
        #for i in range(0,3):

        inp = input('Por favor entre os numeros do puzzle separados por espaços: ')

        state = list(map(int, inp.split(' ')))

        if(puzzleVerification(state)):
                Puzzle.num_of_instances=0
                print('Escolha o algotimo a ser usado:')
                print('Digite 1 para usar o BFS e 2 para usar o A*')
                algorithm = input()

                if(algorithm == '1'):
                        t0=time()
                        bfs=breadth_first_search(state)
                        t1=time()-t0
                        print('BFS:', bfs)

                else:
                        t0 = time()
                        astar = Astar_search(state)
                        t1 = time() - t0
                        print('A*:',astar)

                print('passos:', Puzzle.num_of_instances)
                print('tempo:', t1)
                print()


                print('------------------------------------------')

                Puzzle.printPuzzle()
        else:
                print('Puzzle impossivel de ser resolvido!')
                print()
                print('------------------------------------------')
        
        print('Deseja tentar novamente?')
        
        ans = input('S ou N: ')

        if(ans == 'N' or ans == 'n'):
                continuar = False
                print('Falou')
        