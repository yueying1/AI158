names = ['张三','张三','李四','张三','王五','张三',]
# for i in names :
#     if i == '张三' :
#         names.remove(i)
# print(names)

    # ind = names.index('zhao')

try:
    ind = names.index('zhao')
except ValueError:
    print('没有这个元素')