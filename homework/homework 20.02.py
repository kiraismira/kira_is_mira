import random
tickets = 1000
for i in range(tickets):
    numbers_in_tickets = str(random.randint(111111,1000000))
    if numbers_in_tickets[2+4+6] == numbers_in_tickets[1+3+5]:
        print('This is a winner ticket')
    else:
        print('Better luck next time')
