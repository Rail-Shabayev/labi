# Вариант 27.
# Шеснадцатиричные четные числа, не превышающие 2048 и
# содержащие количество цифр большее, чем вторая цифра числа.
# Вывести числа и их количество. Максимальное число вывести прописью.
import os
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
even = ("0", "2", "4", "6", "8", "A", "C", "E")
file = open("text.txt", "r")
if os.stat("text.txt").st_size == 0:
    print("файл является пустым")
    sys.exit()
for i in file.readline().split():
    if i[0] == "0":
        print("Число " + i + " начинается с 0")
        continue
    try:
        a = int(i, 16)
    except ValueError as error:
        print(error)
        print("Число записано не в 16-ой системе счисления")
    if a < 2048:
        secondDigit = i[1]
        quantityOfDigitsInNumber = str(len(i))
        if quantityOfDigitsInNumber > secondDigit:
            if i[-1].upper() in even:
                desiredDigits.append(i)
                quantityOfDigits += 1
            else:
                print("16-ое число: " + str(i) + " - kисло не четное")
        else:
            print("16-ое число: " + str(i) + " - kоличество цифр меньше второго числа")
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
