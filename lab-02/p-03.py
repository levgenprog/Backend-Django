a = int(input())

for i in range(1, a // 2 + 1):
    if a % i == 0:
        print(i, end=" ")
print(a)
