a = int(input("Enter a side of a square:"))


def square(length):
    return 4 * length, length ** 2, length * 2 ** (1 / 2)

print(square(a))
