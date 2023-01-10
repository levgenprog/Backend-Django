n = int(input())

if n >= 1 and n <= 4:
    trans = "few"
elif n >= 5 and n <= 9:
    trans = "several"
elif n >= 10 and n <= 19:
    trans = "pack"
elif n >= 20 and n <= 49:
    trans = "lots"
elif n >= 50 and n <= 99:
    trans = "horde"
elif n >= 100 and n <= 249:
    trans = "throng"
elif n >= 250 and n <= 499:
    trans = "swarm"
elif n >= 500 and n <= 999:
    trans = "zounds"
else:
    trans = "legion"

print(trans)
