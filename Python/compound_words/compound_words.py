import sys
from itertools import permutations

array = []

for line in sys.stdin:
    line = line.strip().split(" ")
    array.extend(line)

chosen_ones = set(["".join(map(str, perm)) for perm in permutations(array, 2)])

for word in sorted(chosen_ones):
    print(word)
