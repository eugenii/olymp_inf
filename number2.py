d, m, g = [int(i) for i in input().split()]
vis = False
if (g % 100) % 4 == 0 and (g // 100) % 4 == 0:
    vis = True
days = [31, (28, 29)[vis], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
out = sum(days[:m - 1]) + d
print(out)