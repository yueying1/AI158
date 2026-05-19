# print("Hello World")
# import random

# a = b = c = 1
# print(id(a))
# print(id(b))
# print(id(c))

# n = random.randint(1,10)
# print(n)

# 定义循环变量
n = 9
# 编写循环代码
# while n <= 10:
#     # 循环体打印数字
#     print(n , end=', ')
#     # 循环变量改变
#     n += 1
# else:
#     print(f'{n} 不在1～10之间')


# hobby = ["健身","看书","读报",18]
# print(hobby)

# name = "里四"
# info = {id : '1001', name : '张三', 'age' : 18}
# print(info)
# print(str(info))
# a = info.get(id)
# print(id)
# print(a)


#
# info = {'id' : '1003', 'name' : '张三', 'age' : 18}
# info1 = { 'id' : '1001', 'name' : '李四', 'infos' : info}
# print(info1)
# print(info)
# print(info1.get('infos'))
# print(info1.get('infos').get('id'))
# print(type('name'))

# print(10 / 3)

# names = ["张三", "里斯", "王五"]
# if(names and 1):
#     print("True")


Tom = {'name' : 'Tom', 'age' : 18}
Jarry =  {'name' : 'Jarry'}
admin = {'role' : 'admin'}
arrs = [Tom, Jarry, admin]
for i in arrs:
    match i :
        case {'name' : name, 'age' : age}:
            print(name,age)
        case {'name' : name}:
            print(name)
        case _:
            print("ERROR")

