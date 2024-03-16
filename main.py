# Лабораторная №2. Регулярные выражения
# Вариант 27.
# Шеснадцатиричные четные числа, не превышающие 2048 и
# содержащие количество цифр большее, чем вторая цифра числа.
# Вывести числа и их количество. Максимальное число вывести прописью.
import os
import re
import sys

number_dict = {'0': 'ноль',
               '1': 'один',
               '2': 'два',
               '3': 'три',
               '4': 'четыре',
               '5': 'пять',
               '6': 'шесть',
               '7': 'семь',
               '8': 'восемь',
               '9': 'девять',
               'A': 'A',
               'B': 'B',
               'C': 'C',
               'D': 'D',
               'E': 'E',
               'F': 'F'}
desiredDigits = []
quantityOfDigits = 0
file = open("text.txt", "r")
size = os.stat("text.txt").st_size
if re.match("0", str(size)):
    print("файл является пустым")
    sys.exit()
for i in file.readline().split():
    if re.match("^0", i[0]):
        print("Число " + i + " начинается с 0")
        continue
    if re.match(r'(0x)?[A-Fa-f0-9]+', i) is False:
        print("Число записано не в 16-ой системе счисления")
    if int(i, 16) < 2048:
        sec = i[1]
        qty = str(len(i))
        if (re.match("[012]", str(sec)) and re.match("3", qty) or
                re.match("[012]", str(sec)) and re.match("3", qty)):
            if re.match("^[0-9A-Fa-f]*[24680ACE]$", i):
                desiredDigits.append(i)
                quantityOfDigits += 1
            else:
                print("16-ое число: " + str(i) + " - число не четное")
        else:
            print("16-ое число: " + str(i) + " - количество цифр меньше второго числа")
    else:
        print("16-ое число: " + str(i) + " - больше 2048 в десятичной системе")

if quantityOfDigits != 0:
    print("цифры походящие по условиям: " + str(desiredDigits))
    print("количство цифр подходящих по условиям: " + str(quantityOfDigits))
    max_number = max(desiredDigits)
    message = ""
    for i in str(max_number):
        message += number_dict.get(i.upper()) + " "
    print("максимальное число из тех чисел, которые подходят по условиям: " + message)
else:
    print("чисел удовлетворяющих условиям нет")
