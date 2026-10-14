import time
import sys

YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
RED = '\u001b[41m'
BLACK = '\u001b[40m'
RESET = '\u001b[0m'
BEGIN = '\u001b[1G'
ERASE = '\u001b[2K'

def flag():
    height = 9
    for i in range(height):
        if i < height // 3:
            print(f'{YELLOW}{('   ' * 18)}{RESET}')
        elif height // 3 <= i < (2 * height) // 3:
            print(f'{GREEN}{('   ' * 18)}{RESET}')
        else:
            print(f'{RED}{('   ' * 18)}{RESET}')

def print_loading():
    for i in range(100):
        print(f"\u001b[20DProcessing...{i+1}%",end ='',flush = True)
        time.sleep(0.1)
    print(' 67! ')


def draw_multiple(num_tasks):
    bar_width = 25
    for task in range(num_tasks+1):
        for proc in range(1,bar_width+1):
            bar = '#' * proc + '-' * (bar_width - proc)
            print(f'{BEGIN}{ERASE}Task {task}/{num_tasks} [{bar}] {proc*4}%')
            time.sleep(0.1)


def draw_diamond():
    h = 15
    offset = h // 2
    center = h // 2
    step = 1
    length = 1
    colours = [15, 46, 67, 159]
    while True:
        for i in colours:
            for line in range(h):
                print(f"{' ' * offset}\u001b[48;5;{i}m{' ' * length}{RESET}")
                if line < center:
                    offset -= step
                    length += step * 2
                else:
                    offset += step
                    length -= step * 2
            print(f'\u001b[{h+1}A')
            offset = h //2
            length = 1
            time.sleep(2)


def file_process():
    file = open('file.txt','r')
    list1 ,list2 = [],[]
    for line in file:
        number = float(line)
        if (number // 1) % 2 == 0:
            list1.append(number)
        else:
            list2.append(number)
        
    file.close()
    print(f'{RED}{' ' * int((len(list1) * 100)/(len(list1) + len(list2)))}{RESET}')
    print(f'{GREEN}{' ' * int((len(list2) * 100)/(len(list2) + len(list1)))}{RESET}')
    print(len(list1))
    print(len(list2))
    
m = int(sys.argv[1]) if len(sys.argv) > 1 else 3
#flag()
#print_loading()
draw_multiple(m)
#draw_diamond()
#file_process()

