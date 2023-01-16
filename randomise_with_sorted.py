from random import random

listed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sorted(listed, key=lambda x: random()))
