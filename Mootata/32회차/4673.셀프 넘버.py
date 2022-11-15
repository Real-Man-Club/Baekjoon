nums = set(range(1, 10001))
g_nums = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    g_nums.add(i)

for i in sorted(nums - g_nums):
    print(i)