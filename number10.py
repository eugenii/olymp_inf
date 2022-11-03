m = int(input())
n = int(input())
t= [[0 for _ in range(n)] for _ in range(m)]
r_max = m - 1
r_min = 0
c_max = n - 1
c_min = 0
ind = 1
row = 0
col = n - 1

while ind <= m * n:
    t[row][col] = ind
    ind += 1
    if col == c_max:
        if row != r_max:
            row += 1
        else:
            col -= 1
            c_max -= 1
    elif row == r_max:
        if col != c_min:
            col -= 1
        else:
            row -= 1
            r_max -= 1
    elif col == c_min:
        if row != r_min:
            row -= 1
        else:
            col += 1
            c_min += 1
    elif row == r_min:
        if col != c_max:
            col += 1
        else:
            row += 1
            r_min += 1


  

print(*t, sep='\n')