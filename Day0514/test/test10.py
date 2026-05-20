i = 0
l1 = []
min1 = 0
while i < 5:
    l1.append(int(input(f"请输入第{i+1}个数:")))
    i += 1
min1 = l1[0]
for item in l1 :
    if min1 > item :
        min1 = item
print(f'最小的数为{min1}')


