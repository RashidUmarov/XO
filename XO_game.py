# здесь храним состояние таблицы
TABLE = [['', '', ''],
         ['', '', ''],
         ['', '', '']
         ]

# клетки, занятые игроками
PLAYERS={
    'X':[],
    'O':[]
}

# выигрышные комбинации
WINS=[(1,2,3),
      (4,5,6),
      (7,8,9),
      (1,4,7),
      (2,5,8),
      (3,6,9),
      (1,5,9),
      (3,5,7)
      ]
# лобовая замене '' на '-'
def get_table():
    t=list()
    for row in TABLE:
        temp=list()
        for col in row:
            fig='-' if col=='' else col
            temp.append(fig)
        t.append(temp)
    return t

def show_info():
    print("Игровое поле состоит из 9-ти клеток, которые выглядят так:")
    print("+----------------+")
    print("|      0  1  2   |")
    print("|                |")
    print("| 0    1  2  3   |")
    print("| 1    4  5  6   |")
    print("| 2    7  8  9   |")
    print("+----------------+")
    print(" Чтобы сделать ход нужно ввести:")
    print(" 1) либо строку и столбец, например: 11  -  это центр поля или клетка номер 5")
    print(" 2) либо номер клеткаи, например: 9  -  правый нижний угол (строка 2, столбец 2)")
    print("   что равносильно вводу 22")
    print("                            ")
    print("Например, если первый ход 'Крестиков' будет 02 (или клетка 3)\n"
          " то тогда поле будет выглядить так")
    print("+----------------+")
    print("|      0  1  2   |")
    print("|                |")
    print("| 0    -  -  x   |")
    print("| 1    -  -  -   |")
    print("| 2    -  -  -   |")
    print("+----------------+\n")


def print_table():
    for row in TABLE:
        print(row)


# вывести доску
def print_board():
    table=get_table()
    print(" игровая таболица           подсказка по клеткам")
    print("+----------------+          +----------------+")
    print("|      0  1  2   |          |      0  1  2   |")
    print("|                |          |                |")
    print("| 0    {}  {}  {}   |          | 0    1  2  3   |".format(table[0][0], table[0][1], table[0][2]))
    print("| 1    {}  {}  {}   |          | 1    4  5  6   |".format(table[1][0], table[1][1], table[1][2]))
    print("| 2    {}  {}  {}   |          | 2    7  8  9   |".format(table[2][0], table[2][1], table[2][2]))
    print("+----------------+          +----------------+\n")
# получить ход
def get_stroke(player):
    text = 'Игрок "' + player + '", введите номер клетки (1-9) или строку+столбец (00-01-..-22):'
    choice = ""
    # цикл, пока не введут только цифры
    while not choice.isnumeric():
        choice = input(text)
        check = choice.replace(' ', '')
        if check.isnumeric():
            break
    # завершение игры
    if len(choice) == 1 and choice.find('0') != -1:
        return 0
    elif len(choice) == 1 and (1 <= int(choice) <= 9):  # номер клетки
        return int(choice)
    else:
        if len(choice.replace(' ', '')) == 2:  # строка и столбец
            row = int(choice[0])
            col = int(choice[1])
            cell = row * 3 + col + 1
            if 1 <= cell <= 9:
                return cell
            else:
                print("   Неверный ввод")
                return None
        else:  # число содержит более 2-х знаков
            print("   Неверный ввод")
            return None


# проверка, что клетка не занята
def cell_empty(cell):
    row = (cell - 1) // 3
    col = (cell - 1) % 3
    return True if TABLE[row][col] == '' else False


# отметить ход на доске
def put_stroke(cell, sign):
    row = (cell - 1) // 3
    col = (cell - 1) % 3
    TABLE[row][col] = sign
    PLAYERS[sign].append(cell)


# есть победитель?
def isWinner(sign):
    cells=set(PLAYERS[sign])
    for rule in WINS:
        if len(cells.intersection(set(rule)))==3:
            return True
    return None

# поздравить игрока
def congratulations(player):
    print('Выиграл игрок "' + player + '", поздравляем!')


# начать игру
def start():
    print('')
    signs = ['X', 'O']
    count = 0
    while True:
        player = signs[count % 2]
        stroke = None
        while stroke is None:
            stroke = get_stroke(player)
        if not stroke:
            print('Игра прекращена :(!')
            break
        # клетка свободна?
        if not cell_empty(stroke):
            print("   Клетка занята")
            continue

        print(f'Выбрана клетка {stroke} (строка {(stroke - 1) // 3} столбец {(stroke - 1) % 3})')
        put_stroke(stroke, player)
        #print_table()  # для отладки только
        print_board()
        winner = isWinner(player)
        # игра окончена?
        if not winner:
            count += 1
            if count >= 9:
                print('Все клетки заняты, ходы закончились! Игра завершена')
                break
            continue
        else:
            congratulations(player)
            break


# приветствуем и начинаем игру
print('----- Добро пожаловать в крестики-нолики! (XO) ------')
show_info()
choice = input("Чтобы начать, введите любой символ, чтобы выйти из игры - 0. Введите символ: ")
if choice.find('0') != -1:
    print('Жаль.... Возвращайтесь!')
    quit(-1)
# мы в игре
start()
