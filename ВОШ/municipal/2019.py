# municip 2019 # 2 plitka
n= int(input())
m = int(input())
N = int(input())
c = 0
while True:
    x = (n + m) ** 2 - 4 * N + 4 * c
    if (x ** 0.5) % 1 == 0:
        a1 = ((m + n) - x ** 0.5) / 4
        a2 = ((m + n) + x ** 0.5) / 4
        if a1 % 1 == 0:
            print(a1, c)
            break
        if a2 % 1 == 0:
            print(a2, c)
            break
    else:
        c += 1