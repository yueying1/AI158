def factorial(n) :
    if n < 2 :
        return 1
    else:
        return n * factorial(n - 1)

sum1 = 0
for i in range(1, 11):
    sum1 += factorial(2 * i - 1)


print(sum1)