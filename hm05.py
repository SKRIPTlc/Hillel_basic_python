n = int(input("Введите целое положительное число: "))
sum_cubes = 0
i = 1
while i <= n:
    if i % 3 != 0:
        sum_cubes += i ** 3
    i += 1
print("Сумма кубов всех натуральных чисел от 1 до", n, "с исключением чисел, кратных 3, равна", sum_cubes)

print('&' * 50)

n = int(input("Введите целое положительное число: "))
sum_cubes = 0
for i in range(1, n+1):
    if i % 3 != 0:
        sum_cubes += i ** 3
print("Сумма кубов всех натуральных чисел от 1 до", n, "с исключением чисел, кратных 3, равна", sum_cubes)

