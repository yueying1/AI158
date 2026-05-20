def solve(n):
    return 2 * n - 1

def summation(j):
    if solve(j) == 1 :
        return 1
    else:
        return solve(j) + summation(j - 1)

num = int(input('输入n：'))
sum1 = 0
for i in range(1, num + 1):
    sum1 += summation(i)

print(sum1)
print(summation(4))

