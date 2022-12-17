tests = int(input())

for _ in range(tests):
    n = int(input())
    fr = input()
    fr = [int(i) for i in fr]
    sr = input()
    sr = [int(i) for i in sr]
    goes = True
    for i in range(n):
        if fr[i] == 1 and sr[i] == 1:
            goes = False
    print("YES") if goes else print("NO")
