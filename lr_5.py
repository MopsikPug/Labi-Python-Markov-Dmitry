import re
import csv

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

    file_3 = open(file, mode='r', encoding='utf-8')
    text_3 = file_3.read()

    reg_id = re.findall(r' ([1-9]\d{0,2}) ', text_3)
    reg_surnames = re.findall(r'\b[A-Z][a-z]+\b', text_3)
    reg_emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text_3)
    reg_sites = re.findall(r'https?://[^\s]+|www\.[^\s]+', text_3)
    
    #ФОРМАТ 1: Год в начале (ГГГГ-ММ-ДД)
    dates_dash_1  = re.findall(r' (\d{4}-\d{2}-\d{2})', text_3)  # с дефисом
    dates_dot_1   = re.findall(r' (\d{4}\.\d{2}\.\d{2})', text_3) # с точкой (точку экранируем \.)
    dates_slash_1 = re.findall(r' (\d{4}/\d{2}/\d{2})', text_3)  # со слэшем

    #ФОРМАТ 2: День в начале (ДД-ММ-ГГГГ)
    dates_dash_2  = re.findall(r' (\d{2}-\d{2}-\d{4})', text_3)  # с дефисом
    dates_dot_2   = re.findall(r' (\d{2}\.\d{2}\.\d{4})', text_3) # с точкой
    dates_slash_2 = re.findall(r' (\d{2}/\d{2}/\d{4})', text_3)  # со слэшем

    reg_dates = dates_dash_1 + dates_dot_1 + dates_slash_1 + dates_dash_2 + dates_dot_2 + dates_slash_2
    reg_id.insert(0,"")
    file_3.close()

    matrix = list(zip(reg_id, reg_surnames, reg_emails, reg_dates, reg_sites))
    matrix.sort(key=lambda x: int(x[0]) if x[0] != "" else -1)
    
    # Записываем всё в csv-файл (используем zip, как в классических простых задачах)
    
    with open('task3_result.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['ID', 'Фамилия', 'Электронная почта', 'Дата регистрации', 'Сайт'])
        
        # Функция zip объединит элементы по порядку
        for row in matrix:
            writer.writerow(row)


def poisk_fragmentov(file):
    file_add = open(file,mode= 'r',encoding='utf-8')
    text_add = file_add.read()

    #ФОРМАТ 1: Год в начале (ГГГГ-ММ-ДД)
    dates_dash_1  = re.findall(r' (\d{4}-\d{2}-\d{2})', text_add)  # с дефисом
    dates_dot_1   = re.findall(r' (\d{4}\.\d{2}\.\d{2})', text_add) # с точкой (точку экранируем \.)
    dates_slash_1 = re.findall(r' (\d{4}/\d{2}/\d{2})', text_add)  # со слэшем

    #ФОРМАТ 2: День в начале (ДД-ММ-ГГГГ)
    dates_dash_2  = re.findall(r' (\d{2}-\d{2}-\d{4})', text_add)  # с дефисом
    dates_dot_2   = re.findall(r' (\d{2}\.\d{2}\.\d{4})', text_add) # с точкой
    dates_slash_2 = re.findall(r' (\d{2}/\d{2}/\d{4})', text_add)  # со слэшем

    reg_dates = dates_dash_1 + dates_dot_1 + dates_slash_1 + dates_dash_2 + dates_dot_2 + dates_slash_2
    reg_emails = re.findall(r' ([\w\.-]+@[\w\.-]+\.\w+)', text_add)
    reg_sites = re.findall(r' (https?://[^\s]+|www\.[^\s]+)', text_add)
    print(*reg_dates)
    print(*reg_emails)
    print(reg_sites)


#task_1('task1-en.txt')
#task_2('task2.html')
#task_3('task3.txt')
#poisk_fragmentov('task_add.txt')