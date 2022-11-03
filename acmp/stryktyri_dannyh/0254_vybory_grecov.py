# acmp stryktyri_dannih 0254_vybory_grecov
count = int(input())
grec = [int(i) for i in input().split()]
zayav = int(input())
old_g = []
new_g = []
for i in range(zayav):
    t = input().split()
    old_g.append(int(t[0]))
    new_g.append(int(t[1]))
for i in range(count):
    if grec[i] in old_g:
        grec[i] = new_g[old_g.index(grec[i])]
print(*grec)