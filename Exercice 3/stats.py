from Exercice1.game import Game
from Exercice2.optimized_game import OptimizedGame

if __name__ == '__main__':
    standard_visited_node = 0
    for i in range(5, 15):
        game = Game([i], True)
        game.__repr__()
        score = game.minmax()
        standard_visited_node += (game.visited_node / i)
        Game.visited_node = 0
    print(f"Le nombre moyen de noeuds visités est: {standard_visited_node / 10} n ")

    standard_visited_node = 0
    for i in range(5, 15):
        game = OptimizedGame([i], True)
        game.__repr__()
        score = game.minmax()
        standard_visited_node += (game.visited_node / i)
        OptimizedGame.visited_node = 0
    print(f"Le nombre moyen de noeuds visités est: {standard_visited_node / 10} n ")
