from Exercice2.optimized_game import OptimizedGame
from game import Game


if __name__ == '__main__':
    menu = True
    print("-------------------------------- Jeu de NIM --------------------------------\n")
    while menu:
        nombreJetons = int(input("Veuillez saisir le nombre de jetons (Max. 18 jetons): "))
        playerOption = input("Veuillez choisir le joueur à jouer le premier: Max (o) ou Min (n): ")
        player = True if playerOption == "o" else False
        choice = input("Veuillez un algorithme: Minimax (m) ou Minimax avec élagage (e): ")
        if choice == "m":
            game = Game([nombreJetons], player)
            game.__repr__()
            score = game.minmax()
            print(f"\nLe score final est {score} avec {Game.visited_node} noeuds visités.")
            menu = False
        elif choice == "e":
            optimized_game = OptimizedGame([nombreJetons], player)
            optimized_game.__repr__()
            score = optimized_game.minmax()
            print(f"\nLe score final est {score} avec {OptimizedGame.visited_node} noeuds visités.")
            menu = False
    print(f"\nNB: Score -1 => Min a gagné // Score 1 => Max a gagné")

