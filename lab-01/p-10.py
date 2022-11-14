a = int(input())
b = int(input())
c = int(input())

if a <= b <= c:
    print(a, b, c)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif a <= c <= b:
    print(a, c, b)
elif c <= a <= b:
    print(c, a, b)
else:
    print(c, b, a)
