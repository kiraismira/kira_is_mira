field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def print_field(my_field):
    print(' _ _ _')
    for i in my_field:
        c = ""
        for b in i:
            c += '|' + b
        print(c + '|')


def make_move(my_field, move, coo):
    if my_field[(coo - 1) // 3][(coo - 1) % 3] == "_":
        my_field[(coo - 1) // 3][(coo - 1) % 3] = move
        return my_field, True
    else:
        return my_field, False


def check_win(my_field):
    win_coord = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
    for i in win_coord:
        if my_field[i[1]] == my_field[i[2]] == my_field[i[3]]:
            return my_field[i[1]] 
        return False
    
    
win = False
while not win:
    print('LETS PLAY!')
    print_field(field)
    move_type = ['X', 'O']
    move_ch = 0
    print('Move of: ', move_type[move_ch % 2])

while True:
    coords = int(input('make your move: '))
    field = make_move(field, move_type[move_ch % 2], coords)[0]
    print_field(field)

    move_ch += 1
    if move_ch > 4:
        tmp = check_win(my_field)
        if tmp:
            print(tmp,'win!')
            win = True
            break
    if move_ch == 9:
        print('dead heat!')
        break
    print_field(my_field)
check_win(my_field)
        

