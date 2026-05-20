i = 1
l1 = []
while i * i < 10000 :
    # 平方减原数是是的倍数
    count = 0
    n = i
    #  判断是几位数
    while n:
        n //= 10
        count += 1
    if (i * i - i) % 10**count == 0 :
        l1.append((i,i * i))
    i += 1

print(f'同构数有：{l1}')