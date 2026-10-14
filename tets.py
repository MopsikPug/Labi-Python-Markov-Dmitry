

import csv
import random
import xml.etree.ElementTree as ET

# =========================================================================
# ЧАСТЬ 1: Функции для работы с CSV (books.csv / books-en.csv)
# =========================================================================


def count_long_titles(csv_filename, max_length=30):
    """Задание 1: Считает количество книг, у которых название длиннее max_length символов."""
    count = 0
    with open(csv_filename, mode="r", encoding="cp1251") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            title = row.get("Название") or row.get("Title") or ""
            if len(title) > max_length:
                count += 1
    return count


def search_books_by_author(csv_filename, author_name):
    """Задание 2 (Вариант 5: Без ограничений): Ищет все книги заданного автора."""
    if not author_name:
        return []

    found_books = []
    with open(csv_filename, mode="r", encoding="cp1251") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            author = row.get("Автор") or row.get("Author") or ""
            if author_name.lower() in author.lower():
                found_books.append(row)
    return found_books


def generate_links_file(csv_filename, output_filename="links.txt", count=20):
    """Задание 3: Генерирует файл со случайными библиографическими ссылками."""
    # Сначала считываем все книги
    all_books = []
    with open(csv_filename, mode="r", encoding="cp1251") as f:
        reader = csv.DictReader(f, delimiter=";")
        all_books = list(reader)

    # Выбираем случайные записи
    if len(all_books) >= count:
        random_books = random.sample(all_books, count)
    else:
        random_books = all_books

    # Записываем ссылки в текстовый файл
    with open(output_filename, mode="w", encoding="utf-8") as out_f:
        for idx, book in enumerate(random_books, 1):
            author = book.get("Автор") or book.get("Author") or "Неизвестен"
            title = book.get("Название") or book.get("Title") or "Без названия"

            # Пытаемся определить год
            date_field = (
                book.get("Дата поступления")
                or book.get("Год")
                or book.get("Year")
                or "0000"
            )
            year = date_field.split(".")[-1].split("-")[0].strip()

            link_str = f"{idx}. <{author}>. <{title}> - <{year}>\n"
            out_f.write(link_str)


def get_unique_publishers(csv_filename):
    """Допзадание 1: Возвращает множество всех уникальных издательств."""
    publishers = set()
    with open(csv_filename, mode="r", encoding="cp1251") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            pub = row.get("Издательство") or row.get("Publisher")
            if pub:
                publishers.add(pub.strip())
    return publishers


def get_top_popular_books(csv_filename, count=20):
    """Допзадание 2: Возвращает ТОП-20 самых популярных книг по количеству выдач."""
    with open(csv_filename, mode="r", encoding="cp1251") as f:
        reader = csv.DictReader(f, delimiter=";")
        all_books = list(reader)

    # Проверяем, какое поле отвечает за популярность
    first_row = all_books[0] if all_books else {}
    pop_field = "Выдачи" if "Выдачи" in first_row else "Downloads"

    if pop_field not in first_row:
        return None  # Поле популярности не найдено

    # Сортируем по убыванию числового значения
    try:
        sorted_books = sorted(
            all_books, key=lambda x: int(x.get(pop_field) or 0), reverse=True
        )
        return sorted_books[:count], pop_field
    except ValueError:
        return [], pop_field


# =========================================================================
# ЧАСТЬ 2: Функция для работы с XML (currency.xml)
# =========================================================================


def parse_currency_lists(xml_filename):
    """Задание 4 (Вариант 5): Извлекает два отдельных списка: CharCode и Value (с приведением типов)."""
    char_codes = []
    values = []

    tree = ET.parse(xml_filename)
    root = tree.getroot()

    for valute in root.findall("Valute"):
        char_code_node = valute.find("CharCode")
        value_node = valute.find("Value")

        if char_code_node is not None and value_node is not None:
            char_codes.append(char_code_node.text)

            # Приведение типов: заменяем запятую на точку для перевода во float
            val_str = value_node.text.replace(",", ".")
            values.append(float(val_str))

    return char_codes, values


# =========================================================================
# ГЛАВНЫЙ БЛОК УПРАВЛЕНИЯ (Точка входа)
# =========================================================================
if __name__ == "__main__":
    # Имя вашего CSV файла (поменяйте на 'books-en.csv', если нужно)
    CSV_FILE = "books.csv"
    XML_FILE = "currency.xml"

    print("=== ЗАПУСК ЛАБОРАТОРНОЙ РАБОТЫ №2 (ВАРИАНТ 5) ===")

    # --- Вызов Задания 1 ---
    long_titles = count_long_titles(CSV_FILE, max_length=30)
    print(f"\n1. Книг с названием длиннее 30 символов: {long_titles}")

    # --- Вызов Задания 2 ---
    author_to_find = input(
        "\n2. Введите автора для поиска (или Enter для пропуска): "
    ).strip()
    if author_to_find:
        found = search_books_by_author(CSV_FILE, author_to_find)
        print(f"   Найдено книг: {len(found)}")
        for idx, book in enumerate(found[:5], 1):  # Покажем первые 5
            print(
                f"   - {book.get('Автор') or book.get('Author')}: {book.get('Название') or book.get('Title')}"
            )
        if len(found) > 5:
            print("   ...и другие.")

    # --- Вызов Задания 3 ---
    generate_links_file(CSV_FILE, "links.txt", count=20)
    print("\n3. Сгенерирован файл 'links.txt' с 20 случайными ссылками.")

    # --- Вызов Допзадания 1 ---
    all_pubs = get_unique_publishers(CSV_FILE)
    print(f"\nДопзадание 1: Найдено уникальных издательств: {len(all_pubs)}")
    print(f"   Примеры: {list(all_pubs)[:5]}")

    # --- Вызов Допзадания 2 ---
    top_books_data = get_top_popular_books(CSV_FILE, count=20)
    if top_books_data is dict or top_books_data:
        books_list, field_name = top_books_data
        print(f"\nДопзадание 2: ТОП-20 популярных книг (по полю '{field_name}'):")
        for idx, book in enumerate(books_list, 1):
            print(
                f"   {idx}. {book.get('Название') or book.get('Title')} — {book.get(field_name)} выдач"
            )
    else:
        print("\nДопзадание 2: Поле популярности не обнаружено в файле.")

    # --- Вызов Задания 4 (XML) ---
    print("\n" + "=" * 50)
    print("4. Тестирование парсинга XML:")
    try:
        codes_list, values_list = parse_currency_lists(XML_FILE)
        print(f"   [Список 1] CharCode (первые 5): {codes_list[:5]}")
        print(f"   [Список 2] Value (первые 5): {values_list[:5]}")
        print(f"   Длина списков совпадает: {len(codes_list) == len(values_list)} (всего элементов: {len(codes_list)})")
    except FileNotFoundError:
        print(f"   Ошибка: Файл '{XML_FILE}' не найден.")
