number = int(input('Введите число: '))
prime_divisors = list()
for i in range (1, number):
    if number % i == 0 and i % 2 != 0 or i == 2:
            prime_divisors.append(i)

print(f'Список делителей числа {number}: {prime_divisors}')


    
