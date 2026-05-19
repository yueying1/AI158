"""
第14题：水仙花数
如果一个数等于它的每一位数的立方和，则称为水仙花数
如153=1^3+5^3+3^3=1+125+27
求100~999之间的全部水仙花数
"""

def main():
    results = []
    for num in range(100, 1000):
        # 分离百位、十位、个位
        a = num // 100      # 百位
        b = num // 10 % 10  # 十位
        c = num % 10        # 个位

        if a**3 + b**3 + c**3 == num:
            results.append(num)

    print("100~999之间的水仙花数：")
    for r in results:
        a, b, c = r // 100, r // 10 % 10, r % 10
        print(f"{r} = {a}^3 + {b}^3 + {c}^3 = {a**3} + {b**3} + {c**3}")


if __name__ == "__main__":
    main()
