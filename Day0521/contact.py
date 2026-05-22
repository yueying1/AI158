names = ['张三','张三']
phones = ['13112341234','12212341234']
msg = '''1.添加联系人
2.查看联系人
3.修改联系人
4.删除联系人
0.推出程序
请选择：'''
while True:
    #  输入选择
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

    #  判断进入那个功能模块
    if key == 0 :
        print('欢迎下次光临！！')
        break
    #  添加联系人
    elif key == 1:
        print('='*20)
        print('1.添加联系人')
        name = input('请输入联系人姓名：')
        phone = input('请输入联系人电话：')
        names.append(name)
        phones.append(phone)
        print(f'{name}：{phone}添加成功')
    #   查看联系人
    elif key == 2:
        print('2.查看联系人')
        print('='*20)
        #  选择查看全部还是指定联系人查看
        while True:
            k = input('1.查看全部联系人\n2.查看指定联系人\n请选择：')
            if k.isdigit() :
                k = int(k)
                if 1 <= k <= 2 :
                    break
                else:
                    print('输入有误，请输入（1或2）！')
                pass
            else:
                print('输入有误，请输入（1或2）！')
        #  判断进入那个查找模块
        #   查看全部
        if k == 1 :
            print('=========联系人=========')
            print(f'姓名\t\t手机号')
            for i in range(len(names)):
                print(f'{names[i]:7}{phones[i]}')
        #   指定查看
        else:
            print('查看指定联系人')
            name = input('请输入想要查看的联系人的姓名：')
            if name in names :
                print('姓名\t\t手机号')
                print(f'{name:7}{phones[names.index(name)]}')
            else:
                print('查无此人')
    #  修改联系人
    elif key == 3:
        print('3.修改联系人')

        name = input('请输入要修改的联系人的姓名：')
        if name in names :
            # 选择修改姓名/修改手机号/全修改
            while True:
                print('='*20)
                k = input('1.修改姓名\n2.修改手机号\n3.全部修改\n请选择：')
                if k.isdigit() :
                    k = int(k)
                    if 1 <= k <= 3 :
                        break
                    else:
                        print('输入有误，请输入（1-3）')
                else:
                    print('输入有误，请输入（1-3）')

            # 出来选择
            indexName = names.index(name)
            if k == 1 :
                print('='*20)
                modifiedName = input('请输入修改后的姓名：')
                names[indexName] = modifiedName
                print(f'{name}：姓名修改成功')
            elif k == 2:
                print('='*20)
                modifiedPhone = input('请输入修改后的手机号：')
                phones[indexName] = modifiedPhone
                print(f'{modifiedPhone}手机号修改成功')
            else:
                print('='*20)
                modifiedName = input('请输入修改后的姓名：')
                modifiedPhone = input('请输入修改后的手机号：')
                phones[indexName] = modifiedPhone
                names[indexName] = modifiedName
                print(f'{modifiedName}：{modifiedPhone}姓名和手机号修改成功')
        else:
            print('查无此人')
    #  删除联系人
    elif key == 4:
        print('4.删除联系人')
        name = input('请输入要删除的联系人的姓名：')
        if name in names :
            # 查有没有重名
            quantity = names.count(name)
            if quantity == 1:
                # 只有一个，直接删
                indexName = names.index(name)
                names.remove(name)
                phones.pop(indexName)
                print(f'联系人{name}已成功删除')
            else:
                #  有重名
                print('因要删除的联系人姓名重名，下面时重名的联系人')
                print('姓名\t\t手机号')
                sequence = 0
                for i in range(len(names)):
                    if names[i] == name :
                        sequence += 1
                        print(f'{names[i]:7}{phones[i]:16}({sequence})')

                while True:

                    serialNumber = input(f'请输入想要删除的联系人的序号(1-{sequence})：')
                    if serialNumber.isdigit() :
                        serialNumber = int(serialNumber)
                        count = 0
                        if 1 <= serialNumber <= sequence :
                            for i in range(len(names)):
                                if names[i] == name :
                                    count += 1
                                if count == serialNumber :
                                    names.pop(i)
                                    phones.pop(i)
                                    print(f'联系人{name}:{phones[i]}已成功删除')
                                    break
                            break
                        else:
                            print(f'请输入联系人对应的序号(1-{sequence}):')
                    else:
                        print(f'请输入联系人对应的序号(1-{sequence}):')
        else:
            print('查无此人')