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
from time import time
from itertools import product, islice
from tkinter import *
from tkinter import scrolledtext

combinations = []
res_it_1 = []
res_it_2 = []

window = Tk()
window.title('Лабораторная работа №8')
window.geometry('900x750')

lbl = Label(window, text='Введите количество пиджаков', font=('Times', 12))
lbl.place(relx=0.05, rely=0.05)
pe = Entry(window, width=10)
pe.place(relx=0.35, rely=0.05)
#
lbl = Label(window, text='Введите количество галстуков', font=('Times', 12))
lbl.place(relx=0.05, rely=0.10)
ge = Entry(window, width=10)
ge.place(relx=0.35, rely=0.1)
#
lbl = Label(window, text='Введите количество рубашек', font=('Times', 12))
lbl.place(relx=0.05, rely=0.15)
re = Entry(window, width=10)
re.place(relx=0.35, rely=0.15)
#
lbl = Label(window, text='Введите количество брюк', font=('Times', 12))
lbl.place(relx=0.05, rely=0.2)
be = Entry(window, width=10)
be.place(relx=0.35, rely=0.2)

result_text = scrolledtext.ScrolledText(window, width=75, height=12)
result_text.place(relx=0.5, rely=0.44, anchor=CENTER)

result_text2 = scrolledtext.ScrolledText(window, width=75, height=12)
result_text2.place(relx=0.5, rely=0.80, anchor=CENTER)

lbl = Label(window, text='Алгоритмический результат', font=('Times', 12))
lbl.place(relx=0.67, rely=0.25)
lbl = Label(window, text='Результат функций питона', font=('Times', 12))
lbl.place(relx=0.67, rely=0.61)

def execution():
    global res_it_2
    global res_it_1
    global combinations
    result_text.delete('1.0', END)
    result_text2.delete('1.0', END)
    p = int(pe.get())
    b = int(be.get())
    r = int(re.get())
    g = int(ge.get())

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


    start1 = time()
    shuffle(0)
    end1 = time()
    c = len(combinations)

    pl1 = ['Пиджак ' + str(i + 1) for i in range(0, p, 2)]
    bl1 = ['Брюки ' + str(i + 1) for i in range(0, b, 2)]
    rl1 = ['Рубашка ' + str(i + 1) for i in range(0, r, 2)]
    gl1 = ['Галстук ' + str(i + 1) for i in range(0, g, 2)]

    pl2 = ['Пиджак ' + str(i + 1) for i in range(1, p, 2)]
    bl2 = ['Брюки ' + str(i + 1) for i in range(1, b, 2)]
    rl2 = ['Рубашка ' + str(i + 1) for i in range(1, r, 2)]
    gl2 = ['Галстук ' + str(i + 1) for i in range(1, g, 2)]

    start2 = time()
    res_it_1 = list(islice(product(pl1, bl2, rl1, gl2, repeat=1), c))
    res_it_2 = list(islice(product(pl2, bl1, rl2, gl1, repeat=1), c))
    end2 = time()

    print(f"Время выполнения алгоритмически: {end1 - start1:.6f}")
    print(f"Время выполнения функций Питона: {end2 - start2:.6f}")
    for i in res_it_1:
        for j in i:
            result_text2.insert(INSERT, j + " ")
        result_text2.insert(INSERT, "\n")

    for i in res_it_2:
        for j in i:
            result_text2.insert(INSERT, j + " ")
        result_text2.insert(INSERT, "\n")

    for i in combinations:
        for j in i:
            result_text.insert(INSERT, j + " ")
        result_text.insert(INSERT, "\n")

    combinations = []
    res_it_1  = []
    res_it_2 = []

btn = Button(window, text='Сгенерировать комбинации', command=execution)
btn.place(relx=0.70, rely=0.15, anchor=CENTER)
window.mainloop()
