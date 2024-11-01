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

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    board[position] = mark
    return board


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
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



# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    position = str(position)
    if position.isdigit():
        if int(position) >=1 and int(position) <= 9:
                if board[int(position)] == ' ':
                    return True
                else:
                    return False
    return False

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
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

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    for i in winCombinations:
        if board[i[0]] == player and board[i[1]] == player and board[i[2]] == player:
            return True
    return False

# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
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



#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User

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
        





# Bonus Point: Implement the feature for the user to restart the game after a tie or game over

