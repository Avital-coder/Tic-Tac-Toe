from board import Board
from agents import human_agent, computer_agent


def main():
    boardInstance = Board()
    # What is the symbol for both human and computer
    human_choice = ''
    computer_choice = ''

    # Who is the first player
    first_player = ''

    while human_choice != 'O' and human_choice != 'X':
        try:
            human_choice = input(
                'Choose your symbol, X or O.\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    if human_choice == 'X':
        computer_choice = 'O'
    else:
        computer_choice = 'X'

    while first_player != 'Y' and first_player != 'N':
        try:
            first_player = input('Do you wanna play first? [y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    while len(boardInstance.blank_cells(boardInstance.board)) > 0 and not boardInstance.is_game_over(boardInstance.board):
        if first_player == 'N':
            boardInstance.ai_algo_turn(boardInstance.board,
                                       computer_choice, human_choice)
            first_player = ''

        boardInstance.human_turn(
            boardInstance.board, computer_choice, human_choice)
        boardInstance.ai_algo_turn(boardInstance.board,
                                   computer_choice, human_choice)

    if boardInstance.is_win(boardInstance.board, human_agent):
        print(f'Human turn was [{human_choice}]')
        boardInstance.print_state(boardInstance.board,
                                  computer_choice, human_choice)
        print('NICE, YOU WON!')
    elif boardInstance.is_win(boardInstance.board, computer_agent):
        print(f'Computer turn was [{computer_choice}]')
        boardInstance.print_state(boardInstance.board,
                                  computer_choice, human_choice)
        print('YOU LOSE, Try next time.')
    else:
        boardInstance.print_state(boardInstance.board,
                                  computer_choice, human_choice)
        print('Its\'s a TIE!')

    exit()


if __name__ == '__main__':
    main()
