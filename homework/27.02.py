divide_line = input('Enter numbers:')

def dividing_function(first,second):
    numerical_data = 'числові'
    not_numerical_data = 'не числові'
    for i in divide_line:
        if i == 2 :
            
            numerical_data.extend(i)
        else:
            
            not_numerical_data.extend(i)
print(numerical_data,not_numerical_data)
