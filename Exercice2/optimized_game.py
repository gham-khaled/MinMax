from Exercice1.game import Game


class OptimizedGame(Game):
    def minmax(self, alpha=float("-inf"), beta=float("inf")):
        Game.visited_node += 1

        if self.is_over():
            return -1 if self.max_player else 1
        if self.max_player:
            max_score = -1
            for move in self.possible_moves():
                new_state = OptimizedGame(move, False)
                score = new_state.minmax(alpha, beta)
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_score
        else:
            min_score = 1
            for move in self.possible_moves():
                new_state = OptimizedGame(move, True)
                score = new_state.minmax(alpha, beta)
                min_score = min(min_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score
