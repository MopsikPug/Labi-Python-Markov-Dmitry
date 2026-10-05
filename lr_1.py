import time
import os

BLUE = "\u001b[44m"
WHITE = '\u001b[107m'
YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
RED = '\u001b[41m'
RESET = '\u001b[0m'
BEGIN = '\u001b[1G'
ERASE = '\u001b[2K'
RED_2 = '\u001b[31m'
BLUE_2 = "\u001b[34m"
GREEN_2 = '\u001b[32m'
YELLOW_2 = '\u001b[33m'

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
    if len(odd) > 0:
        avg_odd = sum(odd) / len(odd)
    else:
        avg_odd = 0
    if len(even) > 0:
        avg_even = sum(even) / len(even)
    else:
        avg_even = 0

    total_avg = avg_even + avg_odd
    prct_even = (avg_even/total_avg) * 100
    prct_odd = (avg_odd/total_avg) * 100

    bar_length = 100
    fill_odd = round((prct_odd / 100) * bar_length)
    fill_even = bar_length - fill_odd

    print("\nДиаграмма соотношения:")
    print(f"Нечётные: [{RED}{' ' * fill_odd}{RESET}] {prct_odd:.1f}%")
    print(f"Чётные:   [{BLUE}{' ' * fill_even}{RESET}] {prct_even:.1f}%")


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


def run_animation():
    frames = [
        f"{RED_2}  .  {RESET}",      # Кадр 1: маленькая красная точка
        f"{YELLOW_2} o o {RESET}",   # Кадр 2: жёлтые круги побольше
        f"{GREEN_2}( O ){RESET}",    # Кадр 3: зелёный большой круг
        f"{BLUE_2} o o {RESET}"      # Кадр 4: синие сжимающийся круги
    ]
    print("Запуск анимации...")
    time.sleep(1)

    for _ in range(3):
        for frame in frames:
            os.system("cls")

            # Возвращаем курсор в верхний левый угол (ESC-последовательность \033[H)
            print("\033[H") 
            print("--- АНИМАЦИЯ ---")
            print("\n" * 2 + "     " + frame + "\n" * 2)
            print("----------------")
            time.sleep(0.5)
    os.system("cls")
    print("Анимация завершена!")

#flag_Litvi()
#Usor_e()
#file_uslovie()
#grafik(10)
#run_animation()

