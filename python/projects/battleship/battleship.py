from random import *
import os
import time

field = [[[0] for _ in range(10)] for _ in range(10)]
field_check = [[[0] for _ in range(10)] for _ in range(10)]
ai_field = [[[0] for _ in range(10)] for _ in range(10)]

def ship_direction():
    return choice(['h', 'v'])

def find_random_valid_place(direction, length, field):
    is_empty = lambda x: x == [0]
    has_ship = lambda x: x == [1]

    def process_valid_subrow(valid_subrow):
        if valid_subrow == {}:
            flag = True
            column = None
        else:
            key = choice(list(valid_subrow))
            value = valid_subrow[key]
            
            if key == 0 and value - (length + 1) == 0:
                flag = False
                column = key
            elif key == 0 and value - (length + 1) > 0:
                flag = False
                pos_col = []
                for i in range(value - (length + 1) + 1):
                    pos_col.append(i)
                column = choice(pos_col)
            elif key + value == 10 and value - (length + 1) == 0:
                flag = False
                column = key + 1
            elif key + value == 10 and value - (length + 1) > 0:
                flag = False
                pos_col = []
                for i in range(value - (length + 1) + 1):
                    pos_col.append(key + 1 + i)
                column = choice(pos_col)
            elif value - length == 2:
                flag = False
                column = key + 1
            elif value - length > 2:
                flag = False
                pos_col = []
                for i in range(value - (length + 1)):
                    pos_col.append(key + 1 + i)
                column = choice(pos_col)
            else:
                flag = False
                column = None 
        return flag, column

    def has_valid_subrow(row):
        empty_cells_num = row.count([0]) #len(list(filter(is_empty, row)))
        subrows = {}

        if empty_cells_num < length + 1:
            return {}
        else:
            count_empty_subrow = 0
            tmp = 0
            for i in range(10):
                if row[i] == [0]:
                    count_empty_subrow += 1
                    if count_empty_subrow == 1:
                        tmp = i
                else:
                    if count_empty_subrow == 0:
                        continue
                    else:
                        subrows.setdefault(tmp, count_empty_subrow)
                        count_empty_subrow = 0
                        tmp = 0
            subrows.setdefault(tmp, count_empty_subrow)

            valid_subrows = {}
            for key, value in subrows.items():
                if (key == 0 or key + value == 10) and value >= length + 1:
                    valid_subrows[key] = value
                elif key != 0 and key + value != 10 and value >= length + 2:
                    valid_subrows[key] = value
                else:
                    continue
        return valid_subrows

    flag = True
    attempts = 0
    max_attempts = 1000

    while flag and attempts < max_attempts:
        attempts += 1
        if direction == 'h':
            row = randint(0, 9)
            column = 0

            #Проверяем для первой строки

            if row == 0:
                if all(map(is_empty, field[row])) and all(map(is_empty, field[row + 1])): #Если первая и вторая строка пустые
                    flag = False
                    column = randint(0, 9 - (length - 1))
                elif all(map(is_empty, field[row])) and any(map(has_ship, field[row + 1])): #Если первая строка пустая, вторая непустая
                    valid_subrow = has_valid_subrow(field[row + 1])
                    flag, column = process_valid_subrow(valid_subrow)
                elif any(map(has_ship, field[row])) and all(map(is_empty, field[row + 1])): #Если первая строка непустая, вторая пустая
                    valid_subrow = has_valid_subrow(field[row])
                    flag, column = process_valid_subrow(valid_subrow)
                else: #Если обе строки непустые
                    row_0_subrows = has_valid_subrow(field[row])
                    row_1_subrows = has_valid_subrow(field[row + 1])
                    valid_subrow = {key: value for key, value in row_0_subrows.items() if key in row_1_subrows and row_1_subrows[key] >= value}
                    flag, column = process_valid_subrow(valid_subrow)
            #Проверяем для последней строки
            elif row == 9:
                if all(map(is_empty, field[row])) and all(map(is_empty, field[row - 1])): #Если последняя и предпоследняя строка пустые
                    flag = False
                    column = randint(0, 9 - (length - 1))
                elif all(map(is_empty, field[row])) and any(map(has_ship, field[row - 1])): #Если последняя строка пустая, предпоследняя непустая
                    valid_subrow = has_valid_subrow(field[row - 1])
                    flag, column = process_valid_subrow(valid_subrow)
                elif any(map(has_ship, field[row])) and all(map(is_empty, field[row - 1])): #Если последняя строка непустая, предпоследняя пустая
                    valid_subrow = has_valid_subrow(field[row])
                    flag, column = process_valid_subrow(valid_subrow)
                else: #Если обе строки непустые
                    row_0_subrows = has_valid_subrow(field[row])
                    row_1_subrows = has_valid_subrow(field[row - 1])
                    valid_subrow = {key: value for key, value in row_0_subrows.items() if key in row_1_subrows and row_1_subrows[key] >= value}
                    flag, column = process_valid_subrow(valid_subrow)
            #Проверяем строки со 2 по 9
            else:
                if all(map(is_empty, field[row])) and all(map(is_empty, field[row + 1])) and all(map(is_empty, field[row - 1])): #Если все 3 строки пустые
                    flag = False
                    column = randint(0, 9 - (length - 1))
                elif all(map(is_empty, field[row])) and all(map(is_empty, field[row + 1])) and any(map(has_ship, field[row - 1])): #Если 2, 3 пустые, а 1 непустая
                    valid_subrow = has_valid_subrow(field[row - 1])
                    flag, column = process_valid_subrow(valid_subrow)
                elif all(map(is_empty, field[row])) and any(map(has_ship, field[row + 1])) and all(map(is_empty, field[row - 1])): #Если 1, 2 пустые, а 3 непустая
                    valid_subrow = has_valid_subrow(field[row + 1])
                    flag, column = process_valid_subrow(valid_subrow)
                elif any(map(has_ship, field[row])) and all(map(is_empty, field[row + 1])) and all(map(is_empty, field[row - 1])): #Если 1,3 пустые, а 2 непустая
                    valid_subrow = has_valid_subrow(field[row])
                    flag, column = process_valid_subrow(valid_subrow)
                elif all(map(is_empty, field[row])) and any(map(has_ship, field[row + 1])) and any(map(has_ship, field[row - 1])): #Если 2 пустая, а 1 и 3 непустая
                    row_1_subrows = has_valid_subrow(field[row + 1])
                    row_3_subrows = has_valid_subrow(field[row - 1])
                    valid_subrow = {key: value for key, value in row_1_subrows.items() if key in row_3_subrows and row_3_subrows[key] >= value}
                    flag, column = process_valid_subrow(valid_subrow)
                elif any(map(has_ship, field[row])) and all(map(is_empty, field[row + 1])) and any(map(has_ship, field[row - 1])): #Если 3 пустая, а 1 и 2 непустая
                    row_2_subrows = has_valid_subrow(field[row])
                    row_1_subrows = has_valid_subrow(field[row - 1])
                    valid_subrow = {key: value for key, value in row_2_subrows.items() if key in row_1_subrows and row_1_subrows[key] >= value}
                    flag, column = process_valid_subrow(valid_subrow)
                elif any(map(has_ship, field[row])) and any(map(has_ship, field[row + 1])) and all(map(is_empty, field[row - 1])): #Если 1 пустая, а 2 и 3 непустая
                    row_2_subrows = has_valid_subrow(field[row])
                    row_3_subrows = has_valid_subrow(field[row + 1])
                    valid_subrow = {key: value for key, value in row_2_subrows.items() if key in row_3_subrows and row_3_subrows[key] >= value}
                    flag, column = process_valid_subrow(valid_subrow)
                else: #Если все непустые
                    row_1_subrows = has_valid_subrow(field[row - 1])
                    row_2_subrows = has_valid_subrow(field[row])
                    row_3_subrows = has_valid_subrow(field[row + 1])
                    valid_subrow = {}
                    for key in row_2_subrows:
                        if key in row_1_subrows and key in row_3_subrows:
                            values = [row_2_subrows[key]]
                            values.append(row_3_subrows[key])
                            values.append(row_1_subrows[key])
                            valid_subrow[key] = min(values)
                    
                    flag, column = process_valid_subrow(valid_subrow)
        else:
            row = 0
            column = randint(0, 9)

            if column == 0: #Проверяем для первого столбца
                column_row = []
                column_row_next = []

                for rows in field:
                    column_row.append(rows[column])
                    column_row_next.append(rows[column + 1])

                if all(map(is_empty, column_row)) and all(map(is_empty, column_row_next)): #Если первый и второй столбец пустые
                    flag = False
                    row = randint(0, 9 - (length - 1))
                elif all(map(is_empty, column_row)) and any(map(has_ship, column_row_next)): #Если первый столбец пустой, второй непустой
                    valid_subrow = has_valid_subrow(column_row_next)
                    flag, row = process_valid_subrow(valid_subrow)
                elif any(map(has_ship, column_row)) and all(map(is_empty, column_row_next)): #Если первый столбец непустой, вторая непустая
                    valid_subrow = has_valid_subrow(column_row)
                    flag, row = process_valid_subrow(valid_subrow)
                else: #Если оба столбца непустые
                    row_0_subrows = has_valid_subrow(column_row)
                    row_1_subrows = has_valid_subrow(column_row_next)
                    valid_subrow = {key: value for key, value in row_0_subrows.items() if key in row_1_subrows and row_1_subrows[key] >= value}
                    flag, row = process_valid_subrow(valid_subrow)
            elif column == 9: #Проверяем для последнего столбца
                column_row = []
                column_row_before = []

                for rows in field:
                    column_row.append(rows[column])
                    column_row_before.append(rows[column - 1])

                if all(map(is_empty, column_row)) and all(map(is_empty, column_row_before)): #Если последний и предпоследний столбец пустой
                    flag = False
                    row = randint(0, 9 - (length - 1))
                elif all(map(is_empty, column_row)) and any(map(has_ship, column_row_before)): #Если последний столбец пустой, а предпоследний непустой
                    valid_subrow = has_valid_subrow(column_row_before)
                    flag, row = process_valid_subrow(valid_subrow)
                elif any(map(has_ship, column_row)) and all(map(is_empty, column_row_before)): #Если последний столбец непустой, а предпоследний пустой
                    valid_subrow = has_valid_subrow(field[row])
                    flag, row = process_valid_subrow(valid_subrow)
                else: #Если оба столбца непустые
                    row_0_subrows = has_valid_subrow(column_row)
                    row_1_subrows = has_valid_subrow(column_row_before)
                    valid_subrow = {key: value for key, value in row_0_subrows.items() if key in row_1_subrows and row_1_subrows[key] >= value}
                    flag, row = process_valid_subrow(valid_subrow)
            #Проверяем столбцы со 2 по 9
            else:
                column_row_before = []
                column_row = []
                column_row_next = []

                for rows in field:
                    column_row.append(rows[column])
                    column_row_before.append(rows[column - 1])
                    column_row_next.append(rows[column + 1])

                if all(map(is_empty, column_row)) and all(map(is_empty, column_row_next)) and all(map(is_empty, column_row_before)): #Если все 3 столбца пустые
                    flag = False
                    row = randint(0, 9 - (length - 1))
                elif all(map(is_empty, column_row)) and all(map(is_empty, column_row_next)) and any(map(has_ship, column_row_before)): #Если 2, 3 пустые, а 1 непустая
                    valid_subrow = has_valid_subrow(column_row_before)
                    flag, row = process_valid_subrow(valid_subrow)
                elif all(map(is_empty, column_row)) and any(map(has_ship, column_row_next)) and all(map(is_empty, column_row_before)): #Если 1, 2 пустые, а 3 непустая
                    valid_subrow = has_valid_subrow(column_row_next)
                    flag, row = process_valid_subrow(valid_subrow)
                elif any(map(has_ship, column_row)) and all(map(is_empty, column_row_next)) and all(map(is_empty, column_row_before)): #Если 1,3 пустые, а 2 непустая
                    valid_subrow = has_valid_subrow(column_row)
                    flag, row = process_valid_subrow(valid_subrow)
                elif all(map(is_empty, column_row)) and any(map(has_ship, column_row_next)) and any(map(has_ship, column_row_before)): #Если 2 пустая, а 1 и 3 непустая
                    row_1_subrows = has_valid_subrow(column_row_next)
                    row_3_subrows = has_valid_subrow(column_row_before)
                    valid_subrow = {key: value for key, value in row_1_subrows.items() if key in row_3_subrows and row_3_subrows[key] >= value}
                    flag, row = process_valid_subrow(valid_subrow)
                elif any(map(has_ship, column_row)) and all(map(is_empty, column_row_next)) and any(map(has_ship, column_row_before)): #Если 3 пустая, а 1 и 2 непустая
                    row_2_subrows = has_valid_subrow(column_row)
                    row_1_subrows = has_valid_subrow(column_row_before)
                    valid_subrow = {key: value for key, value in row_2_subrows.items() if key in row_1_subrows and row_1_subrows[key] >= value}
                    flag, row = process_valid_subrow(valid_subrow)
                elif any(map(has_ship, column_row)) and any(map(has_ship, column_row_next)) and all(map(is_empty, column_row_before)): #Если 1 пустая, а 2 и 3 непустая
                    row_2_subrows = has_valid_subrow(column_row)
                    row_3_subrows = has_valid_subrow(column_row_next)
                    valid_subrow = {key: value for key, value in row_2_subrows.items() if key in row_3_subrows and row_3_subrows[key] >= value}
                    flag, row = process_valid_subrow(valid_subrow)
                else: #Если все непустые
                    row_1_subrows = has_valid_subrow(column_row_before)
                    row_2_subrows = has_valid_subrow(column_row)
                    row_3_subrows = has_valid_subrow(column_row_next)
                    valid_subrow = {}
                    for key in row_2_subrows:
                        if key in row_1_subrows and key in row_3_subrows:
                            values = [row_2_subrows[key]]
                            values.append(row_3_subrows[key])
                            values.append(row_1_subrows[key])
                            valid_subrow[key] = min(values)
                    
                    flag, row = process_valid_subrow(valid_subrow)

    if attempts == 1000:
        print(f"⚠️ Не удалось найти место для корабля длиной {length} за {max_attempts} попыток")
        return None, None
        #exit()

    return row, column


def field_init(field):
    ships = {}
    ship_four_direction = ship_direction()

    if ship_four_direction == 'h':
        num = randint(0, 9)
        char = randint(0, 6)
        for i in range(char, char + 4):
            field[num][i] = [1]
            ships.setdefault(41, []).append((i, num))
    else:
        num = randint(0, 6)
        char = randint(0, 9)
        for i in range(num, num + 4):
            field[i][char] = [1]
            ships.setdefault(41, []).append((char, i))

    for i in range(3, 0, -1):
        for j in range(i, 5):
            direction = ship_direction()
            if direction == 'h':
                num, char = find_random_valid_place(direction, i, field)
                if None in [num, char]:
                    print('Перезапуск...')
                    field = [[[0] for _ in range(10)] for _ in range(10)]
                    return field_init(field)           
                for k in range(char, char + i):
                    field[num][k] = [1]
                    ships.setdefault(i * 10 + j - i + 1, []).append((k, num))
            else:
                num, char = find_random_valid_place(direction, i, field)
                if None in [num, char]:
                    print('Перезапуск...')
                    field = [[[0] for _ in range(10)] for _ in range(10)]
                    return field_init(field) 
                for k in range(num, num + i):
                    field[k][char] = [1]
                    ships.setdefault(i * 10 + j - i + 1, []).append((char, k))
    return ships

def field_draw(field):
    print('\033[36m', '  ','A', '', 'B', '', 'C', '', 'D', '', 'E', '', 'F', '', 'G', '', 'H', '', 'I', '', 'J', '\033[0m')

    for i in range(10):
        if i == 9:
            print('\033[36m', i + 1, '\033[0m', sep='', end =' ')
        else:
            print('\033[36m', ' ', i + 1, '\033[0m', sep='', end =' ')
        for j in range(10):
            if field[i][j] == [1]:
                print('\033[32m', field[i][j], '\033[0m', sep='', end='')
            elif field[i][j] == [2]:
                print('\033[1;33m', field[i][j], '\033[0m', sep='', end='')
            elif field[i][j] == [7]:
                print('\033[2;36;46m', field[i][j], '\033[0m', sep='', end='')
            elif field[i][j] == [5]:
                print('\033[1;9;31m', field[i][j], '\033[0m', sep='', end='')          
            else:
                print('\033[3;90;46m', field[i][j], '\033[0m', sep='', end='')
                #print(field[i][j], end='') 
        print()

def start():
    os.system('cls')
    print('Добро пожаловать в Морской Бой. Чтобы начать игру, напишите "старт/start". Чтобы выйти из игры напишите "выход/exit"')
    for value in ai_ships.values():
        print(value)
    while True:
        start = input()
        if start.lower() in ['старт', 'start']:
            os.system('cls')
            play()
            break
        elif start.lower() in ['exit', 'выход']:
            print('До свидания!')
            exit()
        else:
            print('Введите "старт/start" или "выход/exit"')

my_ships = field_init(field)
ai_ships = field_init(ai_field)
player_hits = {}
ai_hits = {}
ai_coords = []

def render_fields():
    print(my_ships)
    print('   ' + '-' * 30)
    print('   ---------Ваши корабли---------')
    print('   ' + '-' * 30)
    field_draw(field)
    print('   ' + '-' * 30)
    print('   -------Поле для заметок-------')
    print('   ' + '-' * 30)
    field_draw(field_check)

    print(ai_ships)
    field_draw(ai_field)

def play():
    print('Инициализация игрового поля...')
    render_fields()

    who_is_first = choice(['player', 'ai'])

    print('Игровое поле создано. Определяю кто начнет первым...')
    if who_is_first == 'player':
        print('Вы ходите первым.')
        player_turn()
    else:
        print('Противник ходит первым.')
        ai_turn()

def player_turn():
    print('Введите координаты для удара (например: "b 4"):')
    while True:
        coords = input().split()
        if len(coords) > 4 or len(coords) < 2:
            print('Введите правильные координаты!')
            player_turn()
        elif coords[0].lower() not in 'abcdefghij':
            print('Введите правильную букву столбца!')
            player_turn()
        elif int(coords[1]) not in range(1, 11):
            print('Введите правильное число строки!')
            player_turn()
        else:
            hit_check('player', coords)

def ai_turn():
    time.sleep(2)
    while True:
        coords = [choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']), choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
        x, y = coords
        col, row = ord(x) - 97, int(y) - 1
        
        if (col, row) not in ai_coords:
            ai_coords.append((col, row))
            hit_check('ai', coords)
            break

def ai_logic():
    pass

def hit_check(who, coordinates):
    x, y = coordinates
    col, row = ord(x) - 97, int(y) - 1

    if who == 'player':
        for key, value in ai_ships.items():
            if (col, row) in value:
                player_hits.setdefault(key, []).append((col, row))
                if len(player_hits[key]) == key // 10:
                    for i in range(key // 10):
                        a, b = player_hits[key][i]
                        field_check[b][a] = [5]
                    os.system('cls')
                    print(player_hits)
                    print('Вы уничтожили корабль противника!')
                    print('Ваш ход.')
                    render_fields()
                    player_turn()
                else:
                    os.system('cls')
                    print(player_hits)
                    field_check[row][col] = [2]
                    print('Вы попали по противнику!')
                    print('Ваш ход.')
                    render_fields()
                    player_turn()
                break
        else:
            os.system('cls')
            print(player_hits)
            print('Вы промахнулись!')
            print('Ход противника.')
            field_check[row][col] = [7]
            render_fields()
            ai_turn()
    else:
        for key, value in my_ships.items():
            if (col, row) in value:
                ai_hits.setdefault(key, []).append((col, row))
                if len(ai_hits[key]) == key // 10:
                    for i in range(key // 10):
                        a, b = ai_hits[key][i]
                        field[b][a] = [5]
                    os.system('cls')
                    print(ai_hits)
                    print('Противник уничтожил ваш корабль')
                    print('Ход противника.')
                    render_fields()
                    ai_turn()
                else:
                    os.system('cls')
                    print(ai_hits)
                    field[row][col] = [2]
                    print('Противник попал по вам!')
                    print('Ход противника.')
                    render_fields()
                    ai_turn()
                break
        else:
            os.system('cls')
            print(ai_hits)
            print('Противник промахнулся!')
            print('Ваш ход.')
            field[row][col] = [7]
            render_fields()
            player_turn()      

start()