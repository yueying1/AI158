# class Employee:
#     """所有员工发基础类"""
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def displayCount(self):
#         print('Total Employee' + self.empCount)
#
#     def displayEmployee(self):
#         print(f'Name:{self.name},Salary:{self.salary}')
#
# emp1 = Employee('小明', 2000)
# emp2 = Employee('张三', 3000)
# print(Employee.__module__)

# file = open(r"E:\Class\文件\文件\test.txt",'r+')
# # file.write('\n你好啊')
# position = file.tell()
# print(position)
# s = file.read()
# print(s)
# file.close()

#
# file = open(r"E:\Class\文件\文件\test.txt",'a+')
# # file.write('\n你好啊')
# # position = file.tell()
# # print(position
# file.seek(0)
# s = file.readlines()
# print(s)
# file.close()
#
#
# x = 7
# result = eval('x * 3')
# print(type(result))

# dict1 = {'zhangsan': ['123456','1234567'], 'lisi':'12345678'}
# print(dict1['zhangsan'])

# s = list[filter(lambda x: x % 2 == 0, range(10))]
# print(s)


# contactDict = {'张三':['13312341234','122245612345'],'李四':['13312341234','122245612345']}
# for k,v in contactDict.items():
#     for i in range(len(v)):
#         print(f'{x for x}\t\t{v[i]}')

# for k, v in contactDict.items():
#     # 第一个值：键 + 值
#     print(f'{k}\t\t{v[0]}')
#     # 剩下所有值：只打印值，前面缩进
#     for val in v[1:]:
#         print(f'\t\t{val}')
# if True:
#     x = 1
# if x not None :
#     print('1')

# l1 = [(x,y) for xin range(3)]
# cartesian_product = [(x, y) for x in range(3) for y in range(3)]
# print(cartesian_product)  # 输出: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# # [(0,0),(1,1),(2,2),(3,3)]
# [print(f'{v}') for v in cartesian_product if v[1] == v[0]]

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myIter = iter(myclass)
