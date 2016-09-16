from copy import deepcopy
from board import *

def solve(cb, row):
    global solutions, sol_count
    spaces=' '*row
    #print('{}solve(cb,{})'.format(spaces, row))
    #cb.print_board(spaces)
    found = False
    for c in range(cb.n):
        if cb.get(row, c) == '0': 
            old_cb = deepcopy(cb)
            cb.set(row, c, '2')
            found = True
            #print('{}Placing queen @ {},{}'.format(spaces, row, c))
            cb.block_path(block_row=row, block_col=c)
            if row == cb.n-1:
                #solution found. check duplicate and print
                h = cb.convert_board_to_hex()
                if h in solutions:
                    print('Solution already present')
                else:
                    sol_count +=1
                    print('*************** SOLUTION {} ***************'.format(sol_count))
                    cb.print(spaces, debug=False)
                    add_all_to_solutions(cb)
                #comment out next two lines if you want to stop on first solution
                cb = deepcopy(old_cb)
                found = False
            else:
                #solve the next row
                if solve(cb, row+1) == False:
                    cb = deepcopy(old_cb)
                    found = False;
                    #print('{}After backtracking'.format(spaces))
                    #cb.print(spaces)
                    continue
            
    #if found == False:
        #print('{}Found no solution, backtracking'.format(spaces))

    #print('{}solve(cb,{}):{}'.format(spaces, row, str(found)))
    return found

def add_to_solutions( chess_board ):
    h = chess_board.convert_board_to_hex()
    if h in solutions:
        solutions[h] += 1
    else:
        solutions[h] = 1

def add_all_to_solutions( chess_board ):
    add_to_solutions(chess_board)
    add_to_solutions(chess_board.rotate_board_90())
    add_to_solutions(chess_board.rotate_board_180())
    add_to_solutions(chess_board.rotate_board_270())
    add_to_solutions(chess_board.reflect_vertical())
    add_to_solutions(chess_board.reflect_horizontal())

board = ChessBoard(8)
solutions = {}
sol_count = 0

solve(board, 0)
for sol in solutions.keys():
    print('{}: {}'.format(sol, solutions[sol]))

print('Number of solutions: {}'.format(len(solutions)))
