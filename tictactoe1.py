from enum import Enum
import random
import numpy as np

class tictactoe:
    class STATES(Enum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4
    
    def __init__(self):
        # allot first turn to AI or human randomly
        self.game_state = self.STATES(random.getrandbits(1))
        self.game_board = np.chararray((3,3), unicode=True)
        self.game_board[:] = '_'
    
    def place_marker(self, symbol, row, column):
        print(symbol, row, column)
        self.game_board[row, column] = symbol

    #Check game condition, check if any combination in row,col,diag makes a win or draw
    def check_condition(self, marker):
        row_res = np.any(np.all(self.game_board == marker, axis=1))
        col_res = np.any(np.all(self.game_board == marker, axis=0))
        diag_res = ((self.game_board[0,0]==self.game_board[1,1])==self.game_board[2,2]) == marker
        return np.any([row_res, col_res, diag_res])

    #Check if Game is over, check state of game, if no place in board, the game is over
    def is_game_over(self):
        if self.check_condition('x'):
            self.game_state = self.STATES.CROSS_WON
        elif self.check_condition('o'):
            self.game_state = self.STATES.NAUGHT_WON
        elif np.sum(self.game_board == '_') == 0:
            self.game_state = self.STATES.DRAW
        return self.game_state
    
    def evaluate_state(self):
        return 0


    #Display board and state
    def display_game(self):
        print(self.game_board)
        print(self.game_state)
    
    #Instructions to follow to play the game
    def show_instructions(self):
        print("Human will play \'x\' and AI will play \'o\'")
        print('All moves should be entered as row column pairs ranging from 0-2')
        if self.STATES.CROSS_TURN == self.game_state:
            print('Based on a random selection human will play the first turn')
        elif self.STATES.NAUGHT_TURN == self.game_state:
            print('Based on a random selection AI will play the first turn')


    #Get random computer move to play against
    def get_ai_move(self):
        empty_pos = (self.game_board == '_').reshape(-1)
        move = np.random.choice(np.argwhere(empty_pos).reshape(-1))
        move2d = np.argwhere(np.arange(9).reshape(3,3) == move)
        return move2d[0][0], move2d[0][1]

    #Enter your move, enter in Row Coloumn format, a number from 0 to 2
    def get_human_input(self):
        move_row, move_column = input('Enter move as folows: row columns').split()
        move_row, move_column = int(move_row), int(move_column)
        if (  (move_row<0) or (move_column<0) or (move_row>2) or (move_column>2)):
            print('Invalid input, try again')
            move_row, move_column = self.get_human_input()
        elif self.game_board[move_row, move_column] != '_':
            print('Invalid input, try again')
            move_row, move_column = self.get_human_input()
        return move_row, move_column


    
    def play(self):
        self.show_instructions()
        while True:
            self.display_game()
            if self.STATES.CROSS_TURN == self.game_state:
                # wait_for_human
                move_row, move_column = self.get_human_input()
                print('Human played: ',move_row, move_column)
                self.place_marker('x', move_row, move_column)
                self.game_state = self.STATES.NAUGHT_TURN
                self.is_game_over()
            elif self.STATES.NAUGHT_TURN == self.game_state:
                move_row, move_column = self.get_ai_move()
                self.game_state = self.STATES.CROSS_TURN
                self.place_marker('o', move_row, move_column)
                print('AI played: ',move_row, move_column)
                self.is_game_over()
            elif self.STATES.DRAW == self.game_state:
                print("Game has ended in a draw")
                break
            elif self.STATES.NAUGHT_WON == self.game_state:
                print("AI has won the game")
                break
            elif self.STATES.CROSS_WON == self.game_state:
                print("Human user won the game")
                break



if __name__ == "__main__":
    game = tictactoe()
    game.play()


