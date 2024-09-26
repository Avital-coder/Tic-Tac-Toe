from agents import human_agent, computer_agent
import time
from alphaBetaAlgo import min_max_alpha_beta
from random import choice

MIN_NUM = float("-inf")
MAX_NUM = float("inf")


class Board:
    board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
    ]

    def print_state(self, state, computer_choice, human_choice):
        chars = {
            -1: human_choice,
            +1: computer_choice,
            0: ' '
        }
        str_line = '---------------'

        print('\n' + str_line)
        for row in state:
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)

    def is_win(self, state, player):
        win_options = [  # Possible winning options
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in win_options:
            return True
        else:
            return False

    def is_game_over(self, state):
        return self.is_win(state, human_agent) or self.is_win(state, computer_agent)

    def blank_cells(self, state):
        cells = []
        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def legal_move(self, x, y):
        if [x, y] in self.blank_cells(self.board):
            return True
        else:
            return False

    def take_move(self, x, y, player):
        if self.legal_move(x, y):
            self.board[x][y] = player
            return True
        else:
            return False

    def ai_algo_turn(self, board, computer_choice, human_choice):
        depth = len(self.blank_cells(board))
        if depth == 0 or self.is_game_over(board):
            return

        print(f'Computer turn [{computer_choice}]')
        self.print_state(board, computer_choice, human_choice)

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = min_max_alpha_beta(
                self, self.board, depth, computer_agent, MIN_NUM, MAX_NUM)
            x, y = move[0], move[1]

        self.take_move(x, y, computer_agent)
        time.sleep(1)

    def human_turn(self, board, computer_choice, human_choice):
        depth = len(self.blank_cells(board))
        if depth == 0 or self.is_game_over(board):
            return

        move = -1
        moves = {  # Possible moves
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        print(f'Human turn [{human_choice}]')
        self.print_state(board, computer_choice, human_choice)

        while move < 1 or move > 9:
            try:
                move = int(
                    input('\nSelect your next move, Choose between (0-9): '))
                coord = moves[move]
                is_legal_move = self.take_move(coord[0], coord[1], human_agent)

                if not is_legal_move:
                    print('Ilegal move, select another one.')
                    move = -1

            except (EOFError, KeyboardInterrupt):
                exit()
            except (KeyError, ValueError):
                print('Bad choice')
