list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = []
for num in list_1:
    if num % 2 == 0:
        list_2.append(num)
    else:
        list_2.append(0)

print(list_1)
print(list_2)

