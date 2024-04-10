
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
# Variant 27
#      Формируется матрица F следующим образом: если в Е сумма чисел по периметру области 1 больше,
# чем количество нулей по периметру области 4, то поменять в С симметрично области 1 и 3 местами,
# иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется
# выражение:((К*AT)*А)-K*FT . Выводятся по мере формирования А, F и все матричные операции последовательно."""
from random import randint as rnd

def printList(z):
    for i in z:
        for j in i:
            print("{:4}".format(j), end=' ')
        print()
    print()

k, n = int(input("k = ")), int(input("n = "))
m = n//2
n = m*2
a = []

for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(rnd(-10,10))

print("Matrix A : ")
printList(a)

b = []
c = []
d = []
e = []
for i in range(m):
    b.append([])
    c.append([])
    d.append([])
    e.append([])
    for j in range(m):
        b[i].append(a[i+m][j+m])
        c[i].append(a[i+m][j])
        d[i].append(a[i][j])
        e[i].append(a[i][j+m])

print("Matrix B : ")
printList(b)
print("Matrix C : ")
printList(c)
print("Matrix D : ")
printList(d)
print("Matrix E : ")
printList(e)

