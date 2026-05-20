def summation(n) :
    if n == 1 :
        return 1
    else :
        return  n + summation(n - 1)

sum1 = 0
num = int(input('请输入n：'))
for i in range(1, num + 1):
    sum1 += summation(i)

print(sum1)