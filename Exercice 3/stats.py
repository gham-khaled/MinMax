from Exercice1.game import Game
from Exercice2.optimized_game import OptimizedGame

if __name__ == '__main__':
    min_stack = 5
    max_stack = 15
    standard_visited_node = 0
    print("MinMax Standard")
    for i in range(min_stack, max_stack):
        game = Game([i], True)
        game.minmax()
        print(f"{i} jetons : {game.visited_node} noeuds visités")
        standard_visited_node += (game.visited_node / i)
        Game.visited_node = 0  # Reinitialize Static Variable
    print(f"Le nombre moyen de noeuds visités est: {standard_visited_node / (max_stack - min_stack)} n ")

    print("MinMax Standard Avec Elagage")
    optimized_visited_node = 0
    for i in range(min_stack, max_stack):
        game = OptimizedGame([i], True)
        game.minmax()
        print(f"{i} jetons : {game.visited_node} noeuds visités")
        optimized_visited_node += (game.visited_node / i)
        Game.visited_node = 0  # Reinitialize Static Variable
    print(f"Le nombre moyen de noeuds visités est: {optimized_visited_node / (max_stack - min_stack)} n ")
