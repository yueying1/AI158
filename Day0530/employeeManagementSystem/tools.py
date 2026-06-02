def isNum(msg, start, end):
    while True:
        key = input(msg)
        if key.isdigit():
            key = int(key)
            if start <= key <= end :
                break
            else:
                print(f'输入错误，请输入{start}-{end}')
        else:
            print(f'输入错误，请输入{start}-{end}')
    return key

def isNumber(use):
    while True:
        if use == 'add' :
            key = input('请输入员工编号（输入q结束输入）：')
        elif use == 'query':
            key = input('请输入员工编号：')
        elif use == 'modify':
            key = input('请输入新的员工编号：')
        if key.isdigit():
            key = int(key)
            if 1000 <= key <= 9999 :
                break
            else:
                print(f'输入错误，请输入正确的员工编号')
        elif str(key) == 'q':
            break
        else:
            print(f'输入错误，请输入正确的员工编号')
    return str(key)

def isEmpty(name, age, address):
    if name == '' or age == '' or address == '':
        print('员工姓名，年龄和地址都不能为空！')

