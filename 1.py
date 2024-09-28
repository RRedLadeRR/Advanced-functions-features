#Timofey
def get_lucky_tickets(a, b):

    lucky_tickets = []
    for i in range(a, b +1):
        digits = 0
        number = i
        while number > 0:
            if number % 10 % 10 % 2 == 0:
                digits += 1
            number //= 10
        if 2 * digits == len(str(i)):
            lucky_tickets.append(i)
    return lucky_tickets

print(get_lucky_tickets(*list(map(int, input("Input range limits via space -->").split()))))