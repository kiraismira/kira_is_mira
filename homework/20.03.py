enter = input('Enter:')
words = enter.split('')
answer = {}
for i in words:
    answer[i] = 0
    if i in answer:
        for y in answer.values():
            answ = int(y)
            answ += 1
            answer[i] = y
        answ[y] += 1
print(answ)
