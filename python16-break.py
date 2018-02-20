flag = True
caller = 'input a number or something else. '

while flag:
    msg = input (caller)

    if msg == 'q' or 'quit':
        flag = False
