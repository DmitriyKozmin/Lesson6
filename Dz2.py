min=int(input('Введите минимальное значение диапазона индекса: '))
max=int(input('Введите максимальное значение диапазона индекса элемента: '))
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = []
for i in range(len(list_1)):
    if list_1[i]>=min and list_1[i]<=max:
        list_2.append(i)
print(list_2)