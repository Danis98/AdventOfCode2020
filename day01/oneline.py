import itertools; print([a * b for a, b in itertools.combinations(list(map(int, open("day01.input", "r").read().strip().split("\n"))), 2) if a + b == 2020][0])

import itertools; print([a * b * c for a, b, c in itertools.combinations(list(map(int, open("day01.input", "r").read().strip().split("\n"))), 3) if a + b + c == 2020][0])