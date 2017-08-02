# This program allows users to play Tic-tac-toe
# against another player
from termcolor import colored, cprint
import random

def displayBoard(board):
    x = colored(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9], 'red')
    print(x)
    print(' ---------')
    y = colored(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6], 'blue')
    print(y)
    print(' ---------')
    z = colored(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3], 'yellow')
    print(z)


def inputPlayerLetter():
    letterOptions = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    letter = ''
    character = ''
    while letter not in letterOptions:
        print('Player 1, type in your character')
        letter = input()
    while character not in letterOptions:
        print('Player 2, type in your character')
        character = input()
    return letter, character

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


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


def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    return board[move] == ' '


def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is player1\'s next move? (1-9)')
        move = input()
    return int(move)

def getPlayer2Move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is player2\'s next move? (1-9)')
        move = input()
    return int(move)

def chooseMove(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def boardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Let\'s play Tic Tac Toe!')

while True:

    theBoard = [' '] * 10
    playerLetter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + ' will go first.')
    isPlaying = True

    while isPlaying:
        if turn == 'player1':

            displayBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                displayBoard(theBoard)
                print('Player1 has beaten player2! Player2 loses')
                isPlaying = False
            else:
                if boardFull(theBoard):
                    displayBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'

        else:
            displayBoard(theBoard)
            move = getPlayer2Move(theBoard)
            makeMove(theBoard, player2Letter, move)

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
        break
