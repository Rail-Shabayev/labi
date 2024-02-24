# Вариант 27.
# Шеснадцатиричные четные числа, не превышающие 2048 и
# содержащие количество цифр большее, чем вторая цифра числа.
# Вывести числа и их количество. Максимальное число вывести прописью.
import os
import sys

number_dict = {0: 'ноль',
               1: 'один',
               2: 'два',
               3: 'три',
               4: 'четыре',
               5: 'пять',
               6: 'шесть',
               7: 'семь',
               8: 'восемь',
               9: 'девять'}
desiredDigits = []  # переменная которая будет содержать подходящие по условиям числа
quantityOfDigits = 0  # переменная которая будет содержать общее количество подходящих условиям чисел
even = ("0", "2", "4", "6", "8", "A", "C", "E")  # четные числа в 16-ой системе счисления
file = open("text.txt", "r")
if os.stat("text.txt").st_size == 0:
    print("файл является пустым")
    sys.exit()
for i in file.readline().split():  # цикл проходящий через числа файла
    try:
        a = int(i, 16)  # переводит число из 16-ой в 10-ую систему счисления
    except ValueError as error:
        print(error)
        print("Число записано не в 16-ой системе счисления")
    if a < 2048:  # проверяет является ли число меньше 2048
        secondDigit = int(i[1], 16)  # содержит вторую цифру числа переведя его из 16 в 10 систему счисления
        quantityOfDigitsInNumber = len(str(int(i, 16)))  # содержит общее количество цифр числа переведя его из 16 в 10
        if quantityOfDigitsInNumber < secondDigit:  # проверяет является ли общее количество цифр цисла больше
            # его второй цифры
            if i[-1] in even:  # проверяет является ли число четным
                desiredDigits.append(i)  # числа удовлетворяющиt условиям
                quantityOfDigits += 1  # счетчик количества чисел
if quantityOfDigits != 0:
    print("цифры походящие по условиям: " + str(desiredDigits))
    print("количство цифр подходящих по условиям: " + str(quantityOfDigits))
    max_number = max(desiredDigits)
    max_number_in_russian = int(max_number, 16)
    message = ""
    for i in str(max_number_in_russian):
        message += number_dict.get(int(i)) + " "
    print("максимальное число из тех чисел, которые подходят по условиям: " + message)

else:
    print("чисел удовлетворяющих условиям нету")
