"""
第10题：任意输入5个数，找出最小数
"""

def main():
    nums = []
    for i in range(5):
        n = float(input(f"请输入第{i+1}个数："))
        nums.append(n)

    min_num = nums[0]
    for n in nums:
        if n < min_num:
            min_num = n

    print(f"5个数为：{nums}")
    print(f"最小的数是：{min_num}")


if __name__ == "__main__":
    main()
