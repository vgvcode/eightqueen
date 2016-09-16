from copy import deepcopy
from board import *

def solve(cb, row):
    found = False
    spaces='  '*row
    old_cb = deepcopy(cb)
    #print('{}solve({})'.format(spaces, row))
    for c in range(cb.n):
        if cb.get(row, c) == '0': 
            cb.set(spaces, row, c, '2')
            cb.block_path(spaces, block_row=row, block_col=c)
            if row == cb.n-1:
                found = True
                store_and_print_solution("", cb)
                break
            else:
                #solve the next row
                solve(cb, row+1)
                #no solution, copy back the old board
                cb = deepcopy(old_cb)
            
    #print('{}Return solve({}):{}'.format(spaces, row, found))

def store_and_print_solution(spc, b):
    global solutions
    h = b.convert_board_to_hex()
    solutions[h] = 1
    print('{}*************** SOLUTION {} ***************'.format(spc,len(solutions)))
    b.print(spc, debug=False)
    #if h in derived_solutions:
        #print('{}Solution already present'.format(spc))
    #else:
        #solutions[h] = 1
        #add_all_to_solutions(cb, spc)
        #print('{}*************** SOLUTION {} ***************'.format(spaces,len(solutions)))
        #cb.print(spc, debug=False)
    #break

def add_to_derived_solutions( chess_board, spaces="" ):
    h = chess_board.convert_board_to_hex()
    if h in derived_solutions:
        derived_solutions[h] += 1
        print('{}Already present: {}'.format(spaces, h))
    else:
        derived_solutions[h] = 1
        print('{}New: {}'.format(spaces, h))

def add_all_to_solutions( chess_board, spaces="" ):
    add_to_derived_solutions(chess_board, spaces)
    add_to_derived_solutions(chess_board.rotate_board_90(), spaces)
    add_to_derived_solutions(chess_board.rotate_board_180(), spaces)
    add_to_derived_solutions(chess_board.rotate_board_270(), spaces)
    add_to_derived_solutions(chess_board.reflect_vertical(), spaces)
    add_to_derived_solutions(chess_board.reflect_horizontal(), spaces)

board = ChessBoard(8)
derived_solutions = {}
solutions = {}

solve(board, 0)
print('Number of solutions: {}'.format(len(solutions)))
