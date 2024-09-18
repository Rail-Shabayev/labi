# """ С клавиатуры вводятся два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
# B, C, D, E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
# заполнение, а целенаправленное.
# Вид матрицы А:
# D	Е
# С	В
# Каждая из матриц B, C, D, E имеет вид:
#      4
#   3     1
#      2
#      Вариант 27
#      Формируется матрица F следующим образом: если в Е сумма чисел по периметру области 1 больше,
# чем количество нулей по периметру области 4, то поменять в С симметрично области 1 и 3 местами,
# иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется
# выражение:((К*AT)*А)-K*FT . Выводятся по мере формирования А, F и все матричные операции последовательно."""
from random import randint as rnd


def print_list(mtx):
    for i in mtx:
        for j in i:
            print("{:5}".format(j), end=' ')
        print()
    print()


k, n = int(input("введите k = ")), int(input("введите n = "))
a = []
middle = n // 2
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(rnd(-10, 10))

print("матрица A : ")
print_list(a)

b, c, d, e = [], [], [], []
for i in range(middle):
    b.append([])
    c.append([])
    d.append([])
    e.append([])
    for j in range(middle):
        b[i].append(a[i + middle][j + middle])
        c[i].append(a[i + middle][j])
        d[i].append(a[i][j])
        e[i].append(a[i][j + middle])

print("матрица B : ")
print_list(b)
print("матрица C : ")
print_list(c)
print("матрица D : ")
print_list(d)
print("матрица E : ")
print_list(e)

zero_count = 0
for i in range(middle):  # Считаем кол-во нулей в 4 области в матрице E
    for j in range(middle):
        if (i <= j) and ((i + j + 1) <= middle):
            if e[i][j] == 0:
                zero_count += 1

perimeter = (sum(e[0][i] for i in range(1, middle)) +  # Считаем сумму чисел периметра в 1 области в матрице Е
             sum(e[middle][i] for i in range(1, n % 2)) +
             sum(e[middle - i][middle] for i in range(1, n % 2 + 1)) +
             sum(e[middle - i][0] for i in range(1, middle)))

print("Сравниваем кол-во нулей и сумму периметра:")
if zero_count < perimeter:
    for indx_i, i in zip(range(len(c)), c):
        for indx_j, j in zip(range(len(i)), i):
            if indx_j <= indx_i <= len(i) - indx_j - 1:
                c[indx_i][indx_j], c[len(i) - 1 - indx_i][len(i) - 1 - indx_j] = c[len(i) - 1 - indx_i][
                    len(i) - 1 - indx_j], c[indx_i][indx_j]
    print("матрица C : ")
    print_list(c)
else:
    b, e = e, b
    print("матрица B : ")
    print_list(b)
    print("матрица E : ")
    print_list(e)

f = [[0 for j in range(n)] for i in range(n)]
for i in range(middle):  # Создаем матрицу f
    for j in range(middle):
        f[i][j] = d[i][j]
        f[i][middle + j] = e[i][j]
        f[middle + i][j] = c[i][j]
        f[middle + i][middle + j] = b[i][j]
print('матрица F:')
print_list(f)


def trans_mtx(mtx):
    trans_m = [[mtx[j][i] for j in range(n)] for i in range(n)]
    return trans_m


def multiply_mtx(mtx1, mtx2):
    result_matrix = [[0 for _ in range(len(mtx1))] for _ in range(len(mtx1))]
    for i in range(len(mtx1)):
        for j in range(len(mtx1)):
            for k in range(len(mtx1)):
                result_matrix[i][j] += mtx1[i][k] * mtx2[k][j]
    return result_matrix


def multiply_number(k, mtx):
    result_matrix = [[0 for _ in range(len(mtx))] for _ in range(len(mtx))]
    for i in range(len(mtx)):
        for j in range(len(mtx)):
            result_matrix[i][j] = k * mtx[i][j]
    return result_matrix


def subtract_mtx(mtx1, mtx2):
    result_matrix = [[0 for _ in range(len(mtx1))] for _ in range(len(mtx1))]
    for i in range(len(mtx1)):
        for j in range(len(mtx1[0])):
            result_matrix[i][j] = mtx1[i][j] - mtx2[i][j]
    return result_matrix

print("выражение ((К*A^T)*А)-K*F^T")
print("транспонируем матрицы А и F")
print("матрица А^T:")
aT = trans_mtx(a)
print_list(aT)
print("матрица F^T:")
fT = trans_mtx(f)
print_list(fT)
print("умножаем k на А^T")
x1 = multiply_number(k, aT)
print_list(x1)
print("умножаем (k * A^T) на А")
x2 = multiply_mtx(x1, a)
print_list(x2)
print("умножаем k на F^T")
x3 = multiply_number(k, fT)
print_list(x3)
print("вычитаем два выражения")
result = subtract_mtx(x2, x3)
print_list(result)