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