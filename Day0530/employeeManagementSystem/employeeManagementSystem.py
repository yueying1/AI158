import csv
import os.path


from Day0530.employeeManagementSystem.tools import isNum, isNumber, isEmpty

PATH_CSV = os.path.join(os.path.dirname(__file__), 'employee.csv')

employeeDirt = {}
names = {}
def reader():
    with open(PATH_CSV, 'r', encoding='utf-8', newline='') as f:
        file = csv.reader(f)
        next(file)
        for line in file:
            employeeDirt[line[0]] = [line[1], line[2], line[3]]
            names[line[0]] = line[1]

def writer():
    with open(PATH_CSV, 'w', encoding='utf-8', newline='') as f:
        file = csv.writer(f)
        file.writerow(['员工编号','员工姓名','年龄','地址'])
        for item in employeeDirt.items():
            # print(item)
            file.writerow([item[0], item[1][0], item[1][1], item[1][2]])

def addEmployee():
    print('='*20)
    print('添加新员工')
    while True:
        addNumber = isNumber('add')
        if not addNumber == 'q' :
            addName = input('请输入员工姓名：')
            addAge = input('请输入员工年龄：')
            addAddress = input('请输入员工地址：')
            isEmpty(addName, addAge, addAddress)
            if addNumber not in employeeDirt:
                employeeDirt[addNumber] =[addName, addAge, addAddress]
                names[addNumber] = addName
                print(f'已成功添加员工{addName}，员工编号{addNumber}')
            else:
                print('该编号员工已在系统中！')
        else:
            break


def queryEmployee():
    msg = '1.根据员工编号查询\n2.根据员工姓名查询\n3.查询全部\n请选择：'
    print('='*20)
    print('查询员工信息')
    queryKey = isNum(msg, 1, 3)
    if queryKey == 1 :
        queryNumber = isNumber('query')
        if queryNumber in employeeDirt :
            print(f'员工编号：{queryNumber}  员工姓名：{employeeDirt[queryNumber][0]}  员工年龄：{employeeDirt[queryNumber][1]}  员工地址：{employeeDirt[queryNumber][2]}')
        else:
            print('系统中没有此员工的信息！')
    # 根据名字查询
    elif queryKey == 2:
        queryName = input('请输入想要查找的员工姓名：')
        if queryName in names.values() :
            print('员工编号\t\t员工姓名\t\t员工年龄\t\t员工地址')
            for item in names.items():
                if item[1] == queryName :
                    print(f'{item[0]}\t\t{employeeDirt[item[0]][0]}\t\t\t{employeeDirt[item[0]][1]}\t\t\t{employeeDirt[item[0]][2]}')
        else:
            print('系统中没有此员工的信息！')
    else:
        print('员工编号\t\t员工姓名\t\t员工年龄\t\t员工地址')
        for item in employeeDirt.items():
            print(f'{item[0]}\t\t{item[1][0]}\t\t\t{item[1][1]}\t\t\t{item[1][2]}')
    pass
def modifyEmployees():
    msg = '1.根据员工编号修改\n2.根据员工姓名修改\n请选择：'
    msg1 = '1.修改员工编号\n2.修改员工姓名\n3.修改员工年龄\n4.修改员工地址\n0.结束修改\n请选择：'
    print('=' * 20)
    print('修改员工信息')
    modifyKey = isNum(msg, 0, 2)
    if modifyKey == 1 :
        print('='*20)
        modifyNumber = isNumber('query')
        if modifyNumber in employeeDirt :
            while True:
                # print(f'员工编号：{modifyNumber}  员工姓名：{employeeDirt[modifyNumber][0]}  员工年龄：{employeeDirt[modifyNumber][1]}  员工地址：{employeeDirt[modifyNumber][2]}')
                modify1Key = isNum(msg1, 0, 4)
                if modify1Key == 1 :
                    modifyNewNumber = isNumber('modify')
                    if modifyNewNumber in employeeDirt :
                        print('已存在此编号员工！！！！')
                    else:
                        employeeDirt[modifyNewNumber] = employeeDirt[modifyNumber]
                        del employeeDirt[modifyNumber]
                elif modify1Key == 2:
                    modifyNewName = input('请输入修改后的员工姓名：')
                    if not modifyNewName == '' :
                        employeeDirt[modifyNumber][0] = modifyNewName
                        print(f'员工姓名已成功修改为{modifyNewName}')
                    else:
                        print('员工姓名不能为空')
                elif modify1Key == 3:
                    while True:
                        modifyNewAge = input('请输入修改后的员工年龄：')
                        if modifyNewAge.isdigit() :
                            modifyNewAge = int(modifyNewAge)
                            if 18 <= modifyNewAge <= 65 :
                                modifyNewAge = str(modifyNewAge)
                                break
                            else:
                                print('请输入正确的员工年龄')
                        else:
                            print('请输入正确的员工年龄')
                    employeeDirt[modifyNumber][1] = modifyNewAge
                elif modify1Key == 4:
                    modifyNewAddress = input('请输入修改后的员工地址：')
                    if not modifyNewAddress == '' :
                        employeeDirt[modifyNumber][2] = modifyNewAddress
                    else:
                        print('员工地址不能为空！')

                else:
                    print(f'结束对编号{modifyNumber}员工的修改')
                    writer()
                    reader()
                    break
        else:
            print('系统中没有此员工的信息！')
    # 根据名字修改
    else:
        queryName = input('请输入想要查找的员工姓名：')
        if queryName in names.values():
            indexQueryName = 0
            print('序号\t\t员工编号\t\t员工姓名\t\t员工年龄\t\t员工地址')
            for item in names.items():
                if item[1] == queryName:
                    indexQueryName += 1
                    print(f'{indexQueryName}\t\t{item[0]}\t\t{employeeDirt[item[0]][0]}\t\t\t{employeeDirt[item[0]][1]}\t\t\t{employeeDirt[item[0]][2]}')
            queryNum = isNum('请输入想要修改的员工的序号：', 1, indexQueryName) - 1
            i = 0
            for item in employeeDirt.keys():
                if i == queryNum :
                    modifyNumber = item
            while True:
                # print(f'员工编号：{modifyNumber}  员工姓名：{employeeDirt[modifyNumber][0]}  员工年龄：{employeeDirt[modifyNumber][1]}  员工地址：{employeeDirt[modifyNumber][2]}')
                modify1Key = isNum(msg1, 0, 4)
                if modify1Key == 1 :
                    modifyNewNumber = isNumber('modify')
                    if modifyNewNumber in employeeDirt :
                        print('已存在此编号员工！！！！')
                    else:
                        employeeDirt[modifyNewNumber] = employeeDirt[modifyNumber]
                        del employeeDirt[modifyNumber]
                elif modify1Key == 2:
                    modifyNewName = input('请输入修改后的员工姓名：')
                    if not modifyNewName == '' :
                        employeeDirt[modifyNumber][0] = modifyNewName
                        print(f'员工姓名已成功修改为{modifyNewName}')
                    else:
                        print('员工姓名不能为空')
                elif modify1Key == 3:
                    while True:
                        modifyNewAge = input('请输入修改后的员工年龄：')
                        if modifyNewAge.isdigit() :
                            modifyNewAge = int(modifyNewAge)
                            if 18 <= modifyNewAge <= 65 :
                                modifyNewAge = str(modifyNewAge)
                                break
                            else:
                                print('请输入正确的员工年龄')
                        else:
                            print('请输入正确的员工年龄')
                    employeeDirt[modifyNumber][1] = modifyNewAge
                elif modify1Key == 4:
                    modifyNewAddress = input('请输入修改后的员工地址：')
                    if not modifyNewAddress == '' :
                        employeeDirt[modifyNumber][2] = modifyNewAddress
                    else:
                        print('员工地址不能为空！')

                else:
                    print(f'结束对编号{modifyNumber}员工的修改')
                    writer()
                    reader()
                    break
        else:
            print('系统中没有此员工的信息！')
def deleteEmployee():
    msg = '1.根据员工编号删除\n2.根据员工姓名删除\n请选择：'
    print('='*20)
    print('删除员工信息')
    deleteKey = isNum(msg, 1,2)
    if deleteKey == 1 :
        deleteNumber = isNumber('query')
        if deleteNumber in employeeDirt :
            del employeeDirt[deleteNumber]
            writer()
            reader()
            print(f'成功删除编号为{deleteNumber}的员工')

        else:
            print('系统中没有此员工的信息！')
    else:
        queryName = input('请输入想要查找的员工姓名：')
        if queryName in names.values():
            indexQueryName = 0
            print('序号\t\t员工编号\t\t员工姓名\t\t员工年龄\t\t员工地址')
            for item in names.items():
                if item[1] == queryName:
                    indexQueryName += 1
                    print(f'{indexQueryName}\t\t{item[0]}\t\t{employeeDirt[item[0]][0]}\t\t\t{employeeDirt[item[0]][1]}\t\t\t{employeeDirt[item[0]][2]}')
            queryNum = isNum('请输入想要修改的员工的序号：', 1, indexQueryName) - 1
            i = 0
            for item in employeeDirt.keys():
                if i == queryNum:
                    deleteNumber = item
                i += 1
            del employeeDirt[deleteNumber]
            writer()
            reader()
            print(f'成功删除编号为{deleteNumber}的员工')
        else:
            print('系统中没有此员工的信息！')


msg = '''1.添加新员工
2.查询员工信息
3.修改员工信息
4.删除员工信息
0.退出系统
请选择：'''
print('欢迎使用员工管理系统')

reader()
print(names.values())
while True:
    print('=' * 20)
    key = isNum(msg, 0, 4)
    if key == 1 :
        addEmployee()
    elif key == 2:
        queryEmployee()
    elif key == 3:
        modifyEmployees()
    elif key == 4:
        deleteEmployee()
    else:
        print('欢迎下次使用！')
        writer()
        break