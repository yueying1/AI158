"""
第19题：雨淋湿了算术本上一道题，8个数字只能看清3个
[□×(□3+□)]^2 = 8□□9
第一个数字虽然模糊不清楚，但可看出不是1
确定方框中应是什么数

解析：
设方框中的数字分别为 a, b, c, d, e（每位0-9）
公式：[a × (10b + 3 + c)]^2 = 8000 + 100d + 10e + 9
其中 a != 1, a 是0-9的数字但第一位不能是0
"""

def main():
    found = False
    for a in range(2, 10):  # 第一个数字不是1，且不能是0（作为乘数）
        for b in range(10):
            for c in range(10):
                value = a * (b * 10 + 3 + c)
                square = value * value

                # 检查是否为4位或5位数，且格式为 8xxx9
                if 10000 <= square <= 89999 or 1000 <= square <= 9999:
                    s = str(square)
                    if s[0] == '8' and s[-1] == '9':
                        found = True
                        print(f"找到解：a={a}, b={b}, c={c}")
                        print(f"  公式：[{a}×({b}3+{c})]^2 = [{a}×{b*10+3+c}]^2 = {value}^2 = {square}")
                        print(f"  即：8□□9 中的数字为 {square}")
                        print()

    # 同样尝试5位数范围
    for a in range(2, 10):
        for b in range(10):
            for c in range(10):
                value = a * (b * 10 + 3 + c)
                square = value * value

                if 80000 <= square <= 89999:
                    s = str(square)
                    if s[-1] == '9':
                        print(f"5位解：a={a}, b={b}, c={c}, square={square}")

    if not found:
        # 扩大搜索：考虑 a 可能为多位数（非1）
        print("穷举搜索所有可能...")
        for a in range(2, 100):  # a是非1的整数
            for b in range(10):
                for c in range(10):
                    value = a * (b * 10 + 3 + c)
                    square = value * value
                    s = str(square)
                    if len(s) == 5 and s[0] == '8' and s[-1] == '9':
                        print(f"a={a}, b={b}, c={c}: [{a}×({b}3+{c})]^2 = {square}")
                        found = True

    if not found:
        print("未找到满足条件的完整解，请检查题目条件。")


if __name__ == "__main__":
    main()
