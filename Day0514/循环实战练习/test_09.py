"""
第9题：从键盘输入a,b,c三个值，检查能否构成三角形
如能构成三角形，则计算三角形的面积（海伦公式）
提示：任意两边之和大于第三边
"""

import math


def main():
    a = float(input("请输入边长a："))
    b = float(input("请输入边长b："))
    c = float(input("请输入边长c："))

    # 判断能否构成三角形：任意两边之和大于第三边
    if a + b > c and a + c > b and b + c > a:
        # 海伦公式
        p = (a + b + c) / 2  # 半周长
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"能构成三角形，面积为：{area:.2f}")
    else:
        print("不能构成三角形！")


if __name__ == "__main__":
    main()
