n = int(input())

res = 0
p = 1

while n != 0:
    rem = n % 10
    res = (rem * p) + res
    p *= 2
    n //= 10
print(res)
