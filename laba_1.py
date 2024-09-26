"""
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального решения.
Вариант 27. У юноши P пиджаков, B брюк, R рубашек, G галстуков.
Составьте все возможные костюмы из этих предметов.
"""
import itertools
import time

combinations = []

p = int(input('Количество пиджаков = '))
b = int(input('Количество брюк = '))
r = int(input('Количество рубашек = '))
g = int(input('Количество галстуков = '))

pl = ['Пиджак ' + str(i + 1) for i in range(p)]
bl = ['Брюки ' + str(i + 1) for i in range(b)]
rl = ['Рубашка ' + str(i + 1) for i in range(r)]
gl = ['Галстук ' + str(i + 1) for i in range(g)]

cloths = [pl, bl, rl, gl]


def shuffle(n, order_=()):
    if n == 4:
        combinations.append(order_)
        return
    for i in cloths[n]:
        nord = []
        nord.extend(order_)
        nord.append(i)
        shuffle(n + 1, nord)


c = int(input("Количество выводимых вариантов : "))

start1 = time.time()
shuffle(0)
end1 = time.time()

start2 = time.time()
res_it = list(itertools.islice(itertools.product(pl, bl, rl, gl, repeat=1), len(combinations)))
end2 = time.time()

print('Результат работы алгоритмически : ')
i = 0
for combination in combinations:
    if i >= c: break
    print('Комбинация {:} : '.format(i + 1))
    i += 1
    for k in range(4):
        print(combination[k], end=' ')
    print()

print("Результат работы функций Питона : ")
i = 0
for combination in res_it:
    if i >= c: break
    print("Комбинация {:} : ".format(i + 1))
    i += 1
    for k in range(4):
        print(combination[k], end=' ')
    print()

print(f"Время выполнения алгоритмически: {end1 - start1:.6f}")
print(f"Время выполнения функций Питона: {end2 - start2:.6f}")
