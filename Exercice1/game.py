import copy


def possible_split(stack):
    return [[stack - x, x] for x in range(1, int(stack / 2) + 1)]


class Game:
    visited_node = 0

    def __init__(self, stacks, max_player):
        self.stacks = stacks
        self.max_player = max_player

    def __repr__(self):
        print("\nStacks : ", end='')
        for stack in self.stacks:
            print(str(stack) + " ", end='')

    def is_over(self):
        return True if max(self.stacks) < 3 else False

    def possible_moves(self):
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
