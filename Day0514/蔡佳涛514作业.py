#一、
age = 17
print(age,type(age))
age2 = '18'
print(age2,type(age2))
age3 = int(age2)+2
print(age3,type(age3))
print(int('18'))
print(int(age))

print(int(18.8))
print(int('-18'))


a= '3.14'
print(a,type(a))
b = float(a)
print(b,type(b))
a='3'
print(a,type(a))
b = float(a)
print(b,type(b))


a = 3.14
print(str(a),type(str(a)))
a=[1,2,3]
print(str(a),type(str(a)))


# name = input('请输入您的姓名:')
# print(name)
# num1 = int(input('请输入第一个数:'))
# num2 = int(input('请输入第二个数:'))
# print(num1,'+',num2,'=',num1+num2)


print('你好',end=' ')
print('世界')

# print(sep=' ')变量之间的分隔符，默认是空格
# num1 = int(input('请输入第一个数:'))
# num2 = int(input('请输入第二个数:'))
# print(num1,'+',num2,'=',num1+num2,sep='')

import random
random.seed(1)
print(random.randint(1,10))
print(random.uniform(1,2))


# num1 = int(input('请输入一个整数:'))
# if num1%2 == 0:
#     print(num1,'是偶数')
# print('程序结束')

# num1 = int(input('请输入一个整数:'))
# if num1>0:
#     print(num1,'是正数')
# if num1 == 0:
#     print(num1,'是零')
# if num1 < 0:
#     print(num1,'是负数')


# y = int(input('请输入年份：'))
# if y%4==0 and y%100 != 0 or y%400 == 0:
#     print(y,'是闰年')


# score = int(input('请输入您的成绩：'))
# if score>=60:
#     print(score,'及格')
# else:
#     print(score,'不及格')


# num1 = int(input('请输入一个数字：'))
# if num1%2==0:
#     print(num1,'是偶数')
# else:
#     print(num1,'是奇数')


# y = int(input('请输入年份'))
# if y%4==0 and y%100!=0 or y%400==0:
#     print(y,'是闰年')
# else:
#     print(y,'是平年')


# score = int(input('请输入一个成绩'))
# if 100>=score>=90:
#     print(score,'优秀')
# elif 90>score>=80:
#     print(score,'良好')
# elif 80>score>=70:
#     print(score,'中等')
# elif 70>score>=60:
#     print(score,'及格')
# elif 60>score>=0:
#     print(score,'不及格')
# else:
#     print(score,'成绩不合法')


# age = int(input('请输入年龄：'))
# if age>=65:
#     print(age,'老年人')
# elif age>=18:
#     print(age,'成年人')
# elif age>0:
#     print(age,'未成年')
# else:
#     print(age,'年龄不合法')


# m = int(input('请输入一个月份：'))
# if 3<=m<=5:
#     print('春季：','植树节','清明节','劳动节')
# elif 6<=m<=8:
#     print('夏季：','儿童节','端午节','建党节')
# elif 9<=m<=11:
#     print('秋季：','中秋节','国庆节')
# elif 1<=m<=2 or m==12:
#     print('冬季：','春节')
# else:
#     print(m,'月份不合法(1-12)')


# score = int(input('请输入您的成绩：'))
# if 0<=score<=100:
#     pass
#     if score>=90:
#         print(score,'优秀')
#     elif score>=80:
#         print(score,'良好')
#     elif score>=70:
#         print(score,'中等')
#     elif score>=60:
#         print(score,'及格')
#     else:
#         print(score,'不及格')
# else:
#     print('输入有误')



# y= int(input('请输入年份：'))
# m= int(input('请输入月份：'))
# if m==2:
#     if y%4==0 and y%100!=0 or y%400==0:
#         print(y,'年',m,'月有',29,'天')
#     else:
#         print(y,'年',m,'月有',28,'天')
# elif m==4 or m==6 or m==9 or m==11:
#     print(y,'年',m,'月有',30,'天')
# elif 1<=m<=12:
#     print(y,'年',m,'月有',31,'天')
# else:
#     print('月份有误(1-12)')


# vip = input('请输入您的等级：')
# money = int(input('请输入您的消费金额：'))
# if vip=='普通会员':
#     pass
#     if money>=1000:
#         print('您的消费金额为：',money*0.9)
#     else:
#         print('您的消费金额为：',money)
# elif vip=='高级会员':
#     pass
#     if money>=1000:
#         print('您的消费金额为：',money*0.8)
#     else:
#         print('您的消费金额为：',money)
# elif vip=='至尊会员':
#     pass
#     if money>=1000:
#         print('您的消费金额为：',money*0.7)
# else:
#     print('您的消费金额为：',money)


# i = 1
# while i<=10:
#     print(i)
#     i+=1


# i = 1
# while i<=10:
#     print(i)
#     i+=1
# else:
#     print('i不小于10了')


# 5！ = 5*4*3*2*1
# n = i = int(input('请输入一个数：'))
# s = 1
# while i>1:
#     s = s*i
#     i-=1
# print(n,'的阶乘为',s)


# i = 1
# while i<=100:
#     if i%5==0:
#         break
#     print(i)
#     i+=1


# i = 0
# s = 0
# while i < 100:
#     i = i + 1
#     if i%2==0:
#         continue
#     s = s + i
# print(s)


#二、
age = 17
print(age,type(age))
age2 = '18'
print(age2,type(age2))
age3 = int(age2)+2
print(age3,type(age3))
print(int('18'))
print(int(age))

print(int(18.8))
print(int('-18'))


a= '3.14'
print(a,type(a))
b = float(a)
print(b,type(b))
a='3'
print(a,type(a))
b = float(a)
print(b,type(b))


a = 3.14
print(str(a),type(str(a)))
a=[1,2,3]
print(str(a),type(str(a)))


# name = input('请输入您的姓名:')
# print(name)
# num1 = int(input('请输入第一个数:'))
# num2 = int(input('请输入第二个数:'))
# print(num1,'+',num2,'=',num1+num2)


print('你好',end=' ')
print('世界')

# print(sep=' ')变量之间的分隔符，默认是空格
# num1 = int(input('请输入第一个数:'))
# num2 = int(input('请输入第二个数:'))
# print(num1,'+',num2,'=',num1+num2,sep='')

import random
random.seed(1)
print(random.randint(1,10))
print(random.uniform(1,2))


# num1 = int(input('请输入一个整数:'))
# if num1%2 == 0:
#     print(num1,'是偶数')
# print('程序结束')

# num1 = int(input('请输入一个整数:'))
# if num1>0:
#     print(num1,'是正数')
# if num1 == 0:
#     print(num1,'是零')
# if num1 < 0:
#     print(num1,'是负数')


# y = int(input('请输入年份：'))
# if y%4==0 and y%100 != 0 or y%400 == 0:
#     print(y,'是闰年')


# score = int(input('请输入您的成绩：'))
# if score>=60:
#     print(score,'及格')
# else:
#     print(score,'不及格')


# num1 = int(input('请输入一个数字：'))
# if num1%2==0:
#     print(num1,'是偶数')
# else:
#     print(num1,'是奇数')


# y = int(input('请输入年份'))
# if y%4==0 and y%100!=0 or y%400==0:
#     print(y,'是闰年')
# else:
#     print(y,'是平年')


# score = int(input('请输入一个成绩'))
# if 100>=score>=90:
#     print(score,'优秀')
# elif 90>score>=80:
#     print(score,'良好')
# elif 80>score>=70:
#     print(score,'中等')
# elif 70>score>=60:
#     print(score,'及格')
# elif 60>score>=0:
#     print(score,'不及格')
# else:
#     print(score,'成绩不合法')


# age = int(input('请输入年龄：'))
# if age>=65:
#     print(age,'老年人')
# elif age>=18:
#     print(age,'成年人')
# elif age>0:
#     print(age,'未成年')
# else:
#     print(age,'年龄不合法')


# m = int(input('请输入一个月份：'))
# if 3<=m<=5:
#     print('春季：','植树节','清明节','劳动节')
# elif 6<=m<=8:
#     print('夏季：','儿童节','端午节','建党节')
# elif 9<=m<=11:
#     print('秋季：','中秋节','国庆节')
# elif 1<=m<=2 or m==12:
#     print('冬季：','春节')
# else:
#     print(m,'月份不合法(1-12)')


# score = int(input('请输入您的成绩：'))
# if 0<=score<=100:
#     pass
#     if score>=90:
#         print(score,'优秀')
#     elif score>=80:
#         print(score,'良好')
#     elif score>=70:
#         print(score,'中等')
#     elif score>=60:
#         print(score,'及格')
#     else:
#         print(score,'不及格')
# else:
#     print('输入有误')



# y= int(input('请输入年份：'))
# m= int(input('请输入月份：'))
# if m==2:
#     if y%4==0 and y%100!=0 or y%400==0:
#         print(y,'年',m,'月有',29,'天')
#     else:
#         print(y,'年',m,'月有',28,'天')
# elif m==4 or m==6 or m==9 or m==11:
#     print(y,'年',m,'月有',30,'天')
# elif 1<=m<=12:
#     print(y,'年',m,'月有',31,'天')
# else:
#     print('月份有误(1-12)')


# vip = input('请输入您的等级：')
# money = int(input('请输入您的消费金额：'))
# if vip=='普通会员':
#     pass
#     if money>=1000:
#         print('您的消费金额为：',money*0.9)
#     else:
#         print('您的消费金额为：',money)
# elif vip=='高级会员':
#     pass
#     if money>=1000:
#         print('您的消费金额为：',money*0.8)
#     else:
#         print('您的消费金额为：',money)
# elif vip=='至尊会员':
#     pass
#     if money>=1000:
#         print('您的消费金额为：',money*0.7)
# else:
#     print('您的消费金额为：',money)


# i = 1
# while i<=10:
#     print(i)
#     i+=1


# i = 1
# while i<=10:
#     print(i)
#     i+=1
# else:
#     print('i不小于10了')


# 5！ = 5*4*3*2*1
# n = i = int(input('请输入一个数：'))
# s = 1
# while i>1:
#     s = s*i
#     i-=1
# print(n,'的阶乘为',s)


# i = 1
# while i<=100:
#     if i%5==0:
#         break
#     print(i)
#     i+=1


# i = 0
# s = 0
# while i < 100:
#     i = i + 1
#     if i%2==0:
#         continue
#     s = s + i
# print(s)



#三、
age = 17
print(age,type(age))
age2 = '18'
print(age2,type(age2))
age3 = int(age2)+2
print(age3,type(age3))
print(int('18'))
print(int(age))

print(int(18.8))
print(int('-18'))


a= '3.14'
print(a,type(a))
b = float(a)
print(b,type(b))
a='3'
print(a,type(a))
b = float(a)
print(b,type(b))


a = 3.14
print(str(a),type(str(a)))
a=[1,2,3]
print(str(a),type(str(a)))


# name = input('请输入您的姓名:')
# print(name)
# num1 = int(input('请输入第一个数:'))
# num2 = int(input('请输入第二个数:'))
# print(num1,'+',num2,'=',num1+num2)


print('你好',end=' ')
print('世界')

# print(sep=' ')变量之间的分隔符，默认是空格
# num1 = int(input('请输入第一个数:'))
# num2 = int(input('请输入第二个数:'))
# print(num1,'+',num2,'=',num1+num2,sep='')

import random
random.seed(1)
print(random.randint(1,10))
print(random.uniform(1,2))


# num1 = int(input('请输入一个整数:'))
# if num1%2 == 0:
#     print(num1,'是偶数')
# print('程序结束')

# num1 = int(input('请输入一个整数:'))
# if num1>0:
#     print(num1,'是正数')
# if num1 == 0:
#     print(num1,'是零')
# if num1 < 0:
#     print(num1,'是负数')


# y = int(input('请输入年份：'))
# if y%4==0 and y%100 != 0 or y%400 == 0:
#     print(y,'是闰年')


# score = int(input('请输入您的成绩：'))
# if score>=60:
#     print(score,'及格')
# else:
#     print(score,'不及格')


# num1 = int(input('请输入一个数字：'))
# if num1%2==0:
#     print(num1,'是偶数')
# else:
#     print(num1,'是奇数')


# y = int(input('请输入年份'))
# if y%4==0 and y%100!=0 or y%400==0:
#     print(y,'是闰年')
# else:
#     print(y,'是平年')


# score = int(input('请输入一个成绩'))
# if 100>=score>=90:
#     print(score,'优秀')
# elif 90>score>=80:
#     print(score,'良好')
# elif 80>score>=70:
#     print(score,'中等')
# elif 70>score>=60:
#     print(score,'及格')
# elif 60>score>=0:
#     print(score,'不及格')
# else:
#     print(score,'成绩不合法')


# age = int(input('请输入年龄：'))
# if age>=65:
#     print(age,'老年人')
# elif age>=18:
#     print(age,'成年人')
# elif age>0:
#     print(age,'未成年')
# else:
#     print(age,'年龄不合法')


# m = int(input('请输入一个月份：'))
# if 3<=m<=5:
#     print('春季：','植树节','清明节','劳动节')
# elif 6<=m<=8:
#     print('夏季：','儿童节','端午节','建党节')
# elif 9<=m<=11:
#     print('秋季：','中秋节','国庆节')
# elif 1<=m<=2 or m==12:
#     print('冬季：','春节')
# else:
#     print(m,'月份不合法(1-12)')


# score = int(input('请输入您的成绩：'))
# if 0<=score<=100:
#     pass
#     if score>=90:
#         print(score,'优秀')
#     elif score>=80:
#         print(score,'良好')
#     elif score>=70:
#         print(score,'中等')
#     elif score>=60:
#         print(score,'及格')
#     else:
#         print(score,'不及格')
# else:
#     print('输入有误')



# y= int(input('请输入年份：'))
# m= int(input('请输入月份：'))
# if m==2:
#     if y%4==0 and y%100!=0 or y%400==0:
#         print(y,'年',m,'月有',29,'天')
#     else:
#         print(y,'年',m,'月有',28,'天')
# elif m==4 or m==6 or m==9 or m==11:
#     print(y,'年',m,'月有',30,'天')
# elif 1<=m<=12:
#     print(y,'年',m,'月有',31,'天')
# else:
#     print('月份有误(1-12)')


# vip = input('请输入您的等级：')
# money = int(input('请输入您的消费金额：'))
# if vip=='普通会员':
#     pass
#     if money>=1000:
#         print('您的消费金额为：',money*0.9)
#     else:
#         print('您的消费金额为：',money)
# elif vip=='高级会员':
#     pass
#     if money>=1000:
#         print('您的消费金额为：',money*0.8)
#     else:
#         print('您的消费金额为：',money)
# elif vip=='至尊会员':
#     pass
#     if money>=1000:
#         print('您的消费金额为：',money*0.7)
# else:
#     print('您的消费金额为：',money)


# i = 1
# while i<=10:
#     print(i)
#     i+=1


# i = 1
# while i<=10:
#     print(i)
#     i+=1
# else:
#     print('i不小于10了')


# 5！ = 5*4*3*2*1
# n = i = int(input('请输入一个数：'))
# s = 1
# while i>1:
#     s = s*i
#     i-=1
# print(n,'的阶乘为',s)


# i = 1
# while i<=100:
#     if i%5==0:
#         break
#     print(i)
#     i+=1


# i = 0
# s = 0
# while i < 100:
#     i = i + 1
#     if i%2==0:
#         continue
#     s = s + i
# print(s)