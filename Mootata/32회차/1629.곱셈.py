a, b, c = map(int, input().split())

def div(x, y):
    if y == 1:
        return x % c
    else:
        d = div(x, y // 2)
        
        if y % 2 == 0:
            return d * d % c
        else:
            return d * d * x % c

print(div(a, b))