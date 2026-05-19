# s = 'Hello World Python'

# print(f'截取{s[0: 6]}123')
# print(s[::-1])
# print(s[::-2])


# l1 = [1, 2, 3, 4, 5, 6]
# print(l1[-1])
# for i in l1[::-1]:
#     print(i)

# print('\n')

# a = s.count('o')
# print(a)
#
# b = s.startswith('a')
# print(b)
#
# c = s.find('b')
# print(c)
#
# print(s.upper())


#   过7

# i = 1
# while i <= 100:
#     if i % 7 ==0 or '7' in str(i) :
#         print('过', end=' ')
#     else:
#         print(i, end=' ')
#     i += 1




#   优化歌词

# '''
# when I Was Young i'd listen to the Radio
#          waiting for My Favorite songs
#       when They played i'd sing Along
#                  it Made me Smile
# '''
#
# s = '''when I Was Young i'd listen to the Radio
#          waiting for My Favorite songs
#       when They played i'd sing Along
#                  it Made me Smile   '''
# def change_first_world(str1):
#     first_str = str1[0]
#     right_str = str1[1:]
#     new_str = first_str.upper() + right_str
#     return new_str
# print(s)
# new_s = ''
# enter_index_qian = 0
# enter_index_hou = 0
# end_index = -1
# print(len(s))
# while True:
#     enter_index_hou = s.find('\n', enter_index_qian, len(s))
#     if enter_index_hou == -1 :
#         enter_index_hou = len(s)
#     s1 = s[enter_index_qian: enter_index_hou]
#     s2 = s1.lstrip().strip()
#     # 第一个字母大写
#     new_s = new_s + change_first_world(s2) + '\n'
#     enter_index_qian = enter_index_hou + 1
#     if enter_index_hou == len(s) :
#         break
# print(new_s)


# s = '     123    456     '
# print(s)
# print(s.strip('1'))




#   优化歌词    优化
# def change_first_world(str1):
#     first_str = str1[0]
#     right_str = str1[1:]
#     new_str = first_str.upper() + right_str + '\n'
#     return new_str
# s = '''when I Was Young i'd listen to the Radio
#          waiting for My Favorite songs
#       when They played i'd sing Along
#                  it Made me Smile   '''
# # new_string = ''
# l1 = s.split('\n')
# for i in l1:
#     new_string += change_first_world(i.strip())
#
# print(new_string)

# l2 = [1, 2, 3, 4, 5]
# l1.extend(l2)
# print(l1)
# x = l1.pop()
# print(x)
# l3 = l2.copy()
# l2.remove(2)
# print(l2)
# print(l3)

# triangle = []
#
# for row in range(4):
#     # 创建一个新的行，并将其初始化为1
#     current_row = [1]
#
#     # 前一行的索引
#     prev_row = row - 1
#
#     # 如果不是第一行，则计算当前行的元素
#     if prev_row >= 0:
#         for i in range(1, row):
#             # 每个元素等于上一行相邻两个元素之和
#             element = triangle[prev_row][i-1] + triangle[prev_row][i]
#             current_row.append(element)
#
#         current_row.append(1)
#
#     # 将当前行添加到杨辉三角列表中
#     triangle.append(current_row)
# print(triangle)

#
# for i in range(1, 1):
#     print(i)
# print('end')




s = '''Twinkle, twinkle, little star, 
How I wonder what you are! 
Up above the world so high, 
Like a diamond in the sky. 
Twinkle, twinkle, little star, 
How I wonder what you are! 
When the blazing sun is gone, 
When he nothing shines upon,
Then you show your little light, 
Twinkle, twinkle, all the night.'''
dict_s = {}
l1 = s.replace(',',' ').replace('!',' ').split()
for word in l1 :
    word = word.lower()
    if dict_s.get(word,0) == 0 :
        dict_s[word] = 1
    else:
        dict_s[word] += 1

for key, value in dict_s.items():
    
    print(f'{key} : {value} ')




