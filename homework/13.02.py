a = [31,342,120,321,10]
x = []
for i in a:
    digit = str(i)
    while True:
        if digit[-1] == '0':
            digit = digit[:-1]
            continue
        break
    x.append(int(digit[::-1]))
print(x)
