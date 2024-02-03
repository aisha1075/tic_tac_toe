tictactoe=[['-']*3,['-']*3,['-']*3]

#функция, которая показывает текущее состояние игры
def print_game_state(table):
    print("  0 1 2")
    for row in range(len(table)):
        line=str(row)+' '
        for column in range(len(table)):
            line=line+table[row][column]+' '
        print(line)

#функция через которую мы проверяем были ли выполнены условия для победы в игре одним из двух символов
def check_victory(table):
    for row in range(len(table)):
        if table[row][0]==table[row][1] and table[row][1]==table[row][2] and table[row][0]!='-':
            return True, table[row][0]

    for column in range(len(table)):
        if table[0][column]==table[1][column] and table[1][column]==table[2][column] and table[0][column]!='-':
            return True, table[0][column]

    if table[0][0]==table[1][1] and table[1][1]==table[2][2] and table[0][0]!='-':
        return True, table[0][0]
    if table[0][2] == table[1][1] and table[1][1] == table[2][0] and table[0][2] != '-':
        return True, table[0][2]

    return False, None

mark=None
player=1
counter=0
victory=False
#Цикл через который ввод данных продолжается до тех пор пока кто-то не выиграл или не было сделано максимальное количество ходов (9)
while not victory and counter<9:
    print_game_state(tictactoe)
    if player == 1:
        print('X player turn')
    else:
        print('0 player turn')
#цикл в цикле, чтобы избежать повторного ввода на уже занятую позицию в игре или ввода несуществующих позиций
    while True:
        row=int(input('row: '))
        column=int(input('column: '))
        if row<0 or row>2 or column<0 or column>2:
            print('this position is invalid')
            continue
        if tictactoe[row][column] != '-':
            print('this place is already taken, choose another position')
        else:
            break

#ввод X и 0
    if player == 1:
        tictactoe[row][column]='x'
    else:
        tictactoe[row][column] = '0'
# смена игроков
    if player == 1:
        player = 2
    else:
        player = 1

    victory,mark=check_victory(tictactoe)
# прибавляем +1 ход после каждого хода для высчета максимального возможного количества ходов
    counter += 1

# выводим победителя
if mark == 'x':
    print('X won')
else:
    print('0 won')



#вызываем функцию текущего состояния игры
print_game_state(tictactoe)