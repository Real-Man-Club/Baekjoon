for _ in range(int(input())):
    lt, wt, le, we = map(int, input().split())
    isTelecomWin = lt * wt - le * we
    print("Eurecom" if isTelecomWin < 0 else "TelecomParisTech" if isTelecomWin > 0 else "Tie")
