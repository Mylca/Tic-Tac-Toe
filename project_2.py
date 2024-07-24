"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: Milan Komůrka

email: komurka.milan@email.cz

discord: Milan K.

"""
import random
import os


# Run once function
def run_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return func(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


@run_once
def rules():
    print(
        '''
Welcome to Tic-Tac-Toe

The game is played on a grid that's 3 cells by 3 cells. 
You are X the computer is O. 
Players take turns putting their marks in empty cells. 
The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
Input is number(for row) space number(for column).
'''
    )


# Create 3 x 3 game board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]


# Defines final board with number designation
def print_board(board):
    print('    ' + '   '.join([str(i) for i in range(3)]))
    print('  ' + '-' * 13)

    for id, row in enumerate(board):
        print(f"{id} | " + ' | '.join(row) + ' |')
        print('  ' + '-' * 13)


# Winner check
def is_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


# Draw check
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)


# Execution of the player's move
def player_move(board, player, row, col):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False


# Execution of the computer move
def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3)
                   if board[i][j] == ' ']
    return random.choice(empty_cells)


# Terminal cleaner
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main body of game
def play_game():
    board = initialize_board()
    player = 'X'

    while True:
        clear_screen()
        rules()
        print_board(board)

        if player == 'X':
            while True:
                print(f'Player {player} turn. (enter row and column): ')
                try:
                    row, col = map(int, input().split())
                    if row in range(3) and col in range(3):
                        break
                    else:
                        clear_screen()
                        print_board(board)
                        print('Error! Enter the correct coordinates.')
                except ValueError:
                    clear_screen()
                    print_board(board)
                    print('Error! Enter two numbers separated by a space.')
        else:
            row, col = computer_move(board)

        if player_move(board, player, row, col):
            if is_winner(board, player):
                clear_screen()
                print_board(board)
                print(f'Player {player} wins!')
                break
            if is_full(board):
                clear_screen()
                print_board(board)
                print('Draw!')
                break
            player = 'O' if player == 'X' else 'X'
        else:
            if player == 'X':
                clear_screen()
                print('The cell is already occupied, choose another one.')
                input('Press Enter to continue...')


if __name__ == '__main__':
    play_game()
