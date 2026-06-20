from random import *

field = [[[0] for _ in range(10)] for _ in range(10)]
field_check = [[[0] for _ in range(10)] for _ in range(10)]
ai_field = [[[0] for _ in range(10)] for _ in range(10)]

def ship_direction():
    return choice(['h', 'v'])

def find_random_valid_place(direction, length):
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
        #return None, None
        exit()

    return row, column


def field_init(field):
    ship_four_direction = ship_direction()

    if ship_four_direction == 'h':
        num = randint(0, 9)
        char = randint(0, 6)
        for i in range(char, char + 4):
            field[num][i] = [1]
    else:
        num = randint(0, 6)
        char = randint(0, 9)
        for i in range(num, num + 4):
            field[i][char] = [1]

    for i in range(3, 0, -1):
        for j in range(i, 5):
            direction = ship_direction()
            if direction == 'h':
                num, char = find_random_valid_place(direction, i)            
                for k in range(char, char + i):
                    field[num][k] = [1]
            else:
                num, char = find_random_valid_place(direction, i)
                for k in range(num, num + i):
                    field[k][char] = [1]
        
field_init(field)

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
            else:
                print(field[i][j], end='') 
        print()

field_draw(field)