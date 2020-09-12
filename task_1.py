def is_prime(x):
    f = True
    for i in range(2, int(x ** 0.5)):
        f = False
    return f


a = int(input('Enter a number:'))
print(is_prime(a))
