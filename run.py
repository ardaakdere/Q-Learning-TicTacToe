from TicTacToe import TicTacToe
from Agent import Agent

game = TicTacToe()

## TRAINING PARAMETER SUGGESTION ##
# for player X --> suggestion = discount_factor = 0.6
# for player O --> suggestion = discount_factor = 0.5
agent = Agent(game, 'X',discount_factor = 0.6, episode = 100000)

agent.train_brain_x_byrandom()

agent.play_with_human()
