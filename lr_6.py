class OpticalDisk:

    def __init__(self,capacity_bytes: int, rpm: int, laser_width_nm: int):
        self.capacity = capacity_bytes     # Ёмкость в байтах
        self.rpm = rpm                     # Обороты в минуту (Rotations Per Minute)
        self.laser_width = laser_width_nm


    def bytes_read_in_20_seconds(self) -> float:
        rotations = self.rpm * (1 / 3)
        total_bytes = rotations * self.capacity
        return total_bytes


    def __add__(self, other):
        # Проверяем, что оба объекта принадлежат строго одному и тому же классу
        if type(self) is not type(other):
            raise TypeError(f"Нельзя сложить объекты разных классов: {type(self).__name__} и {type(other).__name__}")
        
        # Возвращаем сумму ёмкостей (или любую другую логику сложения по вашему выбору)
        return self.capacity + other.capacity


class CD(OpticalDisk):

    def __init__(self, capacity_bytes: int, rpm: int, laser_width_nm: int, cd_type: str):
        super().__init__(capacity_bytes, rpm, laser_width_nm)
         # Добавляем уникальное поле для CD
        self.cd_type = cd_type # Например: "CD-R", "CD-RW"


    def average_rotation_time(self) -> float:
        return (60 / self.rpm)


class DVD(OpticalDisk):

    def __init__(self, capacity_bytes: int, rpm: int, laser_width_nm: int, layers_count: int):
        super().__init__(capacity_bytes, rpm, laser_width_nm)
        # Добавляем уникальное поле для DVD
        self.layers_count = layers_count


    def avg_rotation_time(self) -> float:
        return (60 / self.rpm)

if __name__ == "__main__":
    choice = input("Какой диск вы хотите создать? (Введите CD или DVD): ").strip().upper()

    #Запрашиваем общие параметры
    try:
        capacity = int(input("Введите ёмкость диска (в байтах, например, 734003200): "))
        rpm = int(input("Введите скорость вращения (RPM, например, 500): "))
        laser = int(input("Введите толщину лазера (в нм, например, 780): "))

        #В зависимости от выбора запрашиваем уникальные параметры и создаем объект
        if choice == "CD":
            cd_type = input("Введите тип CD (например, CD-R или CD-RW): ")
            
            #Создаем объект CD из введенных данных
            disk_object = CD(capacity, rpm, laser, cd_type)
            print(f"\nУспешно создан CD диска типа: {disk_object.cd_type}")

        elif choice == "DVD":
            layers = int(input("Введите количество слоев (например, 1 или 2): "))
            
            #Создаем объект DVD из введенных данных
            disk_object = DVD(capacity, rpm, laser, layers)
            print(f"\nУспешно создан DVD с количеством слоев: {disk_object.layers_count}")
        
        else:
            print("Ошибка: Неверный тип диска! Выберите CD или DVD.")
            disk_object = None

        #Если объект успешно создан, выводим результаты расчетов
        if disk_object:
            print(f"--- Результаты расчетов ---")
            print(f"Пройдено байт лазером за 20 секунд: {disk_object.bytes_read_in_20_seconds():,.2f} байт")
            print(f"Среднее время одного оборота: {disk_object.average_rotation_time():.4f} сек.")

    except ValueError:
        print("Ошибка ввода: Ёмкость, RPM, лазер и слои должны быть целыми числами!")
###################################################################################################################
def summa_capacity():
    er = 0
    CLASSES_MAP = {
        "CD": CD,
        "DVD": DVD
    }
    while er == 0:
        try:
            layers_DVD = 1
            cd_type_CD = 'CD-R'
            rpm = 500
            laser_width_nm_ = 800
            c1 = 0
            c2 = 0

            while c1 == 0:
                choice_1 = input("Какой первый диск вы хотите просуммировать? (Введите CD или DVD): ").strip().upper()
                if choice_1 == 'END' or choice_1 == 'КОНЕЦ':
                    er += 1
                    print('Завершение программы')
                    exit()

                if choice_1 in CLASSES_MAP:
                    DiskClass_1 = CLASSES_MAP[choice_1]
                    capacity_disk_1 = int(input("Введите ёмкость диска 1 для суммирования (в байтах, например, 734003200): "))
                    c1 += 1

                else:
                    print('Некорректный тип диска!')

            while c2 == 0:
                choice_2 = input("Какой второй диск вы хотите просуммировать? (Введите CD или DVD): ").strip().upper()
                if choice_2 in CLASSES_MAP:
                    DiskClass_2 = CLASSES_MAP[choice_2]
                    capacity_disk_2 = int(input("Введите ёмкость диска 2 для суммирования (в байтах, например, 734003200): "))
                    c2 += 1
                    
                else:
                    print('Некорректный тип диска!')

            disks_types = [DiskClass_1, DiskClass_2]
            disks_cap = [capacity_disk_1,capacity_disk_2]
            disks = []
            for d in disks_types:
                if d == CD:
                    disk_i = CD(disks_cap.pop(0),rpm,laser_width_nm_,cd_type_CD)
                    disks.append(disk_i)
                elif d == DVD:
                    disk_i = DVD(disks_cap.pop(0),rpm,laser_width_nm_,layers_DVD)
                    disks.append(disk_i)
                else:
                    print('Некорректный тип диска!')
            if len(disks) == 2:
                summa = disks[0] + disks[1]
                print(f'Сумма размеров дисков равна {summa} байтов')

        except TypeError as error:
            print(error)
#summa_capacity