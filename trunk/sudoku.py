# brute-force sudoku solver
#
# gumuz.nl


def isValid(arr, pos):
    # check if gives pos is valid in arr
    
    y,x = divmod(pos, 9)
    
    # check vertical & horizontal
    v_tmp = []
    h_tmp = []
    for i in range(9):
        nv = arr[(i*9)+x]
        nh = arr[(y*9)+i]
        
        if nv in v_tmp or nh in h_tmp: return False
        if nv: v_tmp.append(nv)
        if nh: h_tmp.append(nh)
        
    # check sub-square (3x3)
    sub_y = (y/3)*3
    sub_x = (x/3)*3
    tmp  = []
    for i in range(3):
        for j in range(3):
            n = arr[(i*9)+(sub_y*9)+sub_x+j]
            if n and n in tmp: return False
            if n: tmp.append(n)

    # no problemos!
    return True

def solve(arr): 
    # recursive, backtracking sudoku solver
    
    arr = arr[:] # working copy
    
    try: # find next 0
        pos = arr.index(0)
    except ValueError:
        # solution found!
        return arr 

    for i in range(1,10):
        arr[pos] = i
        if isValid(arr, pos): # is valid move?
            sol = solve(arr)
            if sol: return sol

if __name__ == '__main__':
    print "Brute Force sudoku Solver -- gumuz.nl"
    print
    
    import time, sys
    
    if len(sys.argv) == 1:
        print "Usage: sudoku.py filename.txt"
        sys.exit()
    
    for filename in sys.argv[1:]:
        print "processing", filename
        puzzles = [ [int(n) for n in p.strip()] \
                    for p in open(filename, 'r')]
        
        start = time.time()
        for p in puzzles:
            print p
            solve(p)
            print p
            print

        print "%s sudoku's solved in %s seconds" % (len(puzzles), round(time.time()-start))