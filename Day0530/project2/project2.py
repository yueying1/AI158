import csv, os


from Day0530.project2.tools import isNum, inputDays
PATH_CSV = os.path.join(os.path.dirname(__file__), 'project2.csv')

cars = {}
def reader():
    with open(PATH_CSV, 'r', encoding='utf-8', newline='') as f:
        fileCsv = csv.reader(f)
        next(fileCsv)
        for line in fileCsv:
            if line[0] in cars :
                cars[line[0]].append([line[1], line[2]])
            else:
                cars[line[0]] = [[line[1], line[2]]]


def writer():
    with open(PATH_CSV, 'w', encoding='utf-8', newline='') as f :
        fileCsv = csv.writer(f)
        fileCsv.writerow(['车型,具体信息,日租金'])
        for item in cars.items():
            print(item[0],item[1])
            for i in item[1]:
                # print(f'{item[0]},{i[0]},{i[1]}')
                fileCsv.writerow([item[0],i[0],i[1]])


def sedan():
    print('='*20)
    print('编号\t\t具体信息\t\t\t\t\t日租金')
    indexSedan = 1
    for car in cars['轿车']:
        print(f'{indexSedan:<7}{car[0]:23}{car[1]}')
        indexSedan += 1
    indexSedan = isNum('请选择车型编号：', 1 , indexSedan - 1) - 1
    currentCar = cars['轿车'][indexSedan]
    days = inputDays('请输入租车天数：')
    money = days * int(currentCar[1])
    if 7 < days <= 30 :
        money *= 0.9
    elif 30 < days <= 150:
        money *= 0.8
    else:
        money *= 0.7
    print(f'您租的车时{currentCar[0]}，天数是{days}，总租金为{money}元')

def bus():
    print('=' * 20)
    print('编号\t\t具体信息\t\t\t\t\t日租金')
    indexSedan = 1
    for car in cars['客车']:
        print(f'{indexSedan:<8}{car[0]:23}{car[1]}')
        indexSedan += 1
    indexSedan = isNum('请选择车型编号：', 1, indexSedan - 1) - 1
    currentCar = cars['客车'][indexSedan]
    days = inputDays('请输入租车天数：')
    money = days * int(currentCar[1])
    if days < 3:
        money *= 0.9
    elif 7 < days <= 30:
        money *= 0.8
    elif 30 < days <= 150:
        money *= 0.7
    else:
        money *= 0.6
    print(f'您租的车时{currentCar[0]}，天数是{days}，总租金为{money}元')
reader()
# print(cars)
msg = '0.退出\n1.轿车\n2.客车\n请选择：'
while True:
    print('=' * 20)
    key = isNum(msg,0,2)
    if key == 1 :
        sedan()
    elif key == 2:
        bus()
    else:
        print('退出系统')
        break