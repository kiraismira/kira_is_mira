def more_less(ml):
    number_1 = int(input('Введіть перше число:'))
    number_2 = int(input('Введіть друге число:'))
    if number_1 < number_2:
        print(number_1 + 'найменше число')
    elif number_1 > number_2:
         print(number_2 + 'найменше число')
    else :
         print('Числа однакові')
