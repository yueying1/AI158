"""
第20题：求100以内的所有完备数
完备数是其各因子之和等于其本身的正整数
例如：6 = 1 + 2 + 3
"""

def sum_of_factors(n):
    """计算n的所有真因子之和（不含n本身）"""
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total


def main():
    perfect_numbers = []
    details = []

    for num in range(2, 101):
        factors = [i for i in range(1, num) if num % i == 0]
        if sum(factors) == num:
            perfect_numbers.append(num)
            details.append(f"{num} = {' + '.join(str(f) for f in factors)}")

    print("100以内的完备数：")
    for d in details:
        print(f"  {d}")

    if perfect_numbers:
        print(f"\n共{len(perfect_numbers)}个完备数")
    else:
        print("  无")


if __name__ == "__main__":
    main()
