player_1 = 'X'
player_2 = 'O'
game_board = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8],
              [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8],
              [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]]
move_counter = 0
last_moves = 0
Flag = False
#win_pos are 0-1-2 or 3-4-5 or 6-7-8 or 0-3-6 or 1-4-7 or 2-5-8 or 0-4-8 or 2-4-6
#print(game_board)
#print(game_board[1][1])

#Функция совершения ходов игроками
def game(player, board, counter, last_move):
    #Совершение всех последующих ходов
    if counter != 0:
        square_num = int(input('player'+player+' moves in b'+str(last_move)+'s'))
        if board[last_move][square_num]!='X' and  board[last_move][square_num]!='O':
            board[last_move][square_num] = player
            print(player, 'b'+str(last_move)+'s'+str(square_num))
            counter += 1
            previous_move = last_move
            last_move = square_num
        else:
            print('Choose another field')
            previous_move = last_move
    #Совершение первого хода
    else:
        square_num = int(input('player'+player+' moves in b4s'))
        board[4][square_num] = player
        print(player, 'b4s'+str(square_num))
        counter += 1
        previous_move = 0
        last_move = square_num
    return board, counter, last_move, previous_move

#Функция, проверяющая условие победы
def victory(player, board, previous_move):
    if (board[previous_move][0]==player and board[previous_move][1]==player and board[previous_move][2]==player) or \
        (board[previous_move][3] == player and board[previous_move][4] == player and board[previous_move][5] == player) or \
        (board[previous_move][6] == player and board[previous_move][7] == player and board[previous_move][8] == player) or \
        (board[previous_move][0] == player and board[previous_move][3] == player and board[previous_move][6] == player) or \
        (board[previous_move][1] == player and board[previous_move][4] == player and board[previous_move][7] == player) or \
        (board[previous_move][2] == player and board[previous_move][5] == player and board[previous_move][8] == player) or \
        (board[previous_move][0] == player and board[previous_move][4] == player and board[previous_move][8] == player) or \
        (board[previous_move][2] == player and board[previous_move][4] == player and board[previous_move][6] == player):
        print('player'+player, 'won')
        return True
    else:
        return False

#Алгоритм самой игры
while not Flag:
    #Если значение в счетчике четное, то ходит игрок 1, иначе - игрок 2
    if move_counter%2==0:
        game_board, move_counter, last_moves, prev = game(player_1, game_board, move_counter, last_moves)
        Flag = victory(player_1, game_board, prev)
        print(game_board)
    else:
        game_board, move_counter, last_moves, prev = game(player_2, game_board, move_counter, last_moves)
        Flag = victory(player_2, game_board, prev)
        print(game_board)



