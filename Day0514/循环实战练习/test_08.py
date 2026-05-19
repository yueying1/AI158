"""
第8题：求n!，n由键盘输入，范围要求3~15之间
如果用户输入的数不满足条件，则提示重新输入，直到输入了正确的n
"""

def main():
    while True:
        n = int(input("请输入一个3~15之间的整数n："))
        if 3 <= n <= 15:
            break
        print("输入不满足条件，请重新输入！")

    # 计算阶乘
    result = 1
    for i in range(1, n + 1):
        result *= i

    print(f"{n}! = {result}")


if __name__ == "__main__":
    main()
