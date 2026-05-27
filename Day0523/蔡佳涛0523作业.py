#  联系人作业
from parso.python.tree import Lambda



# 定义联系人字典
contactDict = {'张三':['13312341234','12212341234','11112341234'], '李四':['21112341234','22212341234'],'王五':['31112341234']}
# contactDict = {'张三':['13312341234'], '李四':['21112341234','22212341234']}

msg = '''1.添加联系人
2.查看联系人
3.修改联系人
4.删除联系人
0.推出程序
请选择：'''
#  输入想要进入的
while True:
    # 输入选择
    while True:
        print('='*20)
        key = input(msg)
        if key.isdigit() :
            key = int(key)
            if 0 <= key <= 4 :
                break
            else:
                print('输入有误，请输入（0-4）！')
        else:
            print('输入有误，请输入（0-4）！')
    # 判断进入那个功能模块
    # 退出
    if key == 0 :
        print('欢迎下次光临！！')
        break

    # 添加联系人
    if key == 1 :
        print('='*20)
        print('添加联系人')
        name = input('请输入联系人姓名：')
        phone = input('请输入联系人手机号：')
        # 判断字典中有没有联系人，没有添加，有就把后面手机号改成列表
        if name in contactDict :
            contactDict[name].append(phone)
        else:
            # 没有直接加
            contactDict[name] = [phone]
        print(f'{name}: {phone}添加成功')

    # 查看联系人
    elif key == 2:
        print('='*20)
        print('查看联系人')
        # 查看全部还是指定查看
        while True:
            viewContactKey = input('1.查看全部联系人\n2.查看指定联系人\n请选择：')
            if viewContactKey.isdigit() :
                viewContactKey = int(viewContactKey)
                if 1 <= viewContactKey <= 2 :
                    break
                else:
                    print('输入有误，请输入（1或2）！')
            else:
                print('输入有误，请输入（1或2）！')
        # 查看全部联系人
        if viewContactKey == 1 :
            print('=========联系人=========')
            print('姓名\t\t手机号')
            # 输出联系人
            for k, v in contactDict.items():
                print(f'{k}\t\t{v[0]}')
                for val in v[1:]:
                     print(f'\t\t{val}')
        # 查看指定联系人
        else:
            print('查看指定联系人')
            name = input('请输入先要查找的联系人的姓名：')
            if name in contactDict :
                print('姓名\t\t手机号')
                print(f'{name}\t\t{contactDict[name][0]}')
                for val in contactDict[name][1:] :
                    print(f'\t\t{val}')
            else:
                print('没有此人的联系方式！')

    # 修改联系人
    elif key == 3:
        print('='*20)
        print('修改联系人')
        name = input('请输入要修改的联系人的姓名：')
        if name in contactDict :
            # 修改姓名\手机号\都改
            while True:
                modifyContactKey = input('1.修改姓名\n2.修改手机号\n3.全部修改:')
                if modifyContactKey.isdigit() :
                    modifyContactKey = int(modifyContactKey)
                    if modifyContactKey in range(1, 4) :
                        break
                    else:
                        print('输入有误，请输入（1-3）')
                else:
                    print('输入有误，请输入（1-3）')
            # 修改姓名
            if modifyContactKey == 1 :
                print('='*20)
                modifyName = input('请输入修改后的姓名：')
                contactDict[modifyName] = contactDict[name]
                del contactDict[name]
                print(f'{name}姓名成功修改为{modifyName}')
            # 修改手机号
            elif modifyContactKey == 2:
                print('='*20)
                # 有多个电话
                if len(contactDict[name]) > 1 :
                    print('此人有多个手机号')
                    for i in range(len(contactDict[name])):
                        print(f'{i + 1}. {contactDict[name][i]}')
                    # 输入要修改的手机好的序号
                    while True:
                        modifyNumber = input('请先择要修改哪一个手机号：')
                        if modifyNumber.isdigit() :
                            if int(modifyNumber) in range(1, len(contactDict[name]) + 1) :
                                break
                            else:
                                print(f'输入错误，请输入1-{len(contactDict[name])}')
                        else:
                            print(f'输入错误，请输入1-{len(contactDict[name])}')
                    newPhone = input('请输入修改后的手机号：')
                    oldPhone = contactDict[name][int(modifyNumber) -1]
                    contactDict[name][int(modifyNumber) -1] = newPhone
                    print(f'{name}的{oldPhone}已成功修改为：{newPhone}')
                # 只有一个电话
                else:
                    newPhone = input('请输入修改后的手机号：')
                    oldPhone = contactDict[name][0]
                    contactDict[name] = [newPhone]
                    print(f'{name}的{oldPhone}已成功修改为：{newPhone}')
            # 都修改
            else:
                print('='*20)
                modifyName = input('请输入修改后的姓名：')
                modifyPhone = input('请输入修改后的手机号：')
                contactDict[modifyName] = [modifyPhone]
                print(f'{name}:{contactDict[name]}已成功修改为{modifyName}:{modifyPhone}')
                del contactDict[name]
        else:
            print(f'没有{name}的联系方式！')

    # 删除联系人
    else:
        print('='*20)
        deleteName = input('请输入要删除的联系人：')
        if deleteName in contactDict :
            # 有一个电话
            if len(contactDict[deleteName]) == 1 :
                print(f'联系人{deleteName}已成功删除')
                del contactDict[deleteName]
            # 有多个电话：全删/删一个
            else:
                # 有多个电话选择删除
                print(f'{deleteName}有多个手机号')
                for i in range(1, len(contactDict[deleteName]) + 1):
                    print(f'{i}. {contactDict[deleteName][i - 1]}')
                # 选择删除方式
                while True:
                    print('='*20)
                    deleteNumber = input('0.全部删除\n1.删除一个（直接输入需要删除的电话的序号）\n请选择')
                    if deleteNumber.isdigit() :
                        deleteNumber = int(deleteNumber)
                        if 0 <= deleteNumber <= len(contactDict[deleteName]) + 1 :
                            break
                        else:
                            print(f'输入错误，请输入0-{len(contactDict[deleteName])}')
                    else:
                        print(f'输入错误，请输入0-{len(contactDict[deleteName])}')
                # 全部删除
                if deleteNumber == 0 :
                    print(f'已删除联系人{deleteName}的全部联系方式')
                    del contactDict[str(deleteName)]
                # 删除序号
                else:
                    print(f'已删除联系人{deleteName}的{contactDict[deleteName][deleteNumber - 1]}手机号')
                    contactDict[deleteName].pop(deleteNumber - 1)
        else:
            print(f'没有{deleteName}的联系方式')