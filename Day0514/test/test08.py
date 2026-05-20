def factorial_for(um):
    res = 1
    for i in range(1, um + 1):
        res *= i
    return res

# factorial = 0
while True:
    n = m = int(input('请输入n(n需要在0 ~ 15 之间)：'))
    if 3 <= n <= 15 :
        # factorial = n
        # while n - 1 :
        #     n -= 1
        #     factorial *= n
        factorial = factorial_for(n)
        print(f'{m}的阶乘为{factorial}')
        break

    else:
        print('输入的数字需要在0 ~ 15之间，请重新输入')
        continue