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
Усложнение: за чётным элементом одежды след нечетный, за нечетным - чётный
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


def shuffle(n, combination_=()):
    if n == 4:
        combinations.append(combination_)
        return
    for i in range(len(cloths[n])):
        if n > 0:
            if (int(combination_[-1][-1]) % 2) == ((i + 1) % 2): continue
        nord = []
        nord.extend(combination_)
        nord.append(cloths[n][i])
        shuffle(n + 1, nord)


c = int(input("Количество выводимых вариантов : "))

start1 = time.time()
shuffle(0)
end1 = time.time()

pl1 = ['Пиджак ' + str(i + 1) for i in range(0, p, 2)]
bl1 = ['Брюки ' + str(i + 1) for i in range(0, b, 2)]
rl1 = ['Рубашка ' + str(i + 1) for i in range(0, r, 2)]
gl1 = ['Галстук ' + str(i + 1) for i in range(0, g, 2)]

pl2 = ['Пиджак ' + str(i + 1) for i in range(1, p, 2)]
bl2 = ['Брюки ' + str(i + 1) for i in range(1, b, 2)]
rl2 = ['Рубашка ' + str(i + 1) for i in range(1, r, 2)]
gl2 = ['Галстук ' + str(i + 1) for i in range(1, g, 2)]

start2 = time.time()
res_it_1 = list(itertools.islice(itertools.product(pl1, bl2, rl1, gl2, repeat=1), len(combinations)))
res_it_2 = list(itertools.islice(itertools.product(pl2, bl1, rl2, gl1, repeat=1), len(combinations)))
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
for combination in res_it_1:
    if i >= c: break
    print('Комбинация {:} : '.format(i + 1))
    i += 1
    for k in range(4):
        print(combination[k], end=' ')
    print()

for combination in res_it_2:
    if i >= c: break
    print('Комбинация {:} : '.format(i + 1))
    i += 1
    for k in range(4):
        print(combination[k], end=' ')
    print()

print(f"Время выполнения алгоритмически: {end1 - start1:.6f}")
print(f"Время выполнения функций Питона: {end2 - start2:.6f}")
