"""
第18题：用子程序求级数的前n项和
级数为 s = 1 + (1+3) + (1+3+5) + ... + (1+3+5+...+2n-1)
"""

def term_sum(k):
    """计算第k项：1+3+5+...+(2k-1)"""
    total = 0
    for i in range(1, k + 1):
        total += 2 * i - 1
    return total


def series_sum(n):
    """计算级数前n项和"""
    total = 0
    for k in range(1, n + 1):
        total += term_sum(k)
    return total


def main():
    n = int(input("请输入n的值（前n项和）："))

    result = series_sum(n)

    # 输出各项
    terms = []
    for k in range(1, n + 1):
        inner = "+".join(str(2*i-1) for i in range(1, k + 1))
        terms.append(f"({inner})")

    print(f"s = {' + '.join(terms)}")
    print(f"s = {result}")


if __name__ == "__main__":
    main()
