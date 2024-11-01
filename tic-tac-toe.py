#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}


def markBoard(position, mark):
    board[position] = mark
    return board




def printBoard():
    displayBoard = {}
    
    # Use numbers as placeholders where the board is empty
    for i in range(1, 10):
        if board[i] == ' ':
            displayBoard[i] = str(i)  # Show the number for empty positions
        else:
            displayBoard[i] = board[i]  # Show the current mark ('X' or 'O')

    # Print the board with placeholders for empty positions
    print(' ' + displayBoard[1] + ' | ' + displayBoard[2] + ' | ' + displayBoard[3] + ' \n' +
          ' --------- \n' +
          ' ' + displayBoard[4] + ' | ' + displayBoard[5] + ' | ' + displayBoard[6] + ' \n' +
          ' --------- \n' +
          ' ' + displayBoard[7] + ' | ' + displayBoard[8] + ' | ' + displayBoard[9] + ' \n')

    return




# True denoting that the user input is correct
def validateMove(position):
    position = str(position)
    if position.isdigit():
        if int(position) >=1 and int(position) <= 9:
                if board[int(position)] == ' ':
                    return True
                else:
                    return False
    return False

winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]


# This method should return with True or False
def checkWin(player):
    for i in winCombinations:
        if board[i[0]] == player and board[i[1]] == player and board[i[2]] == player:
            return True
    return False


# This function should return with boolean
def checkFull():
    for i in range(1, 10):
        if board[i] == ' ':
            return False        
    return True

def restartGame():
    global board
    board = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
    print('\n\n' +
          ' 1 | 2 | 3 \n' +
          ' --------- \n' +
          ' 4 | 5 | 6 \n' +
          ' --------- \n' +
          ' 7 | 8 | 9 \n')



gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')



restart = True

while restart:
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")
        if validateMove(move):
            markBoard(int(move), currentTurnPlayer)
            printBoard()
            if checkWin(currentTurnPlayer):
                print(currentTurnPlayer + ' wins!')            
                gameEnded = True
            elif checkFull():
                print('Tie!')
                gameEnded = True
            else:
                currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'
        else:
            print('Invalid input, please try again')

    playAgain = input('Do you want to play again? (Y/N): ').lower()
    if playAgain == 'y':
        restartGame()
        gameEnded = False
        currentTurnPlayer = 'X'
    elif playAgain == 'n':
        restart = False
    else:
        print('Invalid input, please try again')
        

