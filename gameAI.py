from math import inf as infinity
'''
board = [['X', 'X', 'X'],
         [' ', ' ', ' '],
         ['O', 'O', 'O']]
'''
board = [['X', ' ', 'O'],
         ['O', 'O', 'X'],
         ['X', ' ', ' ']]

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]



str = "| |--| |--| |\n | \  |  / | \n |  \ | /  | \n| |--| |--| |\n |  / | \  | \n | /  |  \ | \n| |--| |--| |\n"
values = [1,6,11,43,48,53,85,90,95]
'''
valid_moves = dict([(1, [2,4,5]), (2, [1,3,5]) , (3, [2,5,6]) , (4, [1,5,7]) , (5, [1,2,3,4,6,7,8,9]) ,
              (6, [3,5,9]) , (7, [4,5,8]), (8, [5,7,9]) , (9, [5,6,8])
               ])
'''
valid_moves = dict([(0, [1,3,4]), (1, [0,2,4]) , (2, [1,4,5]) , (3, [0,4,6]) , (4, [0,1,2,3,5,6,7,8]) ,
              (5, [2,4,8]) , (6, [3,4,7]), (7, [4,6,8]) , (8, [4,5,7])
               ])


print(valid_moves)

def print_board():
    global str
    for i in range(0,3):
        for j in range(0,3):
            str = replacer(str, board[i][j],values[3*i+j])
    print(str)


def take_input():
    pos_old, pos_new = input("Enter old and new Position (ex:8 5) : ").split(' ')
    try:
        pos_old = int(pos_old) - 1
        pos_new = int(pos_new) - 1

        if(pos_old>=0 and pos_old<9 and pos_new>=0 and pos_new<9):
            return pos_old, pos_new
        else:
            return 0,0
    except:
        print("Invalid Input")
        return 0,0

def place_player(pos_old, pos_new, player):
    row_old = pos_old // 3
    column_old = pos_old % 3

    row_new = pos_new // 3
    column_new = pos_new % 3
    if(board[row_old][column_old] == player and board[row_new][column_new]==" " and pos_new in valid_moves[pos_old]):
        board[row_old][column_old] = " "
        board[row_new][column_new] = player
        return 1
    else:
        print("Invalid Move")
        return 0

def check_row(i):
    x = 0
    o = 0
    for j in range(3):
        if board[i][j] == 'X':
            if(i==0):
                continue
            x += 1

        if board[i][j] == 'O':
            if(i==2):
                continue
            o += 1
    if x == 3:
        print_board()
        print("X won")
        quit()

    elif o == 3:
        print_board()
        print("O won")
        quit()

def check_column(j):
    x = 0
    o = 0
    for i in range(3):

        if board[i][j] == 'X':
                x += 1

        if board[i][j] == 'O':
            o += 1

    if x == 3:
        print_board()
        print("X won")
        quit()

    elif o == 3:
        print_board()
        print("O won")
        quit()

def check_diagonals(a, b, c):
    var = [a, b, c]
    x = 0
    o = 0
    for i in var:
        if i == 'X':
            x += 1

        if i == 'O':
            o += 1

    if x == 3:
        print_board()
        print("X won")
        quit()

    elif o == 3:
        print_board()
        print("O won")
        quit()
#Checking which player 'X'/'O' win in a board.
#returns true or False
def checkWhichPlayerWin(player):
    #cnt = 0
    for i in range(0,3):
        if i==0 and player=='X':
            continue
        if i==2 and player=='O':
            continue
        cnt = 0
        for j in range(0,3):
            if board[i][j] == player:
                cnt =cnt+1
        if cnt==3:
            return True
    for i in range(0,3):
        cnt = 0
        for j in range(0,3):
            if board[j][i] == player:
                cnt =cnt+1
        if cnt==3:
            return True
    if(board[0][0]==player and board[0][0]==board[1][1] and board[0][0]==board[2][2]):
        return True
    if(board[0][2]==player and board[0][2]==board[1][1] and board[0][2]==board[2][0]):
        return True
    return False

def best_move(ai):
    bestScore = -infinity
    bestMove_old, bestMove_new = 0,0
    best_depth  = 12
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]==ai):
                pos_old = 3*i + j
                #print(pos_old)
                for pos_new in valid_moves[pos_old]:
                    row_old = pos_old//3
                    column_old = pos_old%3
                    row_new = pos_new//3
                    column_new = pos_new%3
                    if(board[row_new][column_new]==" "):
                        board[row_old][column_old] = " "
                        board[row_new][column_new] = ai
                        #score = 0
                        score, value = minimax(board,0,False,ai)
                        score = int(score)
                        if(score>=bestScore):
                            bestScore = score
                            bestMove_old, bestMove_new = pos_old, pos_new
                            best_depth = value
                            #print(bestScore, best_depth)
                            #print_board()
                        board[row_old][column_old] = ai
                        board[row_new][column_new] = " "
    print(bestScore, best_depth)
    return bestMove_old, bestMove_new

def minimax(board, depth, isMaximizing, ai):
    #return 1
    #print(depth)
    if ai=='X':
        human = 'O'
    else:
        human = 'X'
    #return 1
    if (checkWhichPlayerWin(ai)):
        return 10, depth
    elif (checkWhichPlayerWin(human)):
        return -10, depth
    #print_board()
    #return 1

    if depth == 10:
        return 0, depth
    if(isMaximizing):
        #finding valid moves
        bestScore = -infinity
        #bestMove_old, bestMove_new = 0,0
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j]==ai):
                    pos_old = 3*i + j
                    for pos_new in valid_moves[pos_old]:
                        row_old = pos_old//3
                        column_old = pos_old%3
                        row_new = pos_new//3
                        column_new = pos_new%3
                        if(board[row_new][column_new]==" "):
                            board[row_old][column_old] = " "
                            board[row_new][column_new] = ai
                            #score = 0
                            score, value = minimax(board,depth+1,False,ai)
                            score = int(score)
                            if(score>=bestScore):
                                bestScore = score
                                #bestMove_old, bestMove_new = pos_old, pos_new
                            board[row_old][column_old] = ai
                            board[row_new][column_new] = " "
        return bestScore,value
    else:
        bestScore = infinity
        #bestMove_old, bestMove_new = 0,0
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j]==human):
                    pos_old = 3*i + j
                    for pos_new in valid_moves[pos_old]:
                        row_old = pos_old//3
                        column_old = pos_old%3
                        row_new = pos_new//3
                        column_new = pos_new%3
                        if(board[row_new][column_new]==" "):
                            board[row_old][column_old] = " "
                            board[row_new][column_new] = human
                            #score = 0
                            score, value = minimax(board,depth+1,True,ai)
                            score = int(score)
                            if(score<bestScore):
                                bestScore = score
                                #bestMove_old, bestMove_new = pos_old, pos_new
                            board[row_old][column_old] = human
                            board[row_new][column_new] = " "
        return bestScore, value
'''

def main():
    print_board()
    print(checkWhichPlayerWin('X'))
    pos_old,pos_new = best_move('X')
    #print(pos_old,pos_new)
    place_player(pos_old, pos_new,'X')
    print_board()

'''

def main():
    print_board()
    smove= input("Want to start first move? (yes/no): ")
    if(smove=='yes' or smove=='Yes' or smove=='YES' or smove=='y'):
        p = ['O','X']
    else:
        p = ['X','O']

    global game_on
    game_on = True
    count = 0
    while game_on:
        if count==20:
            break
        if count % 2 == 0:
            player = p[0]
        else:
            player = p[1]
        print_board()
        print("Player "+player+"'s Turn")
        if player=='X':
            pos_old,pos_new = best_move(player)
        else:
            pos_old,pos_new = best_move(player)
            #pos_old,pos_new = take_input()
        count += place_player(pos_old, pos_new,player)
        #print(checkWhichPlayerWin(player))
        for j in range(3):
            check_column(j)
            check_row(j)
            check_diagonals(board[0][0], board[1][1], board[2][2])
            check_diagonals(board[0][2], board[1][1], board[2][0])


if __name__ == '__main__':
    main()
