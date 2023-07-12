import random


def random_queen_arrangement():
    while True:
        queens = random.sample(range(8), 8)

        if all(queens[i] != queens[j] and queens[i] - queens[j] != i - j and queens[i] - queens[j] != j - i
               for i in range(8) for j in range(i + 1, 8)):
            yield queens


def prefill_queens():
    yield random.sample(range(8), 8)
