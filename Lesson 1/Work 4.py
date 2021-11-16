number_x = input("Введите любое целое число: ")
number_x = str(number_x)
n = 0
max = 0
while n < len(number_x):
    if (int(number_x[n]) > max):
        max = int(number_x[n])
    print("число: ", number_x[n], " max: ", max)
    n += 1
print("максимальное число = ", max)