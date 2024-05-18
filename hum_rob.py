import random

player_1 = 'X'
player_2 = 'O'
game_board = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8],
              [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8],
              [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]]
move_counter = 0
last_moves = 0
Flag = False

#Функция хода для игрока 1
def game(player, board, counter, last_move):
    #Совершение последующих ходов
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
    #Совершение 1го хода
    else:
        square_num = int(input('player'+player+' moves in b4s'))
        board[4][square_num] = player
        print(player, 'b4s'+str(square_num))
        counter += 1
        previous_move = 0
        last_move = square_num
    return board, counter, last_move, previous_move

#Функция, проверяющая условия победы
def victory(player, board, previous_move):
    if (board[previous_move][0]==player and board[previous_move][1]==player and board[previous_move][2]==player) or \
        (board[previous_move][3] == player and board[previous_move][4] == player and board[previous_move][5] == player) or \
        (board[previous_move][6] == player and board[previous_move][7] == player and board[previous_move][8] == player) or \
        (board[previous_move][0] == player and board[previous_move][3] == player and board[previous_move][6] == player) or \
        (board[previous_move][1] == player and board[previous_move][4] == player and board[previous_move][7] == player) or \
        (board[previous_move][2] == player and board[previous_move][5] == player and board[previous_move][8] == player) or \
        (board[previous_move][0] == player and board[previous_move][4] == player and board[previous_move][8] == player) or \
        (board[previous_move][2] == player and board[previous_move][4] == player and board[previous_move][6] == player):
        return True
    else:
        return False

#Функция минимакса для хода игрока 2, возвращающая рейтинг возможных ходов
def minimax(board, is_maximizing, depth, prev):
    #Если выигрывает противник(т.е. игрок 1), то рейтинг равен -10
    #Если выигрывает робот, то рейтинг равен 10
    #Если выбранная глубина не позволяет застать победу одного из игроков, то рейтинг равен 0(нейтральная позиция)
    if victory(player_1, board, prev):
        return -10
    elif victory(player_2, board, prev):
        return 10
    elif depth == 0:
        return 0
    #Если рассматриваем игру со стороны робота(игрока 2),
    # то выбираем наилучший ход для игрока 2
    if is_maximizing:
        best_score = -10000
        for i in range(9):
            if board[prev][i] != 'X' and board[prev][i] != 'O':
                board[prev][i] = player_2
                score = minimax(board, False, depth - 1, prev)
                board[prev][i] = i
                best_score = max(score, best_score)
        return best_score
    #Если рассматриваем игру со стороны человека(игрока 1)
    # то выбираем наихудший ход для игрока 1
    else:
        best_score = 10000
        for i in range(9):
            if board[prev][i] != 'X' and board[prev][i] != 'O':
                board[prev][i] = player_1
                score = minimax(board, True, depth - 1, prev)
                board[prev][i] = i
                best_score = min(score, best_score)
        return best_score

#Функция для выбора наиболее подходящего хода
def optimal_move(board, depth, prev):
    best_score = -10000
    best_move = None
    #Рассматриваем игровой момент в маленькой ячейке
    for i in range(9):
        if board[prev][i] != 'X' and board[prev][i] != 'O':
            board[prev][i] = player_2
            #Если этот ход именно в эту клетку ячейки приносит победу
            #То это и есть лучший ход, заканчиваем работу функции
            if victory(player_2, board, prev):
                best_move = i
                break
            #Подсчитываем рейтинг клетки, с помощью функции минимакс
            score = minimax(board, False, depth, prev)
            board[prev][i] = i
            counter = 0
            #Если ход в эту клетку не приносит победы противника в следующей большой ячейке
            #То выбираем клетку с наибольшим рейтингом
            for b in range(9):
                if board[i][b]!='X' and board[i][b]!='O':
                    board[i][b]='X'
                    exp_flag = victory('X', board, i)
                    board[i][b] = b
                    if exp_flag==True:
                        counter+=1
            if counter==0:
                if score >= best_score:
                    best_score = score
                    best_move = i
    #При условии, когда нельзя определить наилучший ход(все ходы ведут к поражению),
    # то делаем ход в любую свободную клетку
    if best_move == None:
        best_move = random.randint(0, 8)
        while board[prev][best_move] != 'O' and board[prev][best_move] != 'X':
            best_move = (best_move + 1) % 9
    return best_move

#Алгоритм самой игры
while not Flag:
    #Ход игрока 1
    if move_counter % 2 == 0:
        game_board, move_counter, last_moves, prev = game(player_1, game_board, move_counter, last_moves)
        Flag = victory(player_1, game_board, prev)
        if Flag:
            print('player X won')
            print(game_board)
            break
        last_hu_move = last_moves
        print(game_board)
    #Ход игрока 2
    #Регулируя глубину, можно устанавливать разный уровень сложности
    #Чем больше глубина, тем сложнее уровень
    else:
        best_move = optimal_move(game_board, 2, last_hu_move)
        game_board[last_hu_move][best_move] = player_2
        last_moves = best_move
        print(player_2, 'b' + str(last_hu_move) + 's' + str(best_move))
        move_counter += 1
        Flag = victory(player_2, game_board, last_hu_move)
        if Flag:
            print('player O won')
            break
        print(game_board)