field = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]


def print_field(my_field):
    print(' _ _ _')
    for i in my_field:
        c = ''
        for b in i:
            c +='|' + b
        print(c + '|')


def make_move(my_field,move_type,coords):
    x_or_o = input('Enter x or o:')
    valid = False
    while not valid:
        answer = int(input('Enter where to put(1-9) ' + x_or_o + '?' ))
        if answer >= 1 and answer <= 9:
            if (str(my_field[answer - 1]) not in 'xo'):
                my_field[answer - 1] = move_type
                valid = True
                print(True)
                print(move_type)
            else:
                print('this cage is already taken,False')
                print_field(my_field)




