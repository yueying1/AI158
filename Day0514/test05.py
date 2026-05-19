ageHong = 12
ageFu = ageHong + 20
for i in range(50):
    if ageFu + i == 2 * (ageHong + i) :
        print(f'{i}年后父亲的年累为他的两倍，父亲的年龄为{ageFu + i}，小红的年龄为{ageHong + i}')
        break