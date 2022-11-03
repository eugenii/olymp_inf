'''
col1 = [int(i) for i in input().split()]
col2 = [int(i) for i in input().split()]
count = 0
while col1 and col2 and count <= 1000000:
    count += 1
    if (col1[0] > col2[0]) or (col1[0] == 0 and col2[0] == 9):
        col1.append(col1.pop(0))
        col1.append(col2.pop(0))
    elif (col2[0] > col1[0]) or (col2[0] == 0 and col1[0] == 9):
        col2.append(col1.pop(0))
        col2.append(col2.pop(0))
if count >= 1000000:
    print("botva")
elif not col2:
    print('first', count)
else:
    print('second', count)
'''
first = list(map(int, input().split()))
second = list(map(int, input().split()))
count = 0
while first and second and count < 1e6:
    if first[0] == 0 and second[0] == 9:
        first.append(first.pop(0))
        first.append(second.pop(0))
    elif second[0] == 0 and first[0] == 9:
        second.append(first.pop(0))
        second.append(second.pop(0))
    elif first[0] > second[0]:
        first.append(first.pop(0))
        first.append(second.pop(0))
    else:
        second.append(first.pop(0))
        second.append(second.pop(0))
    count += 1

if count >= 1e6:
    print("botva")
elif first:
    print("first", count)
elif second:
    print("second", count)