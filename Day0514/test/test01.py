def cost (n) :
    print('本次消费总金额：',n)

def cont (n):
    print('消费金额不够，无法换购')
    chose(n)


def chose(n):
    choose = input('请选择：')
    if choose == '1':
        if n >= 50:
            n += 2
            cost(n)
            print('成功换购：百事可乐饮料1瓶')
        else:
            cont(n)
    if choose == '2':
        if n >= 100:
            n += 3
            cost(n)
            print('成功换购：500ml可乐一瓶')
        else:
            cont(n)
    if choose == '3':
        if n >= 100:
            n += 10
            cost(n)
            print('成功换购：5公斤面粉')
        else:
            cont(n)
    if choose == '4':
        if n >= 200:
            n += 10
            cost(n)
            print('成功换购：1个苏波尔炒菜锅')
        else:
            cont(n)
    if choose == '5':
        if n >= 200:
            n += 20
            cost(n)
            print('成功换购：欧莱雅爽肤水一瓶')
        else:
            cont(n)
    if choose == '0':
        cost(n)

money = input('请输入消费金额：')
money = int(money)
print('''
 是否参加优惠换购活动：
 1：满50元，加2元换购百事可乐饮料一瓶
 2：满100元，加3元换购500ml可乐一瓶
 3：满100元，加10元换购5公斤面粉
 4：满200元，加10元可换购1个苏波尔炒菜锅
 5：满200元，加20元可换购欧莱雅爽肤水一瓶
 0：不换购
 ''')

chose(money)
