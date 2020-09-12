print("1-triangle,2-square")
figure = input("Enter a figure: ")

if figure == '1':
    print("Sides of the triangle:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    from math import sqrt

    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Area of the triangle: %.2f" % s)

if figure == '2':
    print("Side of the square:")
    a = float(input("a = "))

    print("Area of the square: %.2f" % (a**2))
