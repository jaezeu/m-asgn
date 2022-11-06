
import random

random_list = [random.getrandbits(32) for i in range(5000000)]

# create a file with those numbers and sort them
with open('numbers_sorted.txt', 'w') as sortednumbers:
    for n in sorted(random_list):
        sortednumbers.write(str(n) + '\n')