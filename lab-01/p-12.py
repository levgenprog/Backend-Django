a = int(input())
b = int(input())
c = int(input())

d = (b * b) + (-4 * a * c)
if d > 0:
    d = d ** 0.5
    x1 = (-b + d) // (2 * a)
    x2 = (-b - d) // (2 * a)
    print(x1, x2)
elif d == 0:
    d = d ** 0.5
    x = -b // (2 * a)
    print(x)
