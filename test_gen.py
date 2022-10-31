
import random

random_list = [random.getrandbits(32) for i in range(5000000)]

# create a file with those numbers (unsorted!)
with open('numbers_test.txt', 'w') as file:
    for n in random_list:
        file.write(str(n) + '\n')


# data = sorted(map(int, open("numbers_test.txt")))
# print(data)