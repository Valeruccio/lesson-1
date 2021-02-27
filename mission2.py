while True:
    user_number = int(input('Insert any number: '))
    if user_number > 0 and user_number < 10:
        print(user_number**2)
        break
    else:
        print('Insert another number >0 <10')