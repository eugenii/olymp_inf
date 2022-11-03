# гоблины и шаманы
n = int(input())
st = list()
out = list()
for i in range(n):
    goblin = input().split()
    if goblin[0] == "+":
        st.append(goblin[1])
    elif goblin[0] == "*":
        if len(st) <= 1:
            st.append(goblin[1])
        elif len(st) % 2 != 0:
            st.insert(len(st) // 2 + 1, goblin[1])
        elif len(st) % 2 == 0:
            st.insert(len(st) // 2, goblin[1])
    else:
        out.append(st.pop(0))
print(*out, sep="\n")