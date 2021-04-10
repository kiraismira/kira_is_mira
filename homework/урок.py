x = int(input('Введіть місяць(від 1 до 12):'))
def season(s):
    i = 'Зима'
    f = 'Весна'
    c = 'Літо'
    w = 'Осінь'
    a = 'Не вірно'
    
    if x == 12 or x == 1 or x == 2:
        return i
    if x == 3 or x == 4 or x == 5:
        return f
    if x == 6 or x == 7 or x == 8:
        return c
    elif x == 9 or x == 10 or x == 11:
        return w
    else:
        return a
        
