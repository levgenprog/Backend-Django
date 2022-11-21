a = int(input())

if a % 2 == 0:
    print(2)
else:
    done = False
    for i in range(3, (a // 2) + 1):
        if a % i == 0:
            print(i)
            done = True
            break
    if not done:
        print(a)
