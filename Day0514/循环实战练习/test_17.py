"""
第17题：计算 S = 1 + (1+2) + (1+2+3) + ... + (1+2+3+...+n)
n由用户输入
"""

def main():
    n = int(input("请输入n的值："))

    total = 0
    current_sum = 0  # 当前项的和

    for i in range(1, n + 1):
        current_sum += i  # 第i项 = 1+2+...+i
        total += current_sum

    # 输出各项验证
    terms = []
    s = 0
    for i in range(1, n + 1):
        s += i
        inner = "+".join(str(x) for x in range(1, i + 1))
        terms.append(f"({inner})")

    print(f"S = {' + '.join(terms)}")
    print(f"S = {total}")


if __name__ == "__main__":
    main()
