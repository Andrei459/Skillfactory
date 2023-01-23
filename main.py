# Ввод поля

field = [[" "] * 3 for i in range(3)]

def show_field():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")

# Ввод координат

def vvod():
    while True:
        coords = input("Введите 2 координаты в диапазоне 0-2:").split()

        x, y = coords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2 :
            print("Координаты вне поля!")
            continue

        if field[x][y] != " " :
            print("Координаты заняты!")
            continue

        return x, y

# Провекра выигрышных комбинаций

def win():
    win_coords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                  ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),  ((0, 2), (1, 2), (2, 2)),
                  ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for coord in win_coords:
        win_list = []
        for a in coord:
            win_list.append(field[a[0]] [a[1]])
        if win_list == ["X", "X", "X"]:
            print("Победил Х!")
            return True
        if win_list == ["0", "0", "0"]:
            print("Победил 0!")
            return True
    return False

hod = 0
while True:
    hod += 1

    show_field()

    if hod % 2 ==  1:
        print ("Ход Х")
    else:
        print ("Ход 0")

    x, y = vvod()

    if hod % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        show_field()
        break

    if hod == 9:
        print("Ничья!")
        show_field()
        break