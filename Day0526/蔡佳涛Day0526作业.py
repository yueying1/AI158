import random

num = random.randint(0, 101)
low = 0
high = 100
while True:
    n = input(f'请输入猜测的数字({low} - {high})：')
    try:
        n = int(n)
        if low <= n <= high:
            if n < num:
                print('你猜的数小了')
                low = n + 1
            elif n > num:
                print('你猜的数大了')
                high = n - 1
            elif low == high:
                print(f'正确答案是{num}，这你都猜不中！！')
                break
            else:
                print(f'恭喜你猜对了，正确答案就是{num}')
                break

        else:
            print('请输入范围内的数字！！！')
    except ValueError:
        print('请输入数字！！！')
