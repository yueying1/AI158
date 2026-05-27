#1. 随机生成50个1-50之间的数，统计每个数出现的次数
import random

list1 = []
dict1 = {}
for i in range(50):
    list1.append(random.randint(1,50))
print(list1)
for i in list1:
    if i in dict1 :
        dict1[i] += 1
    else:
        dict1[i] = 1
list1 = sorted(dict1.items())
print(dict(list1))


#2. 排序字符串中的内容如'100,23,5007,5447'排序后'23,100,5007,5447'
# s = '100,23,5007,5447'
isDigit = True
list2 = []
while isDigit:
    s = input('请输入要排序的字符串(用，隔开)：')
    list2 = s.split(',')
    for i in list2:
        if not i.isdigit():
            isDigit = False
    if not isDigit:
        isDigit = True
        print('输入错误，请重新输入')
    else:
        isDigit = False
list2.sort()
s = ''
for i in list2:
    s = s + i + ','
print(s[:-1])

