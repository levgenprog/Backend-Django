def doll(acc, d):
    return acc / d


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def fill(acc, d):
    while True:
        try:
            cur = int(input(
                "Введите 1 чтобы поплолнить в тенге, введите 2 чтобы пополнить в долларах"
                "Введите 3 чтобы выйти\n"))
            if cur < 1 or cur > 3:
                raise ValueError
            if cur == 3:
                return acc
            amount = int(input("Внесите сумму\n"))
            if amount < 0:
                raise ValueError
            acc = acc + amount if cur == 1 else acc + (amount * d)
            print(f"Ваш текущий счет теперь равен {toFixed(acc)} тенге")
            return acc
        except ValueError:
            print("Попробуйте еще раз")


def withdraw(acc, d):
    while True:
        try:
            cur = int(input(
                "Введите 1 чтобы снять в тенге, введите 2 чтобы снять в доллары\n"
                "Введите 3 чтобы выйти\n"))
            if cur < 1 or cur > 3:
                raise ValueError
            if cur == 3:
                return acc
            amount = int(input("Внесите сумму\n"))
            if amount < 0:
                raise ValueError
            if acc < amount or (cur == 2 and acc < amount * d):
                print("Не хватает средств")
                raise ValueError
            acc = acc - amount if cur == 1 else acc - (amount * d)
            print(f"Ваш текущий счет теперь равен {toFixed(acc)} тенге")
            return acc
        except ValueError:
            print("Попробуйте еще раз")


def main():
    acc = 2000
    dollar = 460
    while True:
        try:
            command = int(input("Введите 1 чтобы узнать сумму в тенге\n"
                                "Введите 2 чтобы узнать сумму в долларах\n"
                                "Введите 3 чтобы пополнить счет\n"
                                "Введите 4 для вывода средств\n"
                                "Введите 5 чтобы выйти\n"))
            if command > 5 or command < 1:
                raise ValueError
            match command:
                case 1:
                    print(f"Сумма в тенге: {toFixed(acc, 2)}")
                case 2:
                    print(f"Сумма в долларах: {toFixed(doll(acc, dollar))}")
                case 3:
                    acc = fill(acc, dollar)
                case 4:
                    acc = withdraw(acc, dollar)
                case 5:
                    break
            cont = int(input("Желаете продолжить? 1 - Да, другое - Нет\n"))
            if cont != 1:
                break
        except ValueError:
            print("Мне нужно число от 1 до 4")


main()
