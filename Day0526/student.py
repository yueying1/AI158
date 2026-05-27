class Student:
    teacher = '刘梅'
    def __init__(self, name, sex, age, height):
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__height = height

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, newAge):
        self.__age = newAge

    def birth_year(self):
        return 2026 - self.__age

    def getTeacher(self):
        print(self.teacher)

    @staticmethod
    def wenHao():
        print('nihao')
    
class Student1(Student):
    def __init__(self, name, sex, age, height, weight):
        super().__init__(name, sex, age, height)
        self.weight = weight

    def birth_year(self):
        return 2025 - self.age

stu2 = Student1('张三', '男', 19, 188, 189)
print(stu2.age)
print(stu2.birth_year())

# class A:
#     def foo1(self,x):
#         if x == 1 :
#             print( '1')
#         elif x == 2:
#             print('2')
#         else:
#             print('不知道')
#
# class B(A):
#     def foo1(self,x):
#         if x == 3 :
#             print('3')
#         else:
#             super().foo1(x)
#
# b1 = B()
# b1.foo1(4)