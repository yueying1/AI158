# 联系人管理系统（数据存储在txt文件中）
import csv
import os

# from Day0521.contact import phones

# txt文件路径（与当前脚本同目录）
TXT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'contact.csv')


def load_contacts():
    """从txt文件读取联系人字典"""
    contacts = {}
    if os.path.exists(TXT_PATH):
        with open(TXT_PATH, 'r', encoding='utf-8',newline='') as file:
            fileCsv = csv.reader(file)
            next(fileCsv)
            for line in fileCsv:
                name = line[0]
                phones = line[1].split(':')
                contacts[name] = phones
            # for line in f:
            #     line = line.strip()
            #     if not line:
            #         continue
            #     # 格式：姓名:手机号1,手机号2,手机号3
            #     name, phones_str = line.split(':', 1)
            #     contacts[name] = phones_str.split(',') if phones_str else []
    return contacts

def save_contacts(contacts):
    """将联系人字典写入txt文件"""
    with open(TXT_PATH, 'w', encoding='utf-8', newline='') as file:
        fileCsv = csv.writer(file)
        fileCsv.writerow(['姓名','手机号'])
        for name, phones in contacts.items():
            fileCsv.writerow([name,':'.join(phones)])

# 添加联系人
def addContact():
    print('=' * 20)
    print('添加联系人')
    name = input('请输入联系人姓名：')
    phone = input('请输入联系人手机号：')
    if name in contactDict:
        contactDict[name].append(phone)
    else:
        contactDict[name] = [phone]
    save_contacts(contactDict)
    print(f'{name}: {phone}添加成功')
# 查看联系人
def viewContact():
    print('=' * 20)
    print('查看联系人')
    while True:
        viewContactKey = input('1.查看全部联系人\n2.查看指定联系人\n请选择：')
        if viewContactKey.isdigit():
            viewContactKey = int(viewContactKey)
            if 1 <= viewContactKey <= 2:
                break
            else:
                print('输入有误，请输入（1或2）！')
        else:
            print('输入有误，请输入（1或2）！')
    # 查看全部联系人
    if viewContactKey == 1:
        print('=========联系人=========')
        # print(contactDict)
        for k, v in contactDict.items():
            print(f'{k}\t\t{v[0]}')
            for val in v[1:]:
                print(f'\t\t{val}')
    # 查看指定联系人
    else:
        print('查看指定联系人')
        name = input('请输入要查找的联系人的姓名：')
        if name in contactDict:
            print('姓名\t\t手机号')
            print(f'{name}\t\t{contactDict[name][0]}')
            for val in contactDict[name][1:]:
                print(f'\t\t{val}')
        else:
            print('没有此人的联系方式！')

# 修改联系人
def modifyContact():
    print('=' * 20)
    print('修改联系人')
    name = input('请输入要修改的联系人的姓名：')
    if name in contactDict:
        while True:
            modifyContactKey = input('1.修改姓名\n2.修改手机号\n3.全部修改\n请选择：')
            if modifyContactKey.isdigit():
                modifyContactKey = int(modifyContactKey)
                if modifyContactKey in range(1, 4):
                    break
                else:
                    print('输入有误，请输入（1-3）')
            else:
                print('输入有误，请输入（1-3）')
        # 修改姓名
        if modifyContactKey == 1:
            print('=' * 20)
            modifyName = input('请输入修改后的姓名：')
            contactDict[modifyName] = contactDict[name]
            del contactDict[name]
            save_contacts(contactDict)
            print(f'{name}姓名成功修改为{modifyName}')
        # 修改手机号
        elif modifyContactKey == 2:
            print('=' * 20)
            if len(contactDict[name]) > 1:
                print('此人有多个手机号')
                for i in range(len(contactDict[name])):
                    print(f'{i + 1}. {contactDict[name][i]}')
                while True:
                    modifyNumber = input('请选择要修改哪一个手机号：')
                    if modifyNumber.isdigit():
                        if int(modifyNumber) in range(1, len(contactDict[name]) + 1):
                            break
                        else:
                            print(f'输入错误，请输入1-{len(contactDict[name])}')
                    else:
                        print(f'输入错误，请输入1-{len(contactDict[name])}')
                newPhone = input('请输入修改后的手机号：')
                oldPhone = contactDict[name][int(modifyNumber) - 1]
                contactDict[name][int(modifyNumber) - 1] = newPhone
                save_contacts(contactDict)
                print(f'{name}的{oldPhone}已成功修改为：{newPhone}')
            else:
                newPhone = input('请输入修改后的手机号：')
                oldPhone = contactDict[name][0]
                contactDict[name] = [newPhone]
                save_contacts(contactDict)
                print(f'{name}的{oldPhone}已成功修改为：{newPhone}')
        # 都修改
        else:
            print('=' * 20)
            modifyName = input('请输入修改后的姓名：')
            modifyPhone = input('请输入修改后的手机号：')
            contactDict[modifyName] = [modifyPhone]
            save_contacts(contactDict)
            print(f'{name}:{contactDict[name]}已成功修改为{modifyName}:{modifyPhone}')
            del contactDict[name]
            save_contacts(contactDict)
    else:
        print(f'没有{name}的联系方式！')

# 删除联系人
def deleteContact():
    print('=' * 20)
    deleteName = input('请输入要删除的联系人：')
    if deleteName in contactDict:
        if len(contactDict[deleteName]) == 1:
            print(f'联系人{deleteName}已成功删除')
            del contactDict[deleteName]
            save_contacts(contactDict)
        else:
            print(f'{deleteName}有多个手机号')
            for i in range(1, len(contactDict[deleteName]) + 1):
                print(f'{i}. {contactDict[deleteName][i - 1]}')
            while True:
                print('=' * 20)
                deleteNumber = input('0.全部删除\n1.删除一个（直接输入需要删除的电话的序号）\n请选择')
                if deleteNumber.isdigit():
                    deleteNumber = int(deleteNumber)
                    if 0 <= deleteNumber <= len(contactDict[deleteName]):
                        break
                    else:
                        print(f'输入错误，请输入0-{len(contactDict[deleteName])}')
                else:
                    print(f'输入错误，请输入0-{len(contactDict[deleteName])}')
            # 全部删除
            if deleteNumber == 0:
                print(f'已删除联系人{deleteName}的全部联系方式')
                del contactDict[deleteName]
                save_contacts(contactDict)
            # 删除指定序号
            else:
                print(f'已删除联系人{deleteName}的{contactDict[deleteName][deleteNumber - 1]}手机号')
                contactDict[deleteName].pop(deleteNumber - 1)
                save_contacts(contactDict)
    else:
        print(f'没有{deleteName}的联系方式')

contactDict = load_contacts()
msg = '''1.添加联系人
2.查看联系人
3.修改联系人
4.删除联系人
0.退出程序
请选择：'''

while True:
    # 输入选择
    while True:
        print('=' * 20)
        key = input(msg)
        if key.isdigit():
            key = int(key)
            if 0 <= key <= 4:
                break
            else:
                print('输入有误，请输入（0-4）！')
        else:
            print('输入有误，请输入（0-4）！')

    # 退出
    if key == 0:
        print('欢迎下次光临！！')
        break
    # 添加联系人
    if key == 1:
        addContact()
    # 查看联系人
    elif key == 2:
        viewContact()
    # 修改联系人
    elif key == 3:
        modifyContact()
    # 删除联系人
    else:
        deleteContact()
