sumOfEvenNumbers = 0
for i in range(1, 101):
    if i % 2 == 0 :
        sumOfEvenNumbers += i
print(f'100以内的偶数之和为{sumOfEvenNumbers}')