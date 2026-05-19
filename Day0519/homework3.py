import random
# =======================第一题==========================

data = {'1': 200, '2': 388, '3': 123, '4': 456, '5': 987, '6': 342, '7': 767, '8': 234, '9': 124, '10': 345, '11': 123, '12': 234 }
while True:
    startingMonth = input('请输入开始月份：')
    endingMonth = input('请输入结束月份：')
    if startingMonth in data.keys() and endingMonth in data.keys() :
        sumVisitor = 0
        for month in range(int(startingMonth), int(endingMonth) + 1):
            sumVisitor = sumVisitor + data[str(month)]
            average = sumVisitor / (int(endingMonth) - int(startingMonth) + 1)
        print(f'{startingMonth}月~{endingMonth}月平均访客量： {average}')
        break
    else:
        print('输入有误，请输入整数月份！')

# =======================第二题==========================
holidayDict = {'firstStage': 1, 'secondStage': 5, 'thirdStage': 7}
while True:
    lengthOfService = input('请输入整年的工龄：')
    if lengthOfService.isdigit() :
        lengthOfService = int(lengthOfService)
        if lengthOfService < 5 :
            holiday = 'firstStage'
        elif 5 <= lengthOfService < 10:
            holiday = 'secondStage'
        else:
            holiday = 'thirdStage'
        print(f'工龄是{lengthOfService}年的员工的年假天数是：{holidayDict[holiday]}')
        break
    else:
        print('输入有误，应该输入数字')

# =======================第三题==========================
while True:
    redBall = []
    for i in range(6):
        while True:
            num = random.randint(1, 33)
            if num not in redBall:
                redBall.append(num)
                break
    blueBall = random.randint(1, 16)
    redBall.sort()
    print(f'红球：{redBall}')
    print(f'篮球：{blueBall}')
    continueYN = input('继续生成吗（Y/N）？')
    if continueYN == 'Y' :
        continue
    else:
        break
