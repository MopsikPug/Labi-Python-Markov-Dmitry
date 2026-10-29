import re

def task_1(file):
    file_1 = open(file,mode= 'r', encoding='utf-8')
    text_1 = file_1.read()
    reg_1_num = re.findall(r'[-+]?(?:\d+(?:\.\d+)?|\.\d+)',text_1) #или вместо первого /d (0|[1-9][0-9]*), если не надо,чтобы начиналось с 0
    reg_1_num_add = re.findall(r'[\u00bc-\u00be]',text_1)
    reg_1_words = re.findall(r'\b([a-zA-Z]{6}|[a-zA-Z]{8})\b',text_1)
    all_numbers = reg_1_num + reg_1_num_add
    file_1.close()  
    print('Все числа:', *all_numbers)
    print("Слова 6 и 8:", *reg_1_words)


def task_2(file):
    file_2 = open(file,mode= 'r', encoding='utf-8')
    text_2 = file_2.read()
    reg_2_if2 = re.findall(r'content\s*=\s*"([^"]*)"', text_2)
    reg_2_if1 = re.findall(r"content\s*=\s*'([^']*)'", text_2)
    print(reg_2_if2[:5])
    print(reg_2_if1[:5])
    file_2.close()


def task_3(file):
    ...



#task_1('task1-en.txt')
#task_2('task2.html')
#task_3('task3.txt')
