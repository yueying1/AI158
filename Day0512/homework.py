print("Hello world")   # 打印hello world
# 打印 人工只能和数据分析158班
print('人工只能和数据分析158班')

'''
这是
多行
注释
'''
# python转义字符
# \t 制表符
print('1234abcd')
print('1234\tabcd')
print('12345\tabcd')
print('学号\t姓名')
print('1001\t张三')
print('10011\t张三')
#   \n 换行
print('人工智能\n和数据分析\n158班')
#  \\ 斜杠
print('abc\\tef')
#  \'  \''
print('I\'m zhangsan')
print("I'm zhangsan")
print("他问：\"一会吃什么？\"")
print('他问："一会吃什么？"')

#   变量定义使用
name = '张三'
print(name)

name, age, sex = '张三', 18, '男'
print(name,age,sex)

name1 = name2 = name3 = '张三'
print(name1,name2,name3)

#  可变类型
hobby = ['健身','看书','看美女',18]
print(hobby,id(hobby),type(hobby))
hobby.append('跳舞')
print(hobby,id(hobby),type(hobby))

info = {'id' : '1001', 'name' : '张三', 'age' : 18}
print(info,id(info),type(info))
info['address'] = '北京海淀'
info['age'] = 19
print(info,id(info),type(info))

set1 = {'健身','看书','看美女'}
print(set1,id(set1),type(set1))
set1.add('看帅哥')
print(set1,id(set1),type(set1))
set1 = {5,2,1,3,8,7,6}
set1.add(6)
print(set1,id(set1),type(set1))
set1.add(6)
print(set1,id(set1),type(set1))


#  不可变类型
weight = 98
print(weight,id(weight),type(weight))
weight = 100
print(weight,id(weight),type(weight))
weight2 = 98
print(weight2,id(weight2),type(weight2))
weight3 = 98
print(weight3,id(weight3),type(weight3))

height = 1.80
print(height,id(height),type(height))
height = 1.85
print(height,id(height),type(height))

name = '张三'
print(name,id(name),type(name))
name = '张三三'
print(name,id(name),type(name))

tuple1 = ('春季','夏季','秋季','冬季')
print(tuple1,id(tuple1),type(tuple1))
tuple1 = ('春季','夏季','秋季','冬季','太阳季')
print(tuple1,id(tuple1),type(tuple1))

flag = True
print(flag,id(flag),type(flag))
flag = False
print(flag,id(flag),type(flag))
flag2 = True
print(flag2,id(flag2),type(flag2))


#  赋值运算符

name = '张三'
print(name)

num1 = 5
num2 = 2
num3 = num1 + num2
print(num1,'+',num2,'=',num3)

print(num1,'-',num2,'=',num1 - num2)

print(num1,'*',num2,'=',num1 * num2)

print(num1,'**',num2,'=',num1 ** num2)

print(num1,'/',num2,'=',num1 / num2)

print(num1,'//',num2,'=',num1 // num2)

print(num1,'%',num2,'=',num1 % num2)

#  复合运算符

a = 10
a = a + 5
print(a)
a += 5
print(a)
a -= 5
print(a)
a *= 5
a **= 5
print(a)
a /= 5
print(a)
a //= 5
print(a)
a %= 5
print(a)


#   比较运算符

a, b = 5, 10
print(a > b)
print(a >= 5)
print(a < b)
print(a <= b)
print(a == 5)
print(a != b)


#  逻辑运算符
print(10 > 5 and 5 < 6)
print(10 >5 or 5 > 6)
print(not 10 > 5)
print(not 10 > 5 and 5 > 3 or 10 < 11)


#  成员运算符
names = ['张三','李四','王五']
print('张三' in names)
print('张' in names)
print('张' in '张三')

print('张三' not in names)
print('张' not in '张三')


#  身份运算符
#   is 判断左右两边是否在内存中的同一个地址
name1 = '张三'
name2 = '张三'
print(name1,id(name1))
print(name2,id(name2))
print(name1 is name2)

names1 = ['张三','李四','王五']
names2 = ['张三','李四','王五']
print(names1,id(names1))
print(names2,id(names2))
print(names1 is names2)

names1 = ['张三','李四','王五']
names2 = names1
print(names1,id(names1))
print(names2,id(names2))
print(names1 is names2)
names1.append('赵六')
print(names1,id(names1))
print(names2,id(names2))
print(names1 is names2)

names1 = ['张三','李四','王五']
names2 = ['张三','李四','王五']
print(names1,id(names1))
print(names2,id(names2))
print(names1 is not names2)

names1 = ['张三','李四','王五']
print(names1 and 1)
print(names1 or 1)

names1 = []
print(names1 and 1)
print(names1 or 0)




#   第二遍
print("Hello world")   # 打印hello world
# 打印 人工只能和数据分析158班
print('人工只能和数据分析158班')

'''
这是
多行
注释
'''
# python转义字符
# \t 制表符
print('1234abcd')
print('1234\tabcd')
print('12345\tabcd')
print('学号\t姓名')
print('1001\t张三')
print('10011\t张三')
#   \n 换行
print('人工智能\n和数据分析\n158班')
#  \\ 斜杠
print('abc\\tef')
#  \'  \''
print('I\'m zhangsan')
print("I'm zhangsan")
print("他问：\"一会吃什么？\"")
print('他问："一会吃什么？"')

#   变量定义使用
name = '张三'
print(name)

name, age, sex = '张三', 18, '男'
print(name,age,sex)

name1 = name2 = name3 = '张三'
print(name1,name2,name3)

#  可变类型
hobby = ['健身','看书','看美女',18]
print(hobby,id(hobby),type(hobby))
hobby.append('跳舞')
print(hobby,id(hobby),type(hobby))

info = {'id' : '1001', 'name' : '张三', 'age' : 18}
print(info,id(info),type(info))
info['address'] = '北京海淀'
info['age'] = 19
print(info,id(info),type(info))

set1 = {'健身','看书','看美女'}
print(set1,id(set1),type(set1))
set1.add('看帅哥')
print(set1,id(set1),type(set1))
set1 = {5,2,1,3,8,7,6}
set1.add(6)
print(set1,id(set1),type(set1))
set1.add(6)
print(set1,id(set1),type(set1))


#  不可变类型
weight = 98
print(weight,id(weight),type(weight))
weight = 100
print(weight,id(weight),type(weight))
weight2 = 98
print(weight2,id(weight2),type(weight2))
weight3 = 98
print(weight3,id(weight3),type(weight3))

height = 1.80
print(height,id(height),type(height))
height = 1.85
print(height,id(height),type(height))

name = '张三'
print(name,id(name),type(name))
name = '张三三'
print(name,id(name),type(name))

tuple1 = ('春季','夏季','秋季','冬季')
print(tuple1,id(tuple1),type(tuple1))
tuple1 = ('春季','夏季','秋季','冬季','太阳季')
print(tuple1,id(tuple1),type(tuple1))

flag = True
print(flag,id(flag),type(flag))
flag = False
print(flag,id(flag),type(flag))
flag2 = True
print(flag2,id(flag2),type(flag2))


#  赋值运算符

name = '张三'
print(name)

num1 = 5
num2 = 2
num3 = num1 + num2
print(num1,'+',num2,'=',num3)

print(num1,'-',num2,'=',num1 - num2)

print(num1,'*',num2,'=',num1 * num2)

print(num1,'**',num2,'=',num1 ** num2)

print(num1,'/',num2,'=',num1 / num2)

print(num1,'//',num2,'=',num1 // num2)

print(num1,'%',num2,'=',num1 % num2)

#  复合运算符

a = 10
a = a + 5
print(a)
a += 5
print(a)
a -= 5
print(a)
a *= 5
a **= 5
print(a)
a /= 5
print(a)
a //= 5
print(a)
a %= 5
print(a)


#   比较运算符

a, b = 5, 10
print(a > b)
print(a >= 5)
print(a < b)
print(a <= b)
print(a == 5)
print(a != b)


#  逻辑运算符
print(10 > 5 and 5 < 6)
print(10 >5 or 5 > 6)
print(not 10 > 5)
print(not 10 > 5 and 5 > 3 or 10 < 11)


#  成员运算符
names = ['张三','李四','王五']
print('张三' in names)
print('张' in names)
print('张' in '张三')

print('张三' not in names)
print('张' not in '张三')


#  身份运算符
#   is 判断左右两边是否在内存中的同一个地址
name1 = '张三'
name2 = '张三'
print(name1,id(name1))
print(name2,id(name2))
print(name1 is name2)

names1 = ['张三','李四','王五']
names2 = ['张三','李四','王五']
print(names1,id(names1))
print(names2,id(names2))
print(names1 is names2)

names1 = ['张三','李四','王五']
names2 = names1
print(names1,id(names1))
print(names2,id(names2))
print(names1 is names2)
names1.append('赵六')
print(names1,id(names1))
print(names2,id(names2))
print(names1 is names2)

names1 = ['张三','李四','王五']
names2 = ['张三','李四','王五']
print(names1,id(names1))
print(names2,id(names2))
print(names1 is not names2)

names1 = ['张三','李四','王五']
print(names1 and 1)
print(names1 or 1)

names1 = []
print(names1 and 1)
print(names1 or 0)







#   第三遍
print("Hello world")   # 打印hello world
# 打印 人工只能和数据分析158班
print('人工只能和数据分析158班')

'''
这是
多行
注释
'''
# python转义字符
# \t 制表符
print('1234abcd')
print('1234\tabcd')
print('12345\tabcd')
print('学号\t姓名')
print('1001\t张三')
print('10011\t张三')
#   \n 换行
print('人工智能\n和数据分析\n158班')
#  \\ 斜杠
print('abc\\tef')
#  \'  \''
print('I\'m zhangsan')
print("I'm zhangsan")
print("他问：\"一会吃什么？\"")
print('他问："一会吃什么？"')

#   变量定义使用
name = '张三'
print(name)

name, age, sex = '张三', 18, '男'
print(name,age,sex)

name1 = name2 = name3 = '张三'
print(name1,name2,name3)

#  可变类型
hobby = ['健身','看书','看美女',18]
print(hobby,id(hobby),type(hobby))
hobby.append('跳舞')
print(hobby,id(hobby),type(hobby))

info = {'id' : '1001', 'name' : '张三', 'age' : 18}
print(info,id(info),type(info))
info['address'] = '北京海淀'
info['age'] = 19
print(info,id(info),type(info))

set1 = {'健身','看书','看美女'}
print(set1,id(set1),type(set1))
set1.add('看帅哥')
print(set1,id(set1),type(set1))
set1 = {5,2,1,3,8,7,6}
set1.add(6)
print(set1,id(set1),type(set1))
set1.add(6)
print(set1,id(set1),type(set1))


#  不可变类型
weight = 98
print(weight,id(weight),type(weight))
weight = 100
print(weight,id(weight),type(weight))
weight2 = 98
print(weight2,id(weight2),type(weight2))
weight3 = 98
print(weight3,id(weight3),type(weight3))

height = 1.80
print(height,id(height),type(height))
height = 1.85
print(height,id(height),type(height))

name = '张三'
print(name,id(name),type(name))
name = '张三三'
print(name,id(name),type(name))

tuple1 = ('春季','夏季','秋季','冬季')
print(tuple1,id(tuple1),type(tuple1))
tuple1 = ('春季','夏季','秋季','冬季','太阳季')
print(tuple1,id(tuple1),type(tuple1))

flag = True
print(flag,id(flag),type(flag))
flag = False
print(flag,id(flag),type(flag))
flag2 = True
print(flag2,id(flag2),type(flag2))


#  赋值运算符

name = '张三'
print(name)

num1 = 5
num2 = 2
num3 = num1 + num2
print(num1,'+',num2,'=',num3)

print(num1,'-',num2,'=',num1 - num2)

print(num1,'*',num2,'=',num1 * num2)

print(num1,'**',num2,'=',num1 ** num2)

print(num1,'/',num2,'=',num1 / num2)

print(num1,'//',num2,'=',num1 // num2)

print(num1,'%',num2,'=',num1 % num2)

#  复合运算符

a = 10
a = a + 5
print(a)
a += 5
print(a)
a -= 5
print(a)
a *= 5
a **= 5
print(a)
a /= 5
print(a)
a //= 5
print(a)
a %= 5
print(a)


#   比较运算符

a, b = 5, 10
print(a > b)
print(a >= 5)
print(a < b)
print(a <= b)
print(a == 5)
print(a != b)


#  逻辑运算符
print(10 > 5 and 5 < 6)
print(10 >5 or 5 > 6)
print(not 10 > 5)
print(not 10 > 5 and 5 > 3 or 10 < 11)


#  成员运算符
names = ['张三','李四','王五']
print('张三' in names)
print('张' in names)
print('张' in '张三')

print('张三' not in names)
print('张' not in '张三')


#  身份运算符
#   is 判断左右两边是否在内存中的同一个地址
name1 = '张三'
name2 = '张三'
print(name1,id(name1))
print(name2,id(name2))
print(name1 is name2)

names1 = ['张三','李四','王五']
names2 = ['张三','李四','王五']
print(names1,id(names1))
print(names2,id(names2))
print(names1 is names2)

names1 = ['张三','李四','王五']
names2 = names1
print(names1,id(names1))
print(names2,id(names2))
print(names1 is names2)
names1.append('赵六')
print(names1,id(names1))
print(names2,id(names2))
print(names1 is names2)

names1 = ['张三','李四','王五']
names2 = ['张三','李四','王五']
print(names1,id(names1))
print(names2,id(names2))
print(names1 is not names2)

names1 = ['张三','李四','王五']
print(names1 and 1)
print(names1 or 1)

names1 = []
print(names1 and 1)
print(names1 or 0)