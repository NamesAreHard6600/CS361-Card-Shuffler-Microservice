import random

# EXAMPLE_INPUT = "size=9999"
EXAMPLE_INPUT = "size=100,seed=892374,algorithm=biased"

class DeckShuffler():
    def __init__(self, size, seed=None):
        self.size = size
        self.deck = [i for i in range(self.size)]
        if seed:
            random.seed(seed)

    # Each permutation is exactly as likely
    # Fisher Yates Shuffle
    def true_random(self):
        for i in range(len(self.deck) - 1, 0, -1):
            rand = random.randint(0, i)
            self.deck[i], self.deck[rand] = self.deck[rand], self.deck[i]

    # No element appears in its starting position - Feels more random
    # Derangement Shuffle
    def biased_shuffle(self):
        # First true random it
        self.true_random()
        # Get each fixed point
        fixed_points = [i for i in range(len(self.deck)) if self.deck[i] == i]

        # Remove fixed points
        for fixed_point in fixed_points:
            if self.deck[fixed_point] != fixed_point:
                # No longer a fixed point, got swapped earlier
                continue
            # Swap is guaranteed to not cause a new fixed point
            rand = random.choice([i for i in range(len(self.deck)) if i != fixed_point])
            self.deck[fixed_point], self.deck[rand] = self.deck[rand], self.deck[fixed_point]

        fixed_points = [i for i in range(len(self.deck)) if self.deck[i] == i]

def main():
    # This input handling could be better (like using a dictionary)
    # but it's small enough it's just not worth worrying about (3 inputs)
    size = 10
    seed = None
    algorithm = "random"
    try:
        input = EXAMPLE_INPUT.split(",")
        for x in input:
            x = x.split("=")
            if x[0] == "size":
                size = int(x[1])
            if x[0] == "seed":
                seed = int(x[1])
            if x[0] == "algorithm":
                algorithm = x[1]
    except:
        print("ERROR IN INPUT HANDLING")
        return

    shuffler = DeckShuffler(size, seed)
    if algorithm == "biased":
        shuffler.biased_shuffle()
    else:
        shuffler.true_random()

    print(shuffler.deck)

if __name__ == '__main__':
    main()