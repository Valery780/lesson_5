import datetime

x = int(input("Enter a day:"))
y = int(input("Enter a month:"))
z = int(input("Enter a year:"))
try:
    data = datetime.date(z, y, x)
    print(data)
    print("True")
except:
    print("False")
