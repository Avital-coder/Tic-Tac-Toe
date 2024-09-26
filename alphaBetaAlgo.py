from math import inf as infinity
from agents import human_agent, computer_agent


def calculate_value(board, state):
    if board.is_win(state, computer_agent):
        value = +1
    elif board.is_win(state, human_agent):
        value = -1
    else:
        value = 0

    return value


def min_max_alpha_beta(board, state, depth, player, a, b):
    if player == computer_agent:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or board.is_game_over(state):
        value = calculate_value(board, state)
        return [-1, -1, value]

    for cell in board.blank_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        value = min_max_alpha_beta(board, state, depth - 1, -player, a, b)
        state[x][y] = 0
        value[0], value[1] = x, y

        if player == computer_agent:
            best = value if value[2] > best[2] else best
            a = max(a, best[2])
            if b <= a:
                break
        else:
            best = value if value[2] < best[2] else best
            b = min(b, best[2])
            if b <= a:
                break
    return best
