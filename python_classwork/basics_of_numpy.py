import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]])
print(a)

print(a[0, 0])

#строка , столб
print(a[ : , 2])

#возвращает размерность
print(a.shape)

#возвращает тип элементов
print(a.dtype)

#количество строк
print(len(a))

#перераспределяет уже данное количество элементов
a = a.reshape((4, 3))
print(a)

a.fill(0)
print(a)

#транспонирование
a = a.T
print(a)

a = np.resize(a, (5, 5))
a = np.ones(a.shape)
print(a)
