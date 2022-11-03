n = int(input())
table = [[int(i) for i in input().split()] for _ in range(n)]
print(*table, sep="\n")
count = 0
for col in range(n - 1):
    for row in range(n - 1):
        temp = set([table[col][row], table[col + 1][row],
            table[col][row + 1], table[col + 1][row + 1]])
        if len(temp) == 4:
            count += 1
print(count)
