from itertools import permutations

n = int(input())
nums = [i for i in range(1, n + 1)]

for number in list(permutations(nums)):
    for num in number:
        print(num, end = ' ')
    print()