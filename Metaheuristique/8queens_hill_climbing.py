"""
Algorithm to solve the n-queens problem
"""
import random
import copy

############################## FUNCTIONS ###########################

CYAN = '\u001b[36m'
BCYAN = CYAN.replace('m',';1m')
RESET = '\u001b[0m'

# function to display plate
def show(plate, n):
    for i in range(n):
        raw = ''
        for j in range(n):
            raw += str(plate[i][j])+' '
        print(raw)

# return number of queen conflicts on plate
def find_conflict(plate):
    conflict = 0
    for i in range(n):
        for j in range(n):
            if plate[i][j] == BCYAN+'Q'+RESET:
                conflict -= 2
                for k in range(n):
                    # raw and columns conflicts
                    # optional if there are already one queen per raw and
                    if plate[i][k] == BCYAN+'Q'+RESET:
                        conflict += 1
                    if plate[k][j] == BCYAN+'Q'+RESET:
                        conflict += 1

                # diagonal conflicts
                k, l = i+1, j+1
                while k < n and l < n:
                    if plate[k][l] == BCYAN+'Q'+RESET:
                        conflict += 1
                    k += 1
                    l += 1
                
                k, l = i-1, j+1
                while k >=0 and l < n:
                    if plate[k][l] == BCYAN+'Q'+RESET:
                        conflict += 1
                    k -= 1
                    l += 1
                
                k, l = i-1, j-1
                while k >= 0 and l >= 0:
                    if plate[k][l] == BCYAN+'Q'+RESET:
                        conflict += 1
                    k -= 1
                    l -= 1

                k, l = i+1, j-1
                while k < n and l >= 0:
                    if plate[k][l] == BCYAN+'Q'+RESET:
                        conflict += 1
                    k += 1
                    l -= 1
    return conflict

# return plate p with lines a and b swapped
def swap_lines(p, a, b): 
    p[a], p[b] = p[b], p[a]
    return p

#################################### MAIN ################################

if __name__ == "__main__":

    ### INITIALISATION
    # plate size = number of queens
    n = 16
    # empty plate
    init_plate = [['\u25AB' for i in range(n)] for j in range(n)]
    # Place one queen per column and per raw
    col = [j for j in range(n)]
    random.shuffle(col)
    for i in range(n):
        init_plate[i][col[i]] = BCYAN+'Q'+RESET
    ###

    print('QUEEN PROBLEM : HILL CLIMBING METHOD')
    print('====================================')
    print('GOAL : Minimize number of conflicts')
    print()

    # show initial config
    print('Initial configuration :')
    print('-----------------------')
    show(init_plate, n)
    e = find_conflict(init_plate)
    print('-----------------------')
    print('Conflicts : ', e)
    print()

    best_error = [e]
    loop_counter = 0

    while (e <= min(best_error) and e > 0):
        
        errors = []
        swap = []
        plate = copy.copy(init_plate)
        
        for i in range(n):
            for j in range(n):
                new_plate = swap_lines(plate,i,j)
                e = find_conflict(new_plate)
                swap.append([i,j])
                errors.append(e)
        e = min(errors)
        if e < best_error[-1]:
            best_error.append(e)
            e_idx = errors.index(e)
            swap = swap[e_idx]
            l1, l2 = swap[0], swap[1]
            init_plate = swap_lines(init_plate, l1, l2)
            loop_counter += 1
            print('BEST SWAP :', l1,'<-->', l2,' GIVES :')
            show(init_plate, n)
            if e == 0:
                print('Conflicts : ', e, ': solution found !')
                break
            else:
                print('Conflicts :', e)
                print('Loop n°', loop_counter)
                print()

                # control iterations (optional)
                input('Press Enter to continue')
        else:
            print('No better swap found.')
            break