import time
import math

WHITE = '\u001b[107m'
YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
RED = '\u001b[41m'
RESET = '\u001b[0m'
BEGIN = '\u001b[1G'
ERASE = '\u001b[2K'

def flag_Litvi():
    height = 9
    for i in range(height):
        if i < height // 3:
            print(f'{YELLOW}{('   ' * 18)}{RESET}')
        elif height // 3 <= i < (2 * height) // 3:
            print(f'{GREEN}{('   ' * 18)}{RESET}')
        else:
            print(f'{RED}{('   ' * 18)}{RESET}')


def Usor_e():
    width = 21
    height = 8
    matrix = [[' ' for _ in range(width)] for __ in range(height)]
    center_x = (width)//2
    for x in range(width):
        # Находим относительную координату от центра (от -10 до +10)
        x_otnoscentra = x - center_x
        # Заполняем матрицу символами по функции y = sqrt(|x|)
        y = int(1.8 * (abs(x_otnoscentra) ** 0.5))
        #переворачиваем y,ибо в матрице идёт сверху вниз
        y = (height-1) - y
        if 0 <= y < height:
            matrix[y][x] = f"{WHITE} {RESET}"

    for row in matrix:
        print(''.join(row))

    
def file_uslovie():
    file = open('sequence.txt')
    odd,even = [],[]
    numbers = []
    for i in file:
        numbers.append(i)
    for i in range(len(numbers)):
        num = abs(float(numbers[i]))
        if i % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    summa_even, summa_odd = sum(even),sum(odd)
    


def grafik(n):
    #n - размернсоть матрицы
    matrix_grafika = [[" " for _ in range(n+1)] for _ in range(n+1)]
    for x in range(n+1):
        matrix_grafika[n][x] = '—'
    for y in range(n):
        matrix_grafika[y][0] = '|'
    matrix_grafika[n][0] = 'L'
    for i in range(n):#тк n+1,то снизу есть доп линия,можно не переживать
        for j in range(1,n+1):#от 1 чтобы | штуки не удалились
            if i + j  == n:
                matrix_grafika[i][j] = f'{WHITE} {RESET}'
    for row in matrix_grafika:
        print(''.join(row))




    


