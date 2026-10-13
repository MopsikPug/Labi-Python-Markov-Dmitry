import csv
import random
import xml.etree.ElementTree as ET


BOOKS = 'books.csv'
XML = 'currency.xml'

def count_long_titles(csv_filename):
    """Задание 1: Считает количество книг, у которых название длиннее max_length символов."""
    max_length = 30
    count = 0
    with open(csv_filename, mode="r", encoding="cp1251") as f:# mode = "r" == для чтения; или cp1251 в encoding
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            title = row.get("Название") or row.get("Title") or ""
            if len(title) > max_length:
                count += 1
    return count


def search_books_by_author(csv_filename, author_name):
    """Задание 2 (Вариант 5: Без ограничений): Ищет все книги заданного автора."""
    if not author_name:
        return 'Нет такого автора!'

    found_books = []
    with open(csv_filename, mode="r", encoding="cp1251") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            author = row.get("Автор") or row.get("Author") or ""
            if author_name.lower() in author.lower():
                found_books.append(row)
    return found_books


def generate_bibliography(csv_path):
    # 1. Просто читаем весь файл в список
    with open(csv_path, mode='r', encoding='cp1251') as f:
        reader = csv.DictReader(f, delimiter=';')
        books = list(reader)

    # 2. Выбираем случайные 20 книг
    random_books = random.sample(books, 20)
    
    # 3. Записываем их в текстовый файл
    with open('links.txt', mode='w', encoding='utf-8') as txt_file:
        for num, book in enumerate(random_books, 1):
            author = book['Автор']
            title = book['Название']
            year = book['Дата поступления'] # Если в таблице просто 'Год', замените на 'Год'
            
            # Записываем строку вида: "1. Автор. Название - Год"
            txt_file.write(f"{num}. {author}. {title} - {year}\n")
            
    print("Задание 3 выполнено! Файл 'links.txt' создан.")


def parse_xml_variant_5(xml_path):
    # Создаем два пустых списка по условию варианта
    char_codes = []
    values = []
    
    # Открываем и читаем XML файл
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # Ищем каждый блок <Valute> и забираем оттуда данные
    for valute in root.findall('.//Valute'):
        code = valute.find('CharCode').text
        val = valute.find('Value').text
        
        # Добавляем данные в списки (заменяем запятую на точку, чтобы Python понял число)
        char_codes.append(code)
        values.append(float(val.replace(',', '.')))
        
    print("\nЗадание 4 выполнено!")
    print("Список кодов валют:", char_codes[:5], "... (и так далее)")
    print("Список значений:", values[:5], "... (и так далее)")


#print(search_books_by_author(BOOKS, author_name))
#print(count_long_titles(BOOKS))
generate_bibliography(BOOKS)

