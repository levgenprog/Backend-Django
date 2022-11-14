n = int(input())
even = (n-1) // 2
odd = ((n-2) // 2) + 1

res = (45 * n) + (even * 15) + (odd * 5)

res_h = (res // 60) + 9
res_m = res % 60

print(res_h, res_m)
