def pow(a, b):
    res = a if b != 0 else 1
    for _ in range(1, b):
        res *= a
    return res


def main():
    a = int(input())
    b = int(input())
    print(pow(a, b))


main()
