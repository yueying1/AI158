l1 = []
for i in range(3,101):
    count = 0
    for j in range(1, i):
        if i % j == 0 :
            count += 1
    if count == 1 :
        l1.append(i)


print(f'3~100之间的素数有{l1}')



