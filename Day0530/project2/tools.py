def isNum(msg, start, end):
    while True:
        key = input(msg)
        if key.isdigit() :
            key = int(key)
            if start <= key <= end :
                break
            else:
                print(f'输入错误，请输入({start}-{end})!!')
        else:
            print(f'输入错误，请输入({start}-{end})!!')
    return key

def inputDays(msg):
    while True:
        key = input(msg)
        if key.isdigit() :
            key = int(key)
            if key > 0 :
                break
            else:
                print('请输入真确的天数！')
        else:
            print('请输入真确的天数！')
    return key