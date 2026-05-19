"""
第11题：任意输入n个数，当输入-1时结束，找出其中最大数和最小数
"""

def main():
    nums = []
    print("请输入数字（输入-1结束）：")

    while True:
        n = float(input())
        if n == -1:
            break
        nums.append(n)

    if nums:
        max_num = nums[0]
        min_num = nums[0]
        for n in nums:
            if n > max_num:
                max_num = n
            if n < min_num:
                min_num = n

        print(f"输入的数为：{nums}")
        print(f"最大数是：{max_num}")
        print(f"最小数是：{min_num}")
    else:
        print("未输入任何有效数字")


if __name__ == "__main__":
    main()
