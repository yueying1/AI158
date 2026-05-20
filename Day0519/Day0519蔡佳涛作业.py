# =======================第一题==========================

data = {'1': 200, '2': 388, '3': 123, '4': 456, '5': 987, '6': 342, '7': 767, '8': 234, '9': 124, '10': 345, '11': 123,
        '12': 234}
while True:
    startingMonth = input('请输入开始月份：')
    endingMonth = input('请输入结束月份：')
    if startingMonth in data.keys() and endingMonth in data.keys():
        sumVisitor = 0
        for month in range(int(startingMonth), int(endingMonth) + 1):
            sumVisitor = sumVisitor + data[str(month)]
            average = sumVisitor / (int(endingMonth) - int(startingMonth) + 1)
        print(f'{startingMonth}月~{endingMonth}月平均访客量： {average}')
        break
    else:
        print('输入有误，请输入整数月份！')

# ======================基础===============================

# =======================第一遍=============================
# --- 1. 字符串索引：正数从0开始，负数从-1开始（倒数） ---
name = '张三'
print(name)

s = 'helloworld'
print(s)
print(s[5])           # 第6个字符
print(s[-1])          # 倒数第1个字符
print(s[-5])          # 倒数第5个字符
# 遍历字符串的三种方式
for i in range(0, len(s), 1):   # 方式1：用索引遍历
    print(s[i])
for i in range(len(s)):         # 方式2：省略start和step
    print(s[i])
for i in s:                     # 方式3：直接遍历字符（最简洁）
    print(i)

# --- 2. 字符串切片：[起始:结束:步长]，左闭右开 ---
s = 'helloworld'
print(s)
print(s[0:5:1])     # 索引0~4，步长1 → hello
print(s[1:5:2])     # 索引1,3，步长2 → el
print(s[::])        # 全拷贝
print(s[::2])       # 每隔一个字符取一个
print(s[:])         # 全拷贝
print(s[-10:-1])    # 负索引切片
print(s[-10:])      # 从倒数第10到末尾
print(s[-10:5:1])   # 负正索引混用
print(s[::-1])      # 步长-1 → 字符串反转
print(s[-8:7:1])
print(s[-8:0:-1])

# --- 3. 字符串拼接、重复、成员判断、转义字符 ---
s1 = 'hello'
s2 = 'world'
print(s1 + s2)          # 字符串拼接
print('=' * 50)         # 字符串重复
print('h' in s1)        # 成员判断：是否包含
print('w' not in s2)    # 成员判断：是否不包含
print('abc\tabc')       # \t 是制表符
print('abc\\tabc')      # \\ 表示一个反斜杠字符
print(r'abc\tabc')      # r'' 原始字符串，转义符不生效

# --- 4. 逢7过游戏：含7或7的倍数就说"过" ---
for i in range(1, 101, 1):
    if '7' in str(i) or i % 7 == 0:
        print('过', end=' ')
    else:
        print(i, end=' ')

# --- 5. 字符串格式化的三种方式 ---
name = input('请输入姓名')
age = 18
height = 185
print('你的名字是%s,你的年龄是%d,你的身高是%.2f' % (name, age, height))            # % 格式化
print(f'你的名字是{name}，你的年龄是{age}，你的身高是{height}')                     # f-string
print('你的名字是{}，你的年龄是{}，你的身高是{}'.format(name, age, height))          # format方法
print('你的名字是{0},你的年龄是{1},你的身高是{2},名字是{0}'.format(name, age, height))  # 索引复用

# --- 6. 字符串查找：count计数、startswith/endswith判断、find/index查找 ---
s = 'helloworld'
print(s.count('h'))         # 统计 'h' 出现次数
print(s.count('l'))
print(s.count('l', 5, 1))   # 起始>结束，返回0
print(s.count('l', 5))      # 从索引5开始统计

print(s.startswith('h'))    # 是否以 'h' 开头
print(s.startswith('w', 5)) # 从索引5开始是否以 'w' 开头

print(s.endswith('d'))      # 是否以 'd' 结尾
print(s.endswith('o', 0, 4)) # 索引0~3范围内是否以 'o' 结尾

print(s.find('l'))          # 查找 'l' 首次出现位置，找不到返回-1
print(s.find('l', 5))
print(s.find('z'))          # 找不到返回-1

print(s.index('l'))         # 与find类似，但找不到会抛出异常
print(s.index('l', 5))
# print(s.index('z'))       # 找不到会抛出 ValueError

# --- 7. isdigit判断数字、成绩判断 ---
print('123'.isdigit())      # 判断字符串是否全为数字

score = input('请输入您的成绩:')
if score.isdigit():         # 先校验输入是否合法
    score = int(score)
    if score >= 60:
        print('及格')
    else:
        print('不及格')
else:
    print('输入不合法')

# --- 8. join拼接、len/lower/upper ---
list1 = ['a', 'b', 'c']
print('a_b_c')
print(' '.join(list1))      # 用空格拼接列表 → 'a b c'

print(len(s))               # 字符串长度
print(s.lower())            # 转小写
print(s.upper())            # 转大写

# --- 9. strip系列：去除两端/左侧/右侧的空白字符 ---
str1 = '   abc   '
print(str1, len(str1))
print(str1.lstrip(), len(str1.lstrip()))   # 去左空白
str1 = '   abc   '
print(str1, len(str1))
print(str1.rstrip(), len(str1.rstrip()))   # 去右空白
str1 = '   abc   '
print(str1, len(str1))
print(str1.strip(), len(str1.strip()))     # 去两端空白

# --- 10. max/min：取最大值/最小值（字符串按ASCII比较） ---
print(max('abc'))
print(max([1, 2, 3]))
print(max(['1', '2', '3']))   # 字符串比较按ASCII码
print(min('abc'))
print(min([1, 2, 3]))
print(min(['1', '2', '3']))

# --- 11. replace替换、rindex从右查找 ---
s = '我爱你，你爱他，他爱我'
print('s')
print(s.replace('爱', '不爱'))       # 全部替换
print(s.replace('爱', '不爱', 1))     # 只替换第1个

s = 'helloworld'
print(s.rindex('l'))          # 从右侧查找 'l' 的位置

# --- 12. split分割、swapcase大小写反转 ---
s = 'a b \n c         d'
print(s.split())              # 默认按空白字符分割（空格、换行等）
s = 'a_b_c_d'
print(s.split('_'))           # 按下划线分割

s = 'Helloworld'
print(s.swapcase())           # 大小写反转 → 'hELLOWORLD'


# --- 13. 综合练习：格式化英文歌词（每行首字母大写，独立的 'i' 改为 'I'） ---
s = '''when I Was Young i'd listen to the Radio
         waiting for My Favorite songs
       when They played i'd sing Along
                    it Made me Smile         '''.strip()
print(s)
s2 = ''                       # 存放处理后的歌词
index1 = -1                   # 上一行换行符的位置
while True:
    index2 = s.find('\n', index1 + 1)   # 查找下一个换行符
    if index2 == -1:                    # 没有换行符 → 最后一行
        s2 += s[index1 + 1:].strip().capitalize()
        break
    s2 += s[index1 + 1:index2].strip().capitalize() + '\n'
    index1 = index2
s2 = s2.replace(' i ', ' I ').replace(" i ", " I ")   # 将独立的 'i' 大写
print(s2)


# --- 14. 列表：创建、索引、遍历 ---
names = ['张三', '李四', '王五']
print(names, type(names))     # 打印列表及类型
print(names[0])               # 第一个元素
print(names[-1])              # 最后一个元素

names = ['张三', '李四', '王五']

# 遍历列表的两种方式
for i in range(len(names)):   # 方式1：通过索引遍历
    print(names[i])

for i in names:               # 方式2：直接遍历元素
    print(i)

# 修改列表中的元素
names = ['张三', '李四', '王五', '张三']
print(names)

for i in range(len(names)):
    if names[i] == '张三':
        names[i] = '张三三'   # 将 '张三' 替换为 '张三三'
print(names)

# --- 15. 列表切片、拼接、重复、成员判断 ---
names = ['张三', '李四', '王五', '张三']
print(names[::])
print(names[1:3:1])
print(names[:3:1])

names1 = ['张三', '李四', '王五', '张三']
names2 = ['a', 'b', 'c', 'd']

print(names1 + names2)        # 列表拼接
print(names1 * 2)             # 列表重复
print('张三' in names1)       # 成员判断（整体匹配）
print('张' in names1)         # 不会匹配到子串
print('a' not in names1)

# --- 16. 列表增加元素：append追加、extend扩展、insert插入 ---
names1 = ['张三', '李四', '王五', '张三']
print(names1, id(names1))
names1.append('赵六')         # 在末尾追加一个元素（id不变，原地修改）
print(names1, id(names1))

print(names1.count('张三'))   # 统计 '张三' 出现次数

names2 = ['a', 'b', 'c']
names1.extend(names2)         # 将另一列表的元素逐个追加
print(names1)

print(names.index('张三'))    # 查找 '张三' 首次出现的位置

names1.insert(0, '侯七')      # 在指定位置插入元素
print(names1)
names1.insert(100, '侯七七')  # 索引超出范围时插入到末尾
print(names1)

# --- 17. 列表删除元素：pop弹出、remove移除、clear清空 ---
names1.pop()                  # 默认弹出末尾元素
print(names1)
names1.pop(0)                 # 弹出指定位置的元素
print(names1)

names1.remove('张三')         # 按值删除（只删第一个匹配项）
print(names1)

while '张三' in names1:       # 循环删除所有值为 '张三' 的元素
    names1.remove('张三')
print(names1)

# --- 18. 列表排序与反转：reverse、sort ---
names1.reverse()              # 原地反转列表
print(names1)
print(names1[::-1])           # 切片反转（不改变原列表）

list1 = [5, 3, 4, 2, 1, 8, 7, 6]
print(list1)
list1.sort(reverse=True)      # 降序排序（原地修改）
print(list1)

list2 = [[5, 3], [2, 1], [4, 6]]
print(list2)
list2.sort(key=lambda x: x[1]) # 按每个子列表的第2个元素排序
print(list2)

names1.clear()                # 清空列表
print(names1)

# --- 19. 列表拷贝：直接赋值 vs copy()浅拷贝 ---
names1 = ['a', 'b', 'c']
names2 = names1               # 直接赋值：names2和names1指向同一对象
names3 = names1.copy()        # copy()：创建新对象（浅拷贝）
print(names1, id(names1))
print(names2, id(names2))     # id与names1相同 → 同一对象
print(names3, id(names3))     # id不同 → 独立的新列表
names1.append('d')            # 修改names1
print(names1, id(names1))
print(names2, id(names2))     # names2也跟着变了（同一对象）
print(names3, id(names3))     # names3不受影响（独立对象）

# =======================第二遍=============================
# --- 1. 字符串索引：正数从0开始，负数从-1开始（倒数） ---
name = '张三'
print(name)

s = 'helloworld'
print(s)
print(s[5])           # 第6个字符
print(s[-1])          # 倒数第1个字符
print(s[-5])          # 倒数第5个字符
# 遍历字符串的三种方式
for i in range(0, len(s), 1):   # 方式1：用索引遍历
    print(s[i])
for i in range(len(s)):         # 方式2：省略start和step
    print(s[i])
for i in s:                     # 方式3：直接遍历字符（最简洁）
    print(i)

# --- 2. 字符串切片：[起始:结束:步长]，左闭右开 ---
s = 'helloworld'
print(s)
print(s[0:5:1])     # 索引0~4，步长1 → hello
print(s[1:5:2])     # 索引1,3，步长2 → el
print(s[::])        # 全拷贝
print(s[::2])       # 每隔一个字符取一个
print(s[:])         # 全拷贝
print(s[-10:-1])    # 负索引切片
print(s[-10:])      # 从倒数第10到末尾
print(s[-10:5:1])   # 负正索引混用
print(s[::-1])      # 步长-1 → 字符串反转
print(s[-8:7:1])
print(s[-8:0:-1])

# --- 3. 字符串拼接、重复、成员判断、转义字符 ---
s1 = 'hello'
s2 = 'world'
print(s1 + s2)          # 字符串拼接
print('=' * 50)         # 字符串重复
print('h' in s1)        # 成员判断：是否包含
print('w' not in s2)    # 成员判断：是否不包含
print('abc\tabc')       # \t 是制表符
print('abc\\tabc')      # \\ 表示一个反斜杠字符
print(r'abc\tabc')      # r'' 原始字符串，转义符不生效

# --- 4. 逢7过游戏：含7或7的倍数就说"过" ---
for i in range(1, 101, 1):
    if '7' in str(i) or i % 7 == 0:
        print('过', end=' ')
    else:
        print(i, end=' ')

# --- 5. 字符串格式化的三种方式 ---
name = input('请输入姓名')
age = 18
height = 185
print('你的名字是%s,你的年龄是%d,你的身高是%.2f' % (name, age, height))            # % 格式化
print(f'你的名字是{name}，你的年龄是{age}，你的身高是{height}')                     # f-string
print('你的名字是{}，你的年龄是{}，你的身高是{}'.format(name, age, height))          # format方法
print('你的名字是{0},你的年龄是{1},你的身高是{2},名字是{0}'.format(name, age, height))  # 索引复用

# --- 6. 字符串查找：count计数、startswith/endswith判断、find/index查找 ---
s = 'helloworld'
print(s.count('h'))         # 统计 'h' 出现次数
print(s.count('l'))
print(s.count('l', 5, 1))   # 起始>结束，返回0
print(s.count('l', 5))      # 从索引5开始统计

print(s.startswith('h'))    # 是否以 'h' 开头
print(s.startswith('w', 5)) # 从索引5开始是否以 'w' 开头

print(s.endswith('d'))      # 是否以 'd' 结尾
print(s.endswith('o', 0, 4)) # 索引0~3范围内是否以 'o' 结尾

print(s.find('l'))          # 查找 'l' 首次出现位置，找不到返回-1
print(s.find('l', 5))
print(s.find('z'))          # 找不到返回-1

print(s.index('l'))         # 与find类似，但找不到会抛出异常
print(s.index('l', 5))
# print(s.index('z'))       # 找不到会抛出 ValueError

# --- 7. isdigit判断数字、成绩判断 ---
print('123'.isdigit())      # 判断字符串是否全为数字

score = input('请输入您的成绩:')
if score.isdigit():         # 先校验输入是否合法
    score = int(score)
    if score >= 60:
        print('及格')
    else:
        print('不及格')
else:
    print('输入不合法')

# --- 8. join拼接、len/lower/upper ---
list1 = ['a', 'b', 'c']
print('a_b_c')
print(' '.join(list1))      # 用空格拼接列表 → 'a b c'

print(len(s))               # 字符串长度
print(s.lower())            # 转小写
print(s.upper())            # 转大写

# --- 9. strip系列：去除两端/左侧/右侧的空白字符 ---
str1 = '   abc   '
print(str1, len(str1))
print(str1.lstrip(), len(str1.lstrip()))   # 去左空白
str1 = '   abc   '
print(str1, len(str1))
print(str1.rstrip(), len(str1.rstrip()))   # 去右空白
str1 = '   abc   '
print(str1, len(str1))
print(str1.strip(), len(str1.strip()))     # 去两端空白

# --- 10. max/min：取最大值/最小值（字符串按ASCII比较） ---
print(max('abc'))
print(max([1, 2, 3]))
print(max(['1', '2', '3']))   # 字符串比较按ASCII码
print(min('abc'))
print(min([1, 2, 3]))
print(min(['1', '2', '3']))

# --- 11. replace替换、rindex从右查找 ---
s = '我爱你，你爱他，他爱我'
print('s')
print(s.replace('爱', '不爱'))       # 全部替换
print(s.replace('爱', '不爱', 1))     # 只替换第1个

s = 'helloworld'
print(s.rindex('l'))          # 从右侧查找 'l' 的位置

# --- 12. split分割、swapcase大小写反转 ---
s = 'a b \n c         d'
print(s.split())              # 默认按空白字符分割（空格、换行等）
s = 'a_b_c_d'
print(s.split('_'))           # 按下划线分割

s = 'Helloworld'
print(s.swapcase())           # 大小写反转 → 'hELLOWORLD'


# --- 13. 综合练习：格式化英文歌词（每行首字母大写，独立的 'i' 改为 'I'） ---
s = '''when I Was Young i'd listen to the Radio
         waiting for My Favorite songs
       when They played i'd sing Along
                    it Made me Smile         '''.strip()
print(s)
s2 = ''                       # 存放处理后的歌词
index1 = -1                   # 上一行换行符的位置
while True:
    index2 = s.find('\n', index1 + 1)   # 查找下一个换行符
    if index2 == -1:                    # 没有换行符 → 最后一行
        s2 += s[index1 + 1:].strip().capitalize()
        break
    s2 += s[index1 + 1:index2].strip().capitalize() + '\n'
    index1 = index2
s2 = s2.replace(' i ', ' I ').replace(" i ", " I ")   # 将独立的 'i' 大写
print(s2)


# --- 14. 列表：创建、索引、遍历 ---
names = ['张三', '李四', '王五']
print(names, type(names))     # 打印列表及类型
print(names[0])               # 第一个元素
print(names[-1])              # 最后一个元素

names = ['张三', '李四', '王五']

# 遍历列表的两种方式
for i in range(len(names)):   # 方式1：通过索引遍历
    print(names[i])

for i in names:               # 方式2：直接遍历元素
    print(i)

# 修改列表中的元素
names = ['张三', '李四', '王五', '张三']
print(names)

for i in range(len(names)):
    if names[i] == '张三':
        names[i] = '张三三'   # 将 '张三' 替换为 '张三三'
print(names)

# --- 15. 列表切片、拼接、重复、成员判断 ---
names = ['张三', '李四', '王五', '张三']
print(names[::])
print(names[1:3:1])
print(names[:3:1])

names1 = ['张三', '李四', '王五', '张三']
names2 = ['a', 'b', 'c', 'd']

print(names1 + names2)        # 列表拼接
print(names1 * 2)             # 列表重复
print('张三' in names1)       # 成员判断（整体匹配）
print('张' in names1)         # 不会匹配到子串
print('a' not in names1)

# --- 16. 列表增加元素：append追加、extend扩展、insert插入 ---
names1 = ['张三', '李四', '王五', '张三']
print(names1, id(names1))
names1.append('赵六')         # 在末尾追加一个元素（id不变，原地修改）
print(names1, id(names1))

print(names1.count('张三'))   # 统计 '张三' 出现次数

names2 = ['a', 'b', 'c']
names1.extend(names2)         # 将另一列表的元素逐个追加
print(names1)

print(names.index('张三'))    # 查找 '张三' 首次出现的位置

names1.insert(0, '侯七')      # 在指定位置插入元素
print(names1)
names1.insert(100, '侯七七')  # 索引超出范围时插入到末尾
print(names1)

# --- 17. 列表删除元素：pop弹出、remove移除、clear清空 ---
names1.pop()                  # 默认弹出末尾元素
print(names1)
names1.pop(0)                 # 弹出指定位置的元素
print(names1)

names1.remove('张三')         # 按值删除（只删第一个匹配项）
print(names1)

while '张三' in names1:       # 循环删除所有值为 '张三' 的元素
    names1.remove('张三')
print(names1)

# --- 18. 列表排序与反转：reverse、sort ---
names1.reverse()              # 原地反转列表
print(names1)
print(names1[::-1])           # 切片反转（不改变原列表）

list1 = [5, 3, 4, 2, 1, 8, 7, 6]
print(list1)
list1.sort(reverse=True)      # 降序排序（原地修改）
print(list1)

list2 = [[5, 3], [2, 1], [4, 6]]
print(list2)
list2.sort(key=lambda x: x[1]) # 按每个子列表的第2个元素排序
print(list2)

names1.clear()                # 清空列表
print(names1)

# --- 19. 列表拷贝：直接赋值 vs copy()浅拷贝 ---
names1 = ['a', 'b', 'c']
names2 = names1               # 直接赋值：names2和names1指向同一对象
names3 = names1.copy()        # copy()：创建新对象（浅拷贝）
print(names1, id(names1))
print(names2, id(names2))     # id与names1相同 → 同一对象
print(names3, id(names3))     # id不同 → 独立的新列表
names1.append('d')            # 修改names1
print(names1, id(names1))
print(names2, id(names2))     # names2也跟着变了（同一对象）
print(names3, id(names3))     # names3不受影响（独立对象）

# =======================第三遍=============================
# --- 1. 字符串索引：正数从0开始，负数从-1开始（倒数） ---
name = '张三'
print(name)

s = 'helloworld'
print(s)
print(s[5])           # 第6个字符
print(s[-1])          # 倒数第1个字符
print(s[-5])          # 倒数第5个字符
# 遍历字符串的三种方式
for i in range(0, len(s), 1):   # 方式1：用索引遍历
    print(s[i])
for i in range(len(s)):         # 方式2：省略start和step
    print(s[i])
for i in s:                     # 方式3：直接遍历字符（最简洁）
    print(i)

# --- 2. 字符串切片：[起始:结束:步长]，左闭右开 ---
s = 'helloworld'
print(s)
print(s[0:5:1])     # 索引0~4，步长1 → hello
print(s[1:5:2])     # 索引1,3，步长2 → el
print(s[::])        # 全拷贝
print(s[::2])       # 每隔一个字符取一个
print(s[:])         # 全拷贝
print(s[-10:-1])    # 负索引切片
print(s[-10:])      # 从倒数第10到末尾
print(s[-10:5:1])   # 负正索引混用
print(s[::-1])      # 步长-1 → 字符串反转
print(s[-8:7:1])
print(s[-8:0:-1])

# --- 3. 字符串拼接、重复、成员判断、转义字符 ---
s1 = 'hello'
s2 = 'world'
print(s1 + s2)          # 字符串拼接
print('=' * 50)         # 字符串重复
print('h' in s1)        # 成员判断：是否包含
print('w' not in s2)    # 成员判断：是否不包含
print('abc\tabc')       # \t 是制表符
print('abc\\tabc')      # \\ 表示一个反斜杠字符
print(r'abc\tabc')      # r'' 原始字符串，转义符不生效

# --- 4. 逢7过游戏：含7或7的倍数就说"过" ---
for i in range(1, 101, 1):
    if '7' in str(i) or i % 7 == 0:
        print('过', end=' ')
    else:
        print(i, end=' ')

# --- 5. 字符串格式化的三种方式 ---
name = input('请输入姓名')
age = 18
height = 185
print('你的名字是%s,你的年龄是%d,你的身高是%.2f' % (name, age, height))            # % 格式化
print(f'你的名字是{name}，你的年龄是{age}，你的身高是{height}')                     # f-string
print('你的名字是{}，你的年龄是{}，你的身高是{}'.format(name, age, height))          # format方法
print('你的名字是{0},你的年龄是{1},你的身高是{2},名字是{0}'.format(name, age, height))  # 索引复用

# --- 6. 字符串查找：count计数、startswith/endswith判断、find/index查找 ---
s = 'helloworld'
print(s.count('h'))         # 统计 'h' 出现次数
print(s.count('l'))
print(s.count('l', 5, 1))   # 起始>结束，返回0
print(s.count('l', 5))      # 从索引5开始统计

print(s.startswith('h'))    # 是否以 'h' 开头
print(s.startswith('w', 5)) # 从索引5开始是否以 'w' 开头

print(s.endswith('d'))      # 是否以 'd' 结尾
print(s.endswith('o', 0, 4)) # 索引0~3范围内是否以 'o' 结尾

print(s.find('l'))          # 查找 'l' 首次出现位置，找不到返回-1
print(s.find('l', 5))
print(s.find('z'))          # 找不到返回-1

print(s.index('l'))         # 与find类似，但找不到会抛出异常
print(s.index('l', 5))
# print(s.index('z'))       # 找不到会抛出 ValueError

# --- 7. isdigit判断数字、成绩判断 ---
print('123'.isdigit())      # 判断字符串是否全为数字

score = input('请输入您的成绩:')
if score.isdigit():         # 先校验输入是否合法
    score = int(score)
    if score >= 60:
        print('及格')
    else:
        print('不及格')
else:
    print('输入不合法')

# --- 8. join拼接、len/lower/upper ---
list1 = ['a', 'b', 'c']
print('a_b_c')
print(' '.join(list1))      # 用空格拼接列表 → 'a b c'

print(len(s))               # 字符串长度
print(s.lower())            # 转小写
print(s.upper())            # 转大写

# --- 9. strip系列：去除两端/左侧/右侧的空白字符 ---
str1 = '   abc   '
print(str1, len(str1))
print(str1.lstrip(), len(str1.lstrip()))   # 去左空白
str1 = '   abc   '
print(str1, len(str1))
print(str1.rstrip(), len(str1.rstrip()))   # 去右空白
str1 = '   abc   '
print(str1, len(str1))
print(str1.strip(), len(str1.strip()))     # 去两端空白

# --- 10. max/min：取最大值/最小值（字符串按ASCII比较） ---
print(max('abc'))
print(max([1, 2, 3]))
print(max(['1', '2', '3']))   # 字符串比较按ASCII码
print(min('abc'))
print(min([1, 2, 3]))
print(min(['1', '2', '3']))

# --- 11. replace替换、rindex从右查找 ---
s = '我爱你，你爱他，他爱我'
print('s')
print(s.replace('爱', '不爱'))       # 全部替换
print(s.replace('爱', '不爱', 1))     # 只替换第1个

s = 'helloworld'
print(s.rindex('l'))          # 从右侧查找 'l' 的位置

# --- 12. split分割、swapcase大小写反转 ---
s = 'a b \n c         d'
print(s.split())              # 默认按空白字符分割（空格、换行等）
s = 'a_b_c_d'
print(s.split('_'))           # 按下划线分割

s = 'Helloworld'
print(s.swapcase())           # 大小写反转 → 'hELLOWORLD'


# --- 13. 综合练习：格式化英文歌词（每行首字母大写，独立的 'i' 改为 'I'） ---
s = '''when I Was Young i'd listen to the Radio
         waiting for My Favorite songs
       when They played i'd sing Along
                    it Made me Smile         '''.strip()
print(s)
s2 = ''                       # 存放处理后的歌词
index1 = -1                   # 上一行换行符的位置
while True:
    index2 = s.find('\n', index1 + 1)   # 查找下一个换行符
    if index2 == -1:                    # 没有换行符 → 最后一行
        s2 += s[index1 + 1:].strip().capitalize()
        break
    s2 += s[index1 + 1:index2].strip().capitalize() + '\n'
    index1 = index2
s2 = s2.replace(' i ', ' I ').replace(" i ", " I ")   # 将独立的 'i' 大写
print(s2)


# --- 14. 列表：创建、索引、遍历 ---
names = ['张三', '李四', '王五']
print(names, type(names))     # 打印列表及类型
print(names[0])               # 第一个元素
print(names[-1])              # 最后一个元素

names = ['张三', '李四', '王五']

# 遍历列表的两种方式
for i in range(len(names)):   # 方式1：通过索引遍历
    print(names[i])

for i in names:               # 方式2：直接遍历元素
    print(i)

# 修改列表中的元素
names = ['张三', '李四', '王五', '张三']
print(names)

for i in range(len(names)):
    if names[i] == '张三':
        names[i] = '张三三'   # 将 '张三' 替换为 '张三三'
print(names)

# --- 15. 列表切片、拼接、重复、成员判断 ---
names = ['张三', '李四', '王五', '张三']
print(names[::])
print(names[1:3:1])
print(names[:3:1])

names1 = ['张三', '李四', '王五', '张三']
names2 = ['a', 'b', 'c', 'd']

print(names1 + names2)        # 列表拼接
print(names1 * 2)             # 列表重复
print('张三' in names1)       # 成员判断（整体匹配）
print('张' in names1)         # 不会匹配到子串
print('a' not in names1)

# --- 16. 列表增加元素：append追加、extend扩展、insert插入 ---
names1 = ['张三', '李四', '王五', '张三']
print(names1, id(names1))
names1.append('赵六')         # 在末尾追加一个元素（id不变，原地修改）
print(names1, id(names1))

print(names1.count('张三'))   # 统计 '张三' 出现次数

names2 = ['a', 'b', 'c']
names1.extend(names2)         # 将另一列表的元素逐个追加
print(names1)

print(names.index('张三'))    # 查找 '张三' 首次出现的位置

names1.insert(0, '侯七')      # 在指定位置插入元素
print(names1)
names1.insert(100, '侯七七')  # 索引超出范围时插入到末尾
print(names1)

# --- 17. 列表删除元素：pop弹出、remove移除、clear清空 ---
names1.pop()                  # 默认弹出末尾元素
print(names1)
names1.pop(0)                 # 弹出指定位置的元素
print(names1)

names1.remove('张三')         # 按值删除（只删第一个匹配项）
print(names1)

while '张三' in names1:       # 循环删除所有值为 '张三' 的元素
    names1.remove('张三')
print(names1)

# --- 18. 列表排序与反转：reverse、sort ---
names1.reverse()              # 原地反转列表
print(names1)
print(names1[::-1])           # 切片反转（不改变原列表）

list1 = [5, 3, 4, 2, 1, 8, 7, 6]
print(list1)
list1.sort(reverse=True)      # 降序排序（原地修改）
print(list1)

list2 = [[5, 3], [2, 1], [4, 6]]
print(list2)
list2.sort(key=lambda x: x[1]) # 按每个子列表的第2个元素排序
print(list2)

names1.clear()                # 清空列表
print(names1)

# --- 19. 列表拷贝：直接赋值 vs copy()浅拷贝 ---
names1 = ['a', 'b', 'c']
names2 = names1               # 直接赋值：names2和names1指向同一对象
names3 = names1.copy()        # copy()：创建新对象（浅拷贝）
print(names1, id(names1))
print(names2, id(names2))     # id与names1相同 → 同一对象
print(names3, id(names3))     # id不同 → 独立的新列表
names1.append('d')            # 修改names1
print(names1, id(names1))
print(names2, id(names2))     # names2也跟着变了（同一对象）
print(names3, id(names3))     # names3不受影响（独立对象）
