"""
第16题：计算 1! + 3! + 5! + ... + (2n-1)! 前10项和
即：1! + 3! + 5! + ... + 19!
"""

def factorial(n):
    """计算n的阶乘"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    n = 10  # 前10项
    total = 0
    terms = []

    for i in range(1, n + 1):
        odd = 2 * i - 1  # 第i项对应的奇数为 2i-1
        fact = factorial(odd)
        total += fact
        terms.append(f"{odd}!")

    print(f"计算前{n}项和：{' + '.join(terms)}")
    print(f"结果 = {total}")


if __name__ == "__main__":
    main()
