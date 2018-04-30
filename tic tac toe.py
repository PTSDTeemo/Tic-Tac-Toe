gameOver = 0
who = 'x'   #Player x goes first. Player o goes second.
takenMoves = []
grid = list('''7|8|9
-----
4|5|6
-----
1|2|3''')
#grid indexes that I care about: 0  2  4
#                               12 14 16
#                               24 26 28
# (all the other indexes are whitespace)



while not gameOver:

    print('Player ' + who + '\'s turn.\nChoose a move:\n\n')
    for c in grid: print(c, end='')
    print ('\n')
    move = input()

    while move in takenMoves:
        print ('\n' + move + ' is taken. Choose again:\n\n')
        for c in grid: print(c, end='')
        print ('\n')
        move = input()

    grid[(grid.index(move))] = who      #Replaces an index with x or o
    takenMoves.append(move)             #Updates list of taken moves



    #This is the win-checker. Too simple for a karnaugh map. 8 ways to win.
    #First it checks horizontal ways, then vertical, then the 2 diagonals.
    if  (
        (grid[0] == who and grid[2]  == who and grid[4]  == who) or
        (grid[12]== who and grid[14] == who and grid[16] == who) or
        (grid[24]== who and grid[26] == who and grid[28] == who) or
        (grid[0] == who and grid[12] == who and grid[24] == who) or
        (grid[2] == who and grid[14] == who and grid[26] == who) or
        (grid[4] == who and grid[16] == who and grid[28] == who) or
        (grid[0] == who and grid[14] == who and grid[28] == who) or
        (grid[4] == who and grid[14] == who and grid[24] == who)
        ):
        print ('You win!\n\n')
        for c in grid: print(c, end='')
        gameOver = 1
    elif len(takenMoves) == 9:      #Tie-checker
        print('Draw. ', end='')     #
        gameOver = 1                #
    else:
        print()
        if who == 'x':
            who = 'o'
        else:
            who = 'x'

print('\n\nGame over.')
