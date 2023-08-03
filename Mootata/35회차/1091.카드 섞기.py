n = int(input())
p = list(map(int, input().split()))  # 각 카드가 어떤 플레이어에게 가야하는지
s = list(map(int, input().split()))  # 카드를 섞는 방법
cards = {}
answer = 0

for i in range(n):
    cards[i] = i % 3  # 세사람에게 돌아가면서 카드를 줘야함

first = cards  # 맨 처음 카드를 나눠준 순서

while True:
    if list(cards.values()) == p:
        print(answer)
        break

    temp = {}

    for idx, i in enumerate(s):  # s에 따라 카드 섞음
        temp[idx] = cards[i]

    if temp == first:  # 맨 처음 카드를 나눠준 순서와 동일하다면, 루프가 존재한다는 의미
        print(-1)
        break

    cards = temp
    answer += 1


# A B C
# C A B
# B C A
#
# 0 1 2
# 2 0 1
# 1 2 0
# 0 1 2
