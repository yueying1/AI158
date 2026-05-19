#     11.
l1 = []
n = 1
while True:
    num = int(input(f'请输入第{n}个数(输入-1结束)：'))
    if num == -1 :
        break
    else:
        l1.append(num)
        n += 1

min1 = max1 = l1[0]
for i in l1 :
    if min1 > i :
        min1 = i
    if max1 < i :
        max1 = i

print(f'最大的数为{max1},最小的数为{min1}')



#   12.
i = 0
num = 1
while i < 9:
    num = (num + 1) * 2
    i += 1

print(f'小猴子共摘来了{num}只桃')