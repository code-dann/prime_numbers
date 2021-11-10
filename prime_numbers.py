def is_prime(number):
    factorial = 0

    for i in range(1,number+1):
        if i == 1 or i == number:
            continue
        elif number%i == 0:
            factorial += 1

    if factorial == 0:
        return True
    else:
        return False
        





def run():
    number = int(input('Enter a number: \n'))
    if is_prime(number) == True:
        print('it\'s a prime number')
    else:
        print('Sorry, it isn\'t a prime number')


if __name__ == '__main__':
    run()