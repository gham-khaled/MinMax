from Exercice2.optimized_game import OptimizedGame
from game import Game

if __name__ == '__main__':
    game = Game([18], True)
    game.__repr__()
    score = game.minmax()
    print(f"\n the score is {score} with {Game.visited_node} nodes visited")
    # print(game.possible_moves())
    optimized_game = OptimizedGame([15], True)
    optimized_game.__repr__()
    score = optimized_game.minmax()
    print(f"\n the score is {score} with {OptimizedGame.visited_node} nodes visited")
