import copy


def possible_split(stack):
    """
    Get the possible division of 1 stack
    :param stack: Number of stack to divide into two stacks
    :return: Example 7 --> [[6,1], [5,2], [4,3]]
    """
    return [[stack - x, x] for x in range(1, int(stack / 2) + 1)]


class Game:
    visited_node = 0

    def __init__(self, stacks, max_player):
        """
        A game is composed with two parameters initial number of stacks and the starting player
        :param stacks (list): The initial number of stack + their disposition
        :param max_player (bool): If true Max player will start

        """
        self.stacks = stacks
        self.max_player = max_player

    def __repr__(self):
        print("\nStacks : ", end='')
        for stack in self.stacks:
            print(str(stack) + " ", end='')

    def is_over(self):
        """
        Check if the game is over when all the stacks cannot be divided
        :return: True if over else False
        """
        return True if max(self.stacks) < 3 else False

    def possible_moves(self):
        """
        Check all the possible future moves from the current disposition
        Example :
            Initial Stack: [6,1]
            Possible Moves: [[5,1,1],[4,2,1]]
        :return: Possible Moves
        """
        possible_moves = []
        for i in range(len(self.stacks)):
            if self.stacks[i] < 3:
                continue
            stack_copy = copy.deepcopy(self.stacks)
            split_stack = stack_copy.pop(i)
            for possible_combination in possible_split(split_stack):
                possible_moves.append(possible_combination + stack_copy)

        return possible_moves

    def minmax(self):
        """
        The MinMax Function.
        1. Check if the game is over
        2. If Max Player create a game for each possible move with starting player Min player and get max result
        3. If Mix Player create a game for each possible move with starting player Max player and get min result
        :return: Final Score 1 or -1 --> if 1 Max Player Won, if -1 Min Player Won
        """
        Game.visited_node += 1
        if self.is_over():
            return -1 if self.max_player else 1
        if self.max_player:
            max_score = -1
            for move in self.possible_moves():
                new_state = Game(move, False)
                score = new_state.minmax()
                max_score = max(max_score, score)

            return max_score
        else:
            min_score = 1
            for move in self.possible_moves():
                new_state = Game(move, True)
                score = new_state.minmax()
                min_score = min(min_score, score)
            return min_score
