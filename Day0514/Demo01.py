# # num = '111001'
# # a = int(num,2)
# # print(a)
# # import random
#
# # print(int(-18))
# # print(int(+18))
# # print(int(18.8))
#
#
# # def sum1 (a, b):
# #     return a + b
# #
# # print('世界', end='， ')
# # print('你好')
# #
# # num1 = 1
# # num2 = 2
# # print(num1, '+', num2, '=', num1 + num2, sep=',')
#
#
# # print('1 + 1 = 2',end='\t')
# # print('1 + 1 = 2',end='\t')
#
#
# # for i in range(1, 100):
# #     print(i)
#
#
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '*', i, '=', i * j, end='\t')

    print()
#
#
#
# # random.seed(3)
# # print(random.randint(1,10))
# # print(random.uniform(1,10))
# #
# # for num_cock in range(0, 21):  # 公鸡数量范围为 0 到 20（包括0和20）
# # 	for num_hen in range(0, 34):  # 母鸡数量范围为 0 到 33（包括0和33）
# # 		num_chick = 100 - num_cock - num_hen  # 小鸡数量为总数减去公鸡和母鸡的数量
# # 		total_cost = 5 * num_cock + 3 * num_hen + num_chick // 3  # 计算总花费
# #
# # 		if num_chick % 3 == 0 and total_cost == 100:  # 检查小鸡数量是否是3的倍数且总花费为100
# # 			print("公鸡数量：{}, 母鸡数量：{}, 小鸡数量：{}".format(num_cock, num_hen, num_chick))
#
#
# sum1 = 0
# for i in range(101):
#     sum1 += i
# print(f'1-100累计和{sum1}')
#
# sum2 = 0
# for i in range(101):
#     if i % 2 == 0 :
#         sum2 += i
# print(f'1-100偶数和为{sum2}')
#
#
# sum3 = 0
# for i in range(101):
#     if i % 2 != 0 :
#         sum3 += i
# print(f'1-100奇数和为{sum3}')
#
#
# sum4 = 0
# for i in range(101):
#     if i % 3 == 0 :
#         sum4 += i
# print(f'1-100之间3的倍数的和为{sum4}')

# i = 1
# while i <= 100:
#     if i % 5 ==0 :
#         break
#     print(i)
#
#     i = i + 1