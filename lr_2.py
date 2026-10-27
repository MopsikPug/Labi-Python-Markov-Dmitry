import csv
import random
import xml.etree.ElementTree as ET


BOOKS = 'books.csv'
XML = 'currency.xml'

def count_long_titles(csv_filename,max_length):
    
    count = 0
    with open(csv_filename, mode="r", encoding="cp1251") as f: # mode = "r" == для чтения; или utf-8 в encoding
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            title = row.get("Название") or row.get("Title") or ""
            if len(title) > max_length:
                count += 1
    return count


def search_books_by_author(csv_filename, author_name):
    
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
            full_date = str(book['Дата поступления'])
            year = full_date[6:10]
            
            
            txt_file.write(f"{num}. {author}. {title} - {year}\n")
            
    print("Файл 'links.txt' создан.")


def parse_xml(xml_path):
    # Создаем два пустых списка по условию 
    char_codes = []
    values = []
    
    # Открываем и читаем XML файл
    tree = ET.parse(xml_path) #открывает XML-файл и читает его структуру.
    root = tree.getroot() #находит корневой тег, внутри которого лежат все остальные данные.

    
    # Ищем каждый блок <Valute> и забираем оттуда данные
    for valute in root.findall('.//Valute'):
        code = valute.find('CharCode').text
        val = valute.find('Value').text
        
        # Добавляем данные в списки (заменяем запятую на точку, чтобы Python понял число)
        char_codes.append(code)
        values.append(float(val.replace(',', '.')))    
    
    print("Список кодов валют:", char_codes[:5], "... (и так далее)")
    print("Список значений:", values[:5], "... (и так далее)")

def get_popularity(book):
    return int(book['Кол-во выдач'])


def top_20_books(csv_path):
    with open(csv_path, mode='r', encoding='cp1251') as f:
        reader = csv.DictReader(f, delimiter=';')
        books = list(reader)
        
    # Сортируем книги по колонке 'Выдачи'. Если такой колонки нет, код выдаст ошибку
    # Программа берет книги, у которых больше всего выдач, и оставляет первые 20
    popular_books = sorted(books, key = get_popularity, reverse=True)[:20]
    
    print("\nТоп-20 популярных книг:")
    for num, book in enumerate(popular_books, 1):
        print(f" {num}. {book['Название']} — {book['Автор']} (Выдач: {book['Кол-во выдач']})")

def get_tags(csv_path):
    with open(csv_path, mode='r', encoding='cp1251') as f:
        reader = csv.DictReader(f, delimiter=';')
        
        # У DictReader названия всех колонок (заголовки) лежат в свойстве fieldnames
        # Превращаем их в список, чтобы вывести на экран
        headers = list(reader.fieldnames)
        
    print("Перечень заголовков (тегов)", headers)


#print(search_books_by_author(BOOKS, author_name))
#print(count_long_titles(BOOKS,30))
#generate_bibliography(BOOKS)
#get_tags(BOOKS)
#top_20_books(BOOKS)