# triangle = []
# num_rows = 5
# for row in range(num_rows):
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

# 
# triangle = []
# new_rows = int(input('输入杨辉三角的行数：'))
# for row in range(new_rows):
#     current_row = [1]
#     thePreviousLine = row - 1
#     if thePreviousLine >= 0 :
#         for i in range(1,row):
#             element = triangle[thePreviousLine][i - 1] + triangle[thePreviousLine][i]
#             current_row.append(element)
#         current_row.append(1)
#     triangle.append(current_row)
# 
# print(triangle)



# list1 = [8, 2, 16, 7, 13, -8]
# for j in range(len(list1)-1):
#     for i in range( len(list1)-1-j):
#         if list1[i] > list1[i + 1]:
#             n = list1[i]
#             list1[i] = list1[i + 1]
#             list1[i + 1] = n
#
# print(list1)




# n, m = 1, 2
# n, m = m, n
# print(n,'   ', m)


def partition(arr1, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr1[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr1[j] <= pivot:
            i = i + 1
            arr1[i], arr1[j] = arr1[j], arr1[i]

    arr1[i + 1], arr1[high] = arr1[high], arr1[i + 1]
    return i + 1


# arr1[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr2 = [10, 7, 8, 9, 1, 5]
n = len(arr2)
quickSort(arr2, 0, n - 1)
print("排序后的数组:")
for i in range(n):
    print("%d" % arr2[i])