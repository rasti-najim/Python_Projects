fizzbuzz_list = []
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        num = 'FizzBuzz'
    elif num % 3 == 0:
        num = 'Fizz'
    elif num % 5 == 0:
        num = 'Buzz'

    fizzbuzz_list.append(num)

print(fizzbuzz_list)
