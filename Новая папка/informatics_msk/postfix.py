data = input().split()
stack = list()
while data:
    stack.append(data.pop(0))
    if stack[-1] in "+-*":
        a = stack.pop(-3)
        b = stack.pop(-2)
        c = str(eval(a + stack.pop() + b))
        stack.append(c)
print(int(stack[0]))