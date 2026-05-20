def reverse(s1):
    newStr = ''
    index = len(s1)
    while index:
        index -= 1
        newStr += s1[index]
    return int(newStr)

num = 95859
while True:
    num += 1
    if num == reverse(str(num)) :
        break

v = (num - 95859) /2
print(f'车速是{v}KM/h，新的对称数为{num}')
