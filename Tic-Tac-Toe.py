# This program allows users to play Tic-tac-toe
# against another player
from termcolor import colored, cprint
import random

def displayBoard(board):
    x = colored(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9], 'red')
    # making the board colored red, blue, and yellow
    print(x)
    print(' ---------')
    y = colored(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6], 'blue')
    print(y)
    print(' ---------')
    z = colored(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3], 'yellow')
    print(z)
    # Making the Tic-Tac-Toe Game Board


def inputPlayerLetter():
    letterOptions = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    # giving the player the option to use any letter as their character, not just X and O
    letter = ''
    character = ''
    while letter not in letterOptions:
        print('Player 1, type in your character(A-Z)')
        letter = input()
    while character not in letterOptions:
        print('Player 2, type in your character(A-Z)')
    # giving both players the option to choose their letter
        character = input()
    return letter, character

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'
    # picking a number, either 1 or 0, resulting in a 50% chance to pick which player will be going first

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
# allowing the player to choose if they want to play again

def makeMove(board, letter, move):
    board[move] = letter


def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))
# listing all the possible ways to get 3 characters in a row, resulting in the ability to check who won

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    return board[move] == ' '
# if space is free, allowing player to make move

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is player1\'s next move? (1-9)')
        move = input()
    return int(move)
# allowing player one to make a move if there is space open on the board

def getPlayer2Move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is player2\'s next move? (1-9)')
        move = input()
    return int(move)
# allowing player two to make a move if there is space open on the board

def chooseMove(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
# to check if any possible moves and to make them if there are
def boardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
# define a function to see if board is full

print('Let\'s play Tic Tac Toe!')

while True:

    theBoard = [' '] * 10
    playerLetter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + ' will go first.')
    isPlaying = True
# calls all the previously defined functions to set up and begin the game
    while isPlaying:
        if turn == 'player1':
# checks if it is Player One's turn, then gives the personalized code to that player's turns and choices
            displayBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                displayBoard(theBoard)
                print('Player1 has beaten player2! Player2 loses')
                isPlaying = False
                # checks when 3 in a row has been reached to determine the winner of the game
            else:
                if boardFull(theBoard):
                    displayBoard(theBoard)
                    print('The game is a tie!')
                    break
                    # checks if no one got 3 in a row, resulting in a tie game
                else:
                    turn = 'player2'

        else:
            displayBoard(theBoard)
            move = getPlayer2Move(theBoard)
            makeMove(theBoard, player2Letter, move)
# checks if it is Player Two's turn, then gives the personalized code to that player's turns and choices
            if isWinner(theBoard, player2Letter):
                displayBoard(theBoard)
                print('Player2 has beaten player1! Player1 loses.')
                isPlaying = False
            else:
                if boardFull(theBoard):
                    displayBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'

    if not playAgain():
        # if not function repeats process until someone wins or there is a tie
        break
