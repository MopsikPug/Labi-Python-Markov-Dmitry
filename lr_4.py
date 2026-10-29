import itertools
# Полный список доступных предметов из таблицы (Имя, Обозначение, Размер, Очки)
def check_combinations_for_capacity(max_cells):
        valid_combos = []
        free_cells = max_cells - mandatory_item[1]

        for r in range(1,len(other_items)+1):
             for combo in itertools.combinations(other_items, r):
                combo_size = sum(item[1] for item in combo)
                if combo_size <= free_cells:
                    backpack = [mandatory_item] + [item for item in combo]
                    score_taken = sum(item[2] for item in backpack)
                    total_score = CURRENT_SCORE + (2 * score_taken - TOTAL_POINTS_ALL)
                    if total_score > 0:
                        valid_combos.append((backpack, total_score))
        return valid_combos


def inventory_combos(solutions):
    for index, (combo, score) in enumerate(solutions, 1):
            inventory_new2 = []
            for sym, size, val in combo:
                inventory_new2.extend([f"[{sym}]"] * size)
            inventory_2d_new = [inventory_new2[i:i+cols] for i in range(0, total_capacity, cols)]
            print(f" {index}. Набор:")   
            for row in inventory_2d_new:
                print(",".join(row))

ITEMS_DATA = {
    "Винтовка": ("r", 3, 25),
    "Пистолет": ("p", 2, 15),
    "Боекомплект": ("a", 2, 15),
    "Аптечка": ("m", 2, 20),
    "Ингалятор": ("i", 1, 5),
    "Нож": ("k", 1, 15),
    "Топор": ("x", 3, 20),
    "Оберег": ("t", 1, 25),
    "Фляжка": ("f", 1, 15),
    "Антидот": ("d", 1, 10),
    "Еда": ("s", 2, 20),
    "Арбалет": ("c", 2, 20)
}

space_of_items = [ITEMS_DATA[item][1] for item in ITEMS_DATA]
value_of_items = [ITEMS_DATA[item][2] for item in ITEMS_DATA]

cols = 4
rows = 2
total_capacity = cols * rows
CURRENT_SCORE = 20
mandatory_item = ITEMS_DATA["Ингалятор"]
remaining_capacity = total_capacity - mandatory_item[1]

other_items = [ITEMS_DATA[itm] for itm in ITEMS_DATA if ITEMS_DATA[itm][0] != "i"]
# Создаем список для хранения максимальной ценности для каждой емкости от 0 до 7
dp = [0] * (remaining_capacity + 1)

# Создаем список списков, чтобы сразу запоминать, какие предметы мы положили
item_combinations = [[] for _ in range(remaining_capacity + 1)]

for item in other_items:
    sym, size, val = item
    
    # Идем по рюкзаку справа налево от 7 до размера текущего предмета
    for w in range(remaining_capacity, size - 1, -1):
        # Проверяем, станет ли ценность больше, если мы возьмем текущий предмет
        if dp[w - size] + val > dp[w]:
            dp[w] = dp[w - size] + val
            item_combinations[w] = item_combinations[w - size] + [item]

final_items = [mandatory_item] + item_combinations[remaining_capacity]           

TOTAL_POINTS_ALL = sum(info[2] for info in ITEMS_DATA.values())
taken_points = sum(item[2] for item in final_items)
final_score = CURRENT_SCORE + (2 * taken_points - TOTAL_POINTS_ALL)

inventory = []
for sym, size, val in final_items:
    inventory.extend([f"[{sym}]"] * size)
inventory_2d = [inventory[i:i+cols] for i in range(0, total_capacity, cols)]   
for row in inventory_2d:
    print(",".join(row))
    
print(f"\nИтоговые очки выживания: {final_score}")
print()
######################################################################################################################################################################################################
solutions_for_7 = check_combinations_for_capacity(7)
    
if len(solutions_for_7) == 0:
    print("РЕШЕНИЙ ДЛЯ 7 ЯЧЕЕК НЕ СУЩЕСТВУЕТ (доказано полным перебором)")
else:
    print(f"Найдено решений: {len(solutions_for_7)}")
    inventory_combos(solutions_for_7)
print()

solutions_for_8 = check_combinations_for_capacity(8)
print(f"Всего найдено подходящих комбинаций: {len(solutions_for_8)}")
inventory_combos(solutions_for_8)