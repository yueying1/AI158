# 导入random模块，用于生成随机数
import random
# =======================第一题==========================
# 题目：输入起止月份，计算该时间段内每月的平均访客量

# 存储1~12月各月的访客量数据
data = {'1': 200, '2': 388, '3': 123, '4': 456, '5': 987, '6': 342, '7': 767, '8': 234, '9': 124, '10': 345, '11': 123, '12': 234 }
# 循环直到输入合法的起止月份
while True:
    # 获取用户输入的起止月份
    startingMonth = input('请输入开始月份：')
    endingMonth = input('请输入结束月份：')
    # 判断输入的月份是否存在于data的键中
    if startingMonth in data.keys() and endingMonth in data.keys() :
        # 累计起止月份之间的访客量总和
        sumVisitor = 0
        for month in range(int(startingMonth), int(endingMonth) + 1):
            sumVisitor = sumVisitor + data[str(month)]
            # 计算平均访客量 = 总访客量 / 月份数
            average = sumVisitor / (int(endingMonth) - int(startingMonth) + 1)
        # 输出平均访客量
        print(f'{startingMonth}月~{endingMonth}月平均访客量： {average}')
        break
    else:
        # 输入不合法时提示重新输入
        print('输入有误，请输入整数月份！')

# =======================第二题==========================
# 题目：根据员工的工龄，确定其年假天数
# 工龄<5年：1天(firstStage)，5≤工龄<10年：5天(secondStage)，工龄≥10年：7天(thirdStage)

# 不同工龄阶段对应的年假天数
holidayDict = {'firstStage': 1, 'secondStage': 5, 'thirdStage': 7}
# 循环直到输入合法的工龄
while True:
    # 获取用户输入的工龄
    lengthOfService = input('请输入整年的工龄：')
    # 判断输入是否为数字
    if lengthOfService.isdigit() :
        # 将输入转换为整数
        lengthOfService = int(lengthOfService)
        # 根据工龄区间确定年假级别
        if lengthOfService < 5 :
            holiday = 'firstStage'
        elif 5 <= lengthOfService < 10:
            holiday = 'secondStage'
        else:
            holiday = 'thirdStage'
        # 输出对应的年假天数
        print(f'工龄是{lengthOfService}年的员工的年假天数是：{holidayDict[holiday]}')
        break
    else:
        # 输入不合法时提示重新输入
        print('输入有误，应该输入数字')

# =======================第三题==========================
# 题目：模拟双色球彩票选号（6个红球1-33不重复 + 1个蓝球1-16），支持重复生成

# 循环生成彩票号码，用户可决定是否继续
while True:
    # 存放红球号码的列表
    redBall = []
    # 随机生成6个不重复的红球号码（范围1~33）
    for i in range(6):
        while True:
            # 生成1~33之间的随机整数
            num = random.randint(1, 33)
            # 如果号码不重复，则加入红球列表
            if num not in redBall:
                redBall.append(num)
                break
    # 随机生成1个蓝球号码（范围1~16）
    blueBall = random.randint(1, 16)
    # 对红球号码进行升序排序
    redBall.sort()
    # 输出生成的彩票号码
    print(f'红球：{redBall}')
    print(f'篮球：{blueBall}')
    # 询问用户是否继续生成
    continueYN = input('继续生成吗（Y/N）？')
    if continueYN == 'Y' :
        # 输入Y则继续循环，生成下一组号码
        continue
    else:
        # 输入其他则结束循环
        break
