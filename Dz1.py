a=int(input('Введите первый элемент прогрессии: '))
b=int(input('Введите шаг арифметической прогрессии: '))
c=int(input('Введите длину списка '))
list_ar=[]
for i in range(c):
         list_ar.append(a+i*b)
print(list_ar)