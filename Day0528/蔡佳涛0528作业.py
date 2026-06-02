import csv, random, os
import tools
#  数据存储  字典  {名字：[密码，卡号]}
CSV_PATH = os.path.join(os.path.dirname(__file__), 'project1.csv')

UserDict = {}
cardNumbers = []
currentUser = []
# 读取
def reader():
    with open(CSV_PATH,'r',encoding='utf-8',newline='',) as file:
        fileCsv = csv.reader(file)
        next(fileCsv)
        for line in fileCsv:
            name, password, cardNumber = line[0], line[1], line[2]
            UserDict[name] = [password, cardNumber]
            cardNumbers.append(cardNumber)
# 写入
def writer():
    with open(CSV_PATH, 'w', encoding='utf-8', newline='', ) as file:
        fileCsv = csv.writer(file)
        fileCsv.writerow(['用户名','密码','会员卡号'])
        for item in UserDict.items() :
            fileCsv.writerow([item[0],item[1][0],item[1][1]])

flag = True
# 注册
def register():
    print('****注册****')
    while True:
        registerName = input('注册名：')
        registerPassword = input('密 码：')
        if not registerName == '' or registerPassword == '' :
            if registerName not in UserDict:
                while True:
                    registerCardNumber = random.randint(1000, 9999)
                    if registerCardNumber not in cardNumbers:
                        break
                    else:
                        continue
                UserDict[registerName] = [registerPassword, registerCardNumber]
                writer()
                print('注册成功！请牢记您的会员卡号')
                print(f'会员名 {registerName}  密码 {registerPassword}  会员卡号  {registerCardNumber}')
                break
            else:
                print('该会员名已存在')
        else:
            print(f'用户名及密码不能为空')

# 登录
def login():
    print('*****登录****')
    loginName = input('请输入会员名：')
    loginPassword = input('请输入密码：')
    if loginName in UserDict :
        if loginPassword == UserDict[loginName][0] :
            # 用户名密码正确
            global currentUser
            currentUser = [loginName,UserDict[loginName]]
            print(f'登录成功，欢迎您{loginName}')
        else:
            print('用户名、密码不正确')
    else:
        print('用户名、密码不正确')

def guess():
    print('****抽奖****')
    if not currentUser == '' :
        print(f'{currentUser[0]} 您的卡号为： {currentUser[1][1]}')
        winningNumber = random.randint(0, 9)
        userNumber = int(currentUser[1][1]) % 10
        if userNumber == winningNumber :
            print(f'恭喜您中奖了')
        else:
            print(f'很遗憾，您没中奖，本次中奖的各位数字为：{winningNumber}')
    else:
        print('请先登录再来抽奖')



while True:
    if flag :
        reader()
        flag = False
    print(UserDict)
    msgMainMenu = '''----------奖客富翁系统----------
请选择你的操作：1.注册  2.登录  3.抽奖  0.退出 ：'''
    keyMainMenu = tools.isNum(msgMainMenu, 0, 3)
    if keyMainMenu == 0 :
        currentUser = []
        writer()
        break
    elif keyMainMenu == 1:
        register()
    elif keyMainMenu == 2:
        login()
    else:
        guess()