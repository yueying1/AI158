#  1. 用户输入当前日期是星期几（1-7的数字即可），如果是工作日（1-5），天气好就去谈业务天气不好在公司整
while True:
    dayOfTheWeek = input('请输入当前日期是星期几（1-7的数字即可）：')
    if dayOfTheWeek.isdigit() :
        dayOfTheWeek = int(dayOfTheWeek)
        if 1 <= dayOfTheWeek <= 5 :
            while True:
                weather = input('天气好不好（请输入好或不好）：')
                if weather == '好':
                    print('今天是工作日，天气好，可以谈业务')
                    break
                elif weather == '不好':
                    print('今天是工作日，天气不好，在公司整理资料')
                    break
                else:
                    print('请输入好或不好!')
        if 5 <= dayOfTheWeek <= 7 :
            while True:
                temperature = input('请输入气温：')
                if temperature.isdigit() :
                    temperature = int(temperature)
                    if temperature > 10 :
                        print('今天是周末，气温大于三十度，去游泳')
                        break
                    else:
                        print('今天是周末，气温低于三十度，去爬山')
                        break
                else:
                    print('请输入气温数字！')
        break
    else:
        print('请输入1-7的数字')



#   2. 判断三角形类型。要求：输入三角形的三条边长度，判断是等边三角形、等腰三角形还是一般三角形
while True:
    sideLength = input('请输入三角形的三条边长（用’，‘隔开）：')
    sideLengthList = sideLength.split(',')
    for i in range(3):
        sideLengthList[i] = int(sideLengthList[i])
    if len(sideLengthList) == 3:
        if sideLengthList[0] + sideLengthList[1] > sideLengthList[2] and sideLengthList[0] + sideLengthList[2] > sideLengthList[1] and sideLengthList[1] + sideLengthList[2] > sideLengthList[0] :
            if sideLengthList[0] == sideLengthList[1] or sideLengthList[0] == sideLengthList[2] or sideLengthList[1] == \
                    sideLengthList[2]:
                print('这是等腰三角形')
            elif sideLengthList[0] == sideLengthList[1] == sideLengthList[2]:
                print('这是等边三角形')
            else:
                print('这是一般三角形')
        else:
            print('这不是三角形')
        break
    else:
        print('请输入三个数字！')



#3. 判断用户输入的一个字符的字符串。
#    要求：用户输入一个字符，判断该字符是大写字母、小写字母、数字还是其他字符。分别输出对应的结果。
strInput = input('请输入一个字符：')
if strInput.isupper() :
    print('大写字母')
elif strInput.islower():
    print('小写字母')
elif strInput.isdigit():
    print('数字')
else:
    print('其他字符')

#4. 要求输入一个0-100之间的分数。根据分数给出相应的等级优,良,中,及格,不及格。
score = input('请输入分数（0-100分）：')
score = int(score)
if 0 <= score <= 100 :
    if 90 <= score <= 100 :
        print('优')
    elif 80 <= score <= 90:
        print('良')
    elif 70 <= score <= 80:
        print('中')
    elif 60 <= score <= 70:
        print('及格')
    else:
        print('不及格')
else:
    print('请输入0-100之内的分数！')



#5. 打印1~100之间3的倍数的和
sun1 = 0
for i in range(101):
    if i % 3 == 0 :
        sun1 += i
print(sun1)

#6. 使用一个循环分别计算1~100奇数的和,偶数和(分别用while 和 for实现)
sumOfOddNumbers = sumOfEvenNumbers =  n = 0
while n <100:
    n += 1
    if n % 2 == 0:           #  偶数
        sumOfEvenNumbers += n
    else:
        sumOfOddNumbers += n
print(f'偶数和为{sumOfEvenNumbers},奇数和为{sumOfOddNumbers}')


