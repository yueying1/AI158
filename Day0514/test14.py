l2 = []
num = 100
while num <= 999:
    # digit = 0
    n = num
    l1 = []
    while n > 0:
        # digit += 1
        l1.append(n % 10)
        n //= 10
    sum1 = 0
    for i in l1 :
        sum1 = sum1 + i ** 3
    if sum1 == num :
        l2.append(num)
    num += 1

print(f'100-999间的水仙数有{l2}')
