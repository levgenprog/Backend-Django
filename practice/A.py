test = int(input())

while test:
    test -= 1
    word = input()
    if len(word) % 2 != 0:
        print("NO")
    else:
        if word[: len(word)//2] == word[len(word)//2:]:
            print("YES")
        else:
            print("NO")
