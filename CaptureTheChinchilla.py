# Author: Valerie Armstrong
# GitHub username: MicroChipCookies
# Date: 08/08/2025
# Description: This program represents a board game played by 2 players on a 7 x 7 grid. Each player starts with 2
# narwhals, 2 okapis, 2 marmosets, and one chinchilla. To start, each player's pieces are lined up on opposite sides
# of the board with the chinchilla in the middle with an okapi on either side of it. Immediately next to the okapis
# are the marmosets, and finally, in the corners are the narwhals. The goal of the game is to capture your opponent's
# chinchilla. To capture an opponents piece, a player must land on the same space as the opponent's piece. On each turn,
# Narwhals can jump two spaces diagonally or one space orthogonally. Marmosets can slide up to 4 spaces diagonally
# or one space orthogonally. Okapis can slide one space in any direction, and chinchillas can slide up to 3 spaces
# orthogonally or one space diagonally. Sliding pieces may not move past another piece on the board. No piece may
# move off the board or land on a space with another piece on its own team. Player 1 controls the tangerine pieces, and
# Player 2 controls the amethyst pieces.

#   Starting state of game board
#      A     B     C     D     E     F     G
#   |-----|-----|-----|-----|-----|-----|-----|
# 1 | N1T | M1T | O1T | CHT | O2T | M2T | N2T |
#   |-----|-----|-----|-----|-----|-----|-----|
# 2 |     |     |     |     |     |     |     |
#   |-----|-----|-----|-----|-----|-----|-----|
# 3 |     |     |     |     |     |     |     |
#   |-----|-----|-----|-----|-----|-----|-----|
# 4 |     |     |     |     |     |     |     |
#   |-----|-----|-----|-----|-----|-----|-----|
# 5 |     |     |     |     |     |     |     |
#   |-----|-----|-----|-----|-----|-----|-----|
# 6 |     |     |     |     |     |     |     |
#   |-----|-----|-----|-----|-----|-----|-----|
# 7 | N1A | M1A | O1A | CHA | O2A | M2A | N2A |
#   |-----|-----|-----|-----|-----|-----|-----|


class AnimalGame:
    """
    Describes an animal game object. Animal Games have Piece objects, which are placed on its game board. Players
    can move pieces and capture pieces. The player who captures the other player's chinchilla piece wins the game.
    """

    def __init__(self):
        """
        Starts a new animal game. Generates a game board and uses the Chinchilla, Okapi, Marmoset, and Narwhal
        classes to create game pieces, which it then places on the board in their starting locations. Player 1 is
        initialized to 'tangerine'.
        """
        self._player = 'tangerine'        # Player 1 is tangerine, and player 2 is amethyst
        self._columns = ('A', 'B', 'C', 'D','E', 'F', 'G')
        self._rows = ('1', '2', '3', '4', '5', '6', '7')
        self._game_board = {}   # Initialize empty dictionary, keys will be square names ('A1', 'B1', ... , 'F7', 'G7')
                                # Values will be the piece object on that square, if any, otherwise None.
        self._winner = ''    # '' == 'UNFINISHED', 'tangerine' == 'TANGERINE_WON', 'amethyst' == 'AMETHYST_WON'
        self._game_message = "Let's play!"  # Used to display errors and win messages

        def _generate_pieces(team):
            """
            Creates new pieces and adds them to the game board in their initial positions
            :param team: string, 'tangerine' or 'amethyst'
            :return: None
            """
            # Initialize the pieces in order from left to right across the board
            pieces = []
            pieces.append(Narwhal(team, 1))
            pieces.append(Marmoset(team,1))
            pieces.append(Okapi(team, 1))
            pieces.append(Chinchilla(team))
            pieces.append(Okapi(team, 2))
            pieces.append(Marmoset(team, 2))
            pieces.append(Narwhal(team, 2))

            # Add the pieces to the board
            if team == 'tangerine':
                start_row = '1'
            else:
                start_row = '7'

            for col_index, column in enumerate(self._columns):
                start_square = column + start_row                       # Set the start square for this piece
                self._game_board[start_square] = pieces[col_index]      # Place the next piece from the list onto the board

        # Create the game board
        for col_index, column in enumerate(self._columns):
            # Generate a row of squares with no pieces
            for row_index, row in enumerate(self._rows):
                square_name = column + row
                self._game_board[square_name] = None

        # Add pieces to the game board
        _generate_pieces('tangerine')
        _generate_pieces('amethyst')

    def get_game_state(self):
        """
        Returns the current state of the game
        :return: string, 'UNFINISHED','TANGERINE_WON', or 'AMETHYST_WON'
        """
        if self._winner == '':
            return 'UNFINISHED'
        if self._winner == 'tangerine':
            return 'TANGERINE_WON'
        if self._winner == 'amethyst':
            return 'AMETHYST_WON'

    def get_game_board(self):
        """
        Returns a dictionary. The key for each square is the two character name of the square ('A1', 'A2', ... , 'G7')
        and the value is the piece object that is on that square, if any, otherwise the value is None.
        """
        return self._game_board

    def get_player(self):
        """
        Returns the team name for the player whose turn it is.
        :return: string,team name 'tangerine' or 'amethyst'
        """
        return self._player

    def get_message(self):
        """
        Returns the current message to the user regarding game start, move success, move error, or win
        :return: string, message to user
        """
        return self._game_message

    def _win(self):
        """
        Changes the game state when a player wins.
        :return: None
        """
        self._winner = self._player

    def next_player(self):
        """
        Switches turns to the next player
        :return: None
        """
        if self._player == 'tangerine':
            self._player = 'amethyst'
        else:
            self._player = 'tangerine'

    def make_move(self, move_from, move_to):
        """
        Determines if a move is legal, first checking that it meets the AnimalGame board requirements; then
        calling the Piece's can_move method to ensure that the piece can complete the requested move. If both of these
        conditions are true, it removes the game piece object from the move_from square and adds it to the move_to
        square and returns True. If the move is illegal for any reason, no move is made, and make_move() returns False.
        :param move_from: string, 2 character square name (A1, A2, ... , G6, G7)
        :param move_to: string, 2 character square name (A1, A2, ... , G6, G7)
        :return: True if move was made, False otherwise
        """
        move_from = move_from.upper()
        move_to = move_to.upper()

        def _path_is_blocked(num_horizontal, num_vertical):
            """
            Determines if there is a piece between the move_from and move_to spaces. This does not include whether
            another piece is on the move_to space. Note: This method requires that the move has already been validated
            as either diagonal or horizontal.
            :param num_horizontal: number of horizontal spaces to be moved
            :param num_vertical: number of vertical spaces to be moved
            :return: True if there is a piece blocking the move path, false otherwise
            """
            num_spaces = abs(num_horizontal) - 1
            if abs(num_horizontal) == 0:
                num_spaces = abs(num_vertical) - 1

            step_horizontal = 0
            if num_horizontal < 0:
                step_horizontal = -1
            if num_horizontal > 0:
                step_horizontal = 1

            step_vertical = 0
            if num_vertical < 0:
                step_vertical = -1
            if num_vertical > 0:
                step_vertical = 1

            square_col = self._columns.index(move_from[0])
            square_row = self._rows.index(move_from[1])

            # If there is a piece on an intervening space, return False
            for num in range(num_spaces):
                square_col += step_horizontal
                square_row += step_vertical
                curr_square = self._columns[square_col] + self._rows[square_row]
                if self._game_board[curr_square] is not None:
                    return True

            return False

        board = self._game_board

        # If the game has already begun, no more moves are possible
        if self._winner != '':
            self._game_message = "This game is over, but you can start a new one =)"
            return False

        # If either the move_from or move_to space is not on the board, return False (set error message?)
        if move_from not in board:
            self._game_message = f'{move_from} is not on the game board. Try again.'
            return False
        elif move_to not in board:
            self._game_message = f'{move_to} is not on the game board. Try again.'
            return False

        moving_piece = board[move_from]

        # If there is no piece on move_from if the piece does not belong to current player, move is invalid
        if moving_piece is None:
            self._game_message = f'There is no piece to move from {move_from}. Try again.'
            return False
        elif moving_piece.get_team() != self._player:
            self._game_message = f'The piece on {move_from} belongs to the other team. Try again.'
            return False

        # If the move_from and move_to spaces are the same, it's not really a move
        if move_from == move_to:
            self._game_message = 'You must move at least one square.'
            return False

        # If there is a piece on the move_to space, and it belongs to the current player, the move isn't legal
        if board[move_to] is not None and board[move_to].get_team() == self._player:
            self._game_message = f'One of your pieces is on {move_to}. Try again.'
            return False

        horizontal_move = self._columns.index(move_to[0]) - self._columns.index(move_from[0])
        vertical_move = self._rows.index(move_to[1]) - self._rows.index(move_from[1])

        # If the piece is not able to move the direction and distance requested, return False
        if not moving_piece.can_move(horizontal_move, vertical_move):
            return False

        # Note: If we've gotten this far, the move is either diagonal or orthogonal
        # If the piece can't jump and the path is blocked, return False.
        if not moving_piece.can_jump() and _path_is_blocked(horizontal_move, vertical_move):
            self._game_message = 'Hmm. It appears that path is blocked. Try again.'
            return False

        self._game_message = f'{self._player} moved from {move_from} to {move_to}'

        # Check for capture and win
        captured_piece = board[move_to]
        if captured_piece is not None:
            self._game_message = f'{self._player} captured {str(captured_piece)}'
            if isinstance(board[move_to], Chinchilla):
                self._win()
                self._game_message = f'Congratulations! {self._player} won!'

        # Complete the move and switch players
        board[move_to] = moving_piece
        board[move_from] = None
        self.next_player()
        return True


class Piece:
    """
    Describes a game piece. This serves as a superclass to all game piece types: Chinchilla, Okapi, Marmoset, and
    Narwhal.
    """
    def __init__(self, name, team, jump):
        """
        Creates a new game piece object
        :param name: string, the unique name of the piece
        :param team: string, 'tangerine' or 'amethyst'
        :param jump: boolean, True if piece can jump over pieces when making a move, False otherwise (sliding piece)
        """
        self._name = name
        self._team = team               # 'tangerine' (player 1) or 'amethyst' (player 2)
        self._can_jump = jump

    def __str__(self):
        """Returns the string representation of the Piece object as its unique name attribute."""
        return self._name

    def get_team(self):
        """
        Returns the name of the team the piece belongs to.
        :return: str, 'tangerine' or 'amethyst'
        """
        return self._team

    def can_jump(self):
        """
        Returns True if a piece is a jumping piece, False otherwise
        :return: boolean
        """
        return self._can_jump


class Chinchilla(Piece):
    """
    Describes a chinchilla game piece. Chinchillas can slide up to 3 spaces orthogonally (or one space diagonally).
    Inherits from Piece.
    """

    def __init__(self, team):
        """
        Creates a chinchilla game piece object
        :param team: string, 'tangerine' or 'amethyst'
        """
        name = 'CH' + team[0].upper()
        super().__init__(name, team, False)

    def can_move(self, num_horizontal, num_vertical):
        """
        Determines if the piece can move to the space specified by the horizontal and vertical offsets from its
        current location. Chinchillas can slide up to 3 spaces orthogonally or one space diagonally.
        :param num_horizontal: int, number of spaces to move right if positive. left if negative
        :param num_vertical: int, number of spaces to move down if positive, up if negative
        :return: True if move is within the chinchilla's abilities, False otherwise
        """

        # Exclusive or (bool^bool) tip from: https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python
        # If (the move is orthogonal) and (less than or equal to 3 spaces), the chinchilla can move
        if (bool(num_horizontal) ^ bool(num_vertical)) and abs(num_horizontal + num_vertical) <= 3:
            return True

        # if the move is diagonal and one space, the chinchilla can move
        if abs(num_horizontal) == abs(num_vertical) == 1:
            return True

        return False


class Okapi(Piece):
    """
    Describes an okapi game piece. Okapis can slide one space in any direction. Inherits from Piece.
    """

    def __init__(self, team, num):
        """
        Creates an okapi game piece object
        :param team: string, 'tangerine' or 'amethyst'
        :param num: int, 1 or 2
        """
        name = 'O' + str(num) + team[0].upper()             # O[kapi] + T[angerine] or A[methyst] + '1' or '2'
        super().__init__(name, team, True)

    def can_move(self, num_horizontal, num_vertical):
        """
        Determines if the piece can move to the space specified by the horizontal and vertical offsets from its
        current location. Okapis can jump one space in any direction.
        :param num_horizontal: int, number of spaces to move right if positive. left if negative
        :param num_vertical: int, number of spaces to move down if positive, up if negative
        :return: True if move is within the okapi's abilities, False otherwise
        """

        # Exclusive or (bool^bool) tip from: https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python
        # If (the move is diagonal and one space) or (the move is orthogonal and one space), the okapi can move
        if ( (abs(num_horizontal) == abs(num_vertical) and abs(num_horizontal) == 1) or
            ((bool(num_horizontal) ^ bool(num_vertical)) and abs(num_horizontal + num_vertical) == 1)):
            return True

        return False


class Marmoset(Piece):
    """
    Describes a marmoset game piece. Marmosets can slide up to 4 spaces diagonally (or one space orthogonally).
    Inherits from Piece.
    """

    def __init__(self, team, num):
        """
        Creates a marmoset game piece object
        :param team: string, 'tangerine' or 'amethyst'
        :param num: int, 1 or 2
        """
        name = 'M' + str(num) + team[0].upper()           # M[armoset] + T[angerine] or A[methyst] + '1' or '2'
        super().__init__(name, team, False)

    def can_move(self, num_horizontal, num_vertical):
        """
        Determines if the piece can move to the space specified by the horizontal and vertical offsets from its
        current location. Marmosets can slide up to 4 spaces diagonally as lonng as they're not blocked, or one
        space orthogonally.
        :param num_horizontal: int, number of spaces to move right if positive. left if negative
        :param num_vertical: int, number of spaces to move down if positive, up if negative
        :return: True if move is within the marmoset's abilities, False otherwise
        """
        # if the move is diagonal and <=4 spaces, it can be done
        if abs(num_horizontal) == abs(num_vertical) and abs(num_horizontal) <= 4:
            return True

        # Exclusive or (bool^bool) tip from: https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python
        # if move is orthogonal and == 1 space, it can be done
        if (bool(num_horizontal) ^ bool(num_vertical)) and abs(num_horizontal + num_vertical) == 1:
            return True

        return False


class Narwhal(Piece):
    """
    Describes a narwhal game piece. Narwhals can jump two spaces diagonally (or one space orthogonally).
    Inherits from Piece.
    """

    def __init__(self, team, num):
        """
        Creates a narwhal game piece object
        :param team: string, 'tangerine' or 'amethyst'
        :param num: int, 1 or 2
        """
        name = 'N' + str(num) + team[0].upper()        # N[arwhal] + T[angerine] or A[methyst] + '1' or '2'
        super().__init__(name, team, True)

    def can_move(self, num_horizontal, num_vertical):
        """
        Determines if the piece can move to the space specified by the horizontal and vertical offsets from its
        current location. Narwhals can jump exactly two spaces diagonally or one space orthogonally.
        :param num_horizontal: int, number of spaces to move right if positive. left if negative
        :param num_vertical: int, number of spaces to move down if positive, up if negative
        :return: True if move is within the narwhal's abilities, False otherwise
        """

        # If the move is diagonal and 2 spaces, the narwhal can make the move
        if abs(num_horizontal) == abs(num_vertical) == 2:
            return True

        # If the move is orthogonal and 1 space, the narwhal can make the move
        if (bool(num_horizontal) ^ bool(num_vertical)) and abs(num_horizontal + num_vertical) == 1:
            return True

        return False


def play_game():
    """
    Draws and updates the game board. Prompts users to make moves and displays helpful error messages when a
    move is not legal.
    """
    def game_board_text(game):
        """
        Displays the board for the specified game
        :param game: an AnimalGame object
        :return: String representation of board
        """
        border = '   |-----|-----|-----|-----|-----|-----|-----|'
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        rows = ['1', '2', '3', '4', '5', '6', '7']
        board = game.get_game_board()

        board_string = f'   |  A  |  B  |  C  |  D  |  E  |  F  |  G  | \n{border}\n'

        for row in rows:
            board_string += f' {row} |'   # add row label
            for column in columns:
                square_name = column + row
                piece = board[square_name]
                if piece is None:                # if the space has a piece on it
                    board_string += f'     |'
                else:
                    board_string += f' {str(piece)} |'
            board_string += f'\n{border}\n'

        return board_string

    instructions = """\nWelcome to the Animal Game!\n
    Your goal is to capture your opponent's chinchilla.
    -Narwhals can jump exactly two spaces diagonally or one space up, down, left, or right.
    -Marmosets can slide up to 4 spaces diagonally or one space up, down, left or right.
    -Chinchillas can slide up to 3 spaces up, down, left, or right, or one space diagonally.
    -Okapis can jump one space in any direction.\n
    To move a piece, enter the name of the square it is on (Ex: A1 or G7); then enter the
    name of the square you want to move it to.\n"""

    my_game = AnimalGame()

    print(instructions)
    last_move_successful = True

    while my_game.get_game_state() == 'UNFINISHED':
        if last_move_successful:
            # Display game board and message
            print(f'{game_board_text(my_game)}\n\n{my_game.get_message()}\n\n')
        else:
            # Display error message
            print(f'\n{my_game.get_message()}\n')

        # Prompt player to enter move_from and move_to
        print(f'{my_game.get_player()},\nWhere would you like to move from? ')
        move_from = input()
        print(f'Where would you like to move to? ')
        move_to = input()

        # Make the move, if possible
        last_move_successful = my_game.make_move(move_from, move_to)

    print(f'{game_board_text(my_game)}\n\n{my_game.get_message()}\n\n')


if __name__ == '__main__':
    play_game()

