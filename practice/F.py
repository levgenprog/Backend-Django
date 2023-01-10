test = int(input())

x = 0
for _ in range(test):
    oper = input()
    if "--" in oper:
        x -= 1
    elif "++" in oper:
        x += 1

print(x)
