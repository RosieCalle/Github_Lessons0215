from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    pass


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    move = int(input("Please enter your move: ")) - 1

    row = move // 3
    col = move % 3
    if (row, col) in make_list_of_free_fields(board):
        board[row][col] = 'O'


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    result = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('O', 'X'):
                result.append((row, col))
    return result


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    for index in range(3):
        if board[index][0] == board[index][1] and board[index][1] == board[index][2]:
            print("player using " + sign + " has won the game")
            return True
        if board[0][index] == board[1][index] and board[1][index] == board[2][index]:
            print("player using " + sign + " has won the game")
            return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        print("player using " + sign + " has won the game")
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        print("player using " + sign + " has won the game")
        return True
    else:
        if len(make_list_of_free_fields(board)) == 0:
            print("Draw, no player won the game")
            return True

        return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] + '   |   ' + board[0][1] + '   |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1][0] + '   |   ' + board[1][1] + '   |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[2][0] + '   |   ' + board[2][1] + '   |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


board = [
    ['1', '2', '3'],
    ['4', 'X', '6'],
    ['7', '8', '9']
]

# draw_move(board)
#
# board = [
#     ['O', '2', '3'],
#     ['O', 'X', '6'],
#     ['O', '8', '9']
# ]
#
# print(victory_for(board, 'O'))
# print(make_list_of_free_fields(board))

sign = 'X'
draw_move(board)
while not victory_for(board, sign):
    if sign == 'X':
        sign = 'O'
    else:
        sign = 'X'

    if sign == 'O':
        enter_move(board)
    else:
        free = make_list_of_free_fields(board)
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'

    draw_move(board)
