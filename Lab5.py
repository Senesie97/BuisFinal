number1 = int(input('Enter number 1:'))
if number1 % 3 == 0 and number1 % 5 == 0:
    print(number1, 'Tic Tac')
elif number1 % 3 == 0:
    print(number1, 'Tic')
elif number1 % 5 == 0:
    print(number1, 'Tac')
else:
    print(number1)
counter = 1
while counter <= 20:
    if counter % 3 == 0 and counter % 5 == 0:
        print(counter, 'Tic Tac')
    elif counter % 3 == 0:
        print(counter, 'Tic')
    elif counter % 5 == 0:
        print(counter, 'Tac')
    else:
        print(counter)

    counter += 1
    import random

    counter = 1

    while counter <= 20:
        random_number = random.randint(1, 100)

        if random_number % 3 == 0 and random_number % 5 == 0:
            print(random_number, 'Tic Tac')
        elif random_number % 3 == 0:
            print(random_number, 'Tic')
        elif random_number % 5 == 0:
            print(random_number, 'Tac')
        else:
            print(random_number)

        counter += 1
attempts = 0

while attempts < 5:
    user_value = int(input('Enter a positive value: '))
    if user_value > 0:
        print('You entered a positive value:', user_value)
        break
    else:
        print('Please enter a value greater than 0.')
        attempts += 1
if attempts == 5:
    print('You exceeded the maximum number of attempts.')
attempts = 0

while attempts < 5:
    user_value = int(input('Enter a positive value: '))
    if user_value > 0:
        random_value = random.randint(1, 100)
        print('Randomly generated value:', random_value)
        if user_value == random_value:
            print('Perfect match!')
        else:
            print('Numbers don\'t match. User value:', user_value, 'Random value:', random_value)

        break
    else:
        print('Please enter a value greater than 0.')
        attempts += 1
if attempts == 5:
    print('You exceeded the maximum number of attempts.')