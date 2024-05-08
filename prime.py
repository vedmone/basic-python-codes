try:
    num = int(input('Enter a number: '))
except:
    exit("Only integer please!")

if num < 0:
    exit('Number should be positive')
else:
    for prime in range(2, num):
        if (num % prime)== 0:
            print(num, 'is not a prime number')
            break
    else:
        print(num, 'is a prime number')
