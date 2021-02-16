import numpy as np

class TicTacToe:
    """
    current_state: holds the current game current_state like [0 X 0 0 0 0 0 0 0]
    
    """
    
    def __init__(self):
        self.current_state = np.zeros(9, dtype = np.int8)
        self.winner = None
        self.player = 1
    
    def draw_current_game(self):
        current_state = ['X' if x == 1 else 'O' if x == -1 else '--' for x in self.current_state]
        print(f'{current_state[0]:^5} {current_state[1]:^5} {current_state[2]:^5}')
        print(f'{current_state[3]:^5} {current_state[4]:^5} {current_state[5]:^5}')
        print(f'{current_state[6]:^5} {current_state[7]:^5} {current_state[8]:^5}')
        print('_'*15)
        # print(self.current_state[:3])
        # print(self.current_state[3:6])
        # print(self.current_state[6:])
    
    def get_current_game(self):
        return self.current_state
    
    def get_current_game_tuple(self):
        return tuple(self.current_state)

    def get_available_positions(self):
        return(np.argwhere(self.current_state==0).ravel()) # argwhere returns 2d array, we need to ravel the array
        # [0, 1, 3, 6, 8]

    def reset_game(self):
        self.current_state = np.zeros(9, dtype = np.int8)
        self.player = 1

    def get_player(self):
        return self.player

    """
    It performs real action.
    """
    def make_move(self, action): # player is 1 for X, player is -1 for O
        if action in self.get_available_positions():
            self.current_state[action] = self.player
            #self.draw_current_game()
            self.player *= -1
        else:
            print('It is not available')

    """
    It returns the state which will occurs if action performed
    """
    def _make_move(self, _current_state, action): # it is not proper function for get input from user. should prefer make_move function
        _current_state[action] = self.player
        return _current_state

    """
    It returns the states which will occur if possible actions performed
    """
    def get_next_states(self):
        states = []
        _current_state = self.current_state
        _available_moves = self.get_available_positions()
        for move in _available_moves:
            states.append(self._make_move(_current_state = _current_state, action=move))
        return states
        
    
    def is_winner(self, isgame = False):
        winner_coordinates = np.array([[0,1,2], [3, 4, 5], [6, 7, 8],
                                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                [0, 4, 8], [2, 4, 6]])
        for coordinate in winner_coordinates:
            total = sum(self.current_state[coordinate])
            if total == 3: # X winner
                if isgame:
                    print('X is Winner!')
                self.winner = 1
                self.reset_game()
                return 1
            elif total == -3: # O Winner
                if isgame:
                    print('O is Winner!')
                self.winner = -1
                self.reset_game()
                return -1
            elif sum(self.current_state == 1) == 5: # Draw
                if isgame:
                    print('DRAW')
                self.winner = -2
                self.reset_game()
                return -2
        return False