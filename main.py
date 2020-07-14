from time import time
from BFS_search import breadth_first_search
from Astar_search import Astar_search
from puzzle import Puzzle
from verification import *


continuar = True
while(continuar):
        #for i in range(0,3):
        print("\nJogando 8-puzzle")
        print("Objetivo do jogo:")
        print( "| 1 , 2 , 3  |\n| 8 , 0 , 4  |\n| 7 , 6 , 5  |\n" )
        inp = input('Por favor entre os numeros do puzzle separados por espaços: ')
        lista =  inp.split(' ')
        ehInt = True
        if(len(lista) != 9):
                ehInt = False
        else:
                for i in range(len(lista)):
                        var = lista[i]
                        if(not var.isnumeric()):
                                ehInt = False
                        elif(int(var) < 0 or int(var) > 8):
                                ehInt = False

        if(ehInt):
                state = list(map(int,lista))

                if(puzzleVerification(state)):
                        print("\nEntrada verificada com sucesso, é possível resolver!!!  \n")
                        Puzzle.num_of_instances=0
                        print('Escolha o algotimo a ser usado:')
                        print('Digite 1 para usar o BFS e 2 para usar o A*')
                        algorithm = input()

                        if(algorithm == '1'):
                                t0=time()
                                bfs=breadth_first_search(state)
                                t1=time()-t0
                                print("\nEntrada:")
                                printPuzzle(state,bfs)

                                        
                                print('passos:', Puzzle.num_of_instances)
                                print('tempo:', t1)
                                print()


                                print('------------------------------------------ \n')

                        elif(algorithm == '2'):
                                t0 = time()
                                astar = Astar_search(state)
                                t1 = time() - t0
                                print("\nEntrada:")
                                printPuzzle(state,astar)

                                        
                                print('passos:', Puzzle.num_of_instances)
                                print('tempo:', t1)
                                print()


                                print('------------------------------------------ \n')
                        else:
                                print("Comando inválido tente novamente.  \n")



                else:
                        print('Puzzle impossivel de ser resolvido!')
                        print()
                        print('------------------------------------------')
                
                print('Deseja tentar novamente?')
                
                ans = input('S ou N: ')

                if(ans == 'N' or ans == 'n'):
                        continuar = False
                        print('Falou')
                elif(ans != 'S' and ans != 's'):
                        print("Comando inválido tente novamente.")
        else:
                print("Entrada inválida, tente novamente!!!")