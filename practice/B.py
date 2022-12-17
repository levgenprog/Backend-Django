t = int(input())

for _ in range(t):
    l = int(input())
    arr = []
    num = input()
    num = [i for i in num.split()]
    for i in num:
        arr.append(int(i))

    mx = max(arr)
    mn = min(arr)
    cnt = mx - mn
    print(cnt)
