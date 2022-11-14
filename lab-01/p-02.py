n = input()

arr = [int(a) for a in n]

if len(arr) > 1:
    x = arr[-2]
else:
    x = 0

print(x)
