def Election(*votes):
    return True if votes.count(1) > votes.count(0) else False


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    print(Election(x, y, z))


main()
