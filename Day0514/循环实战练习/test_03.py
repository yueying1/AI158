"""
第3题：使用while实现摄氏温度与华氏温度对照表
从摄氏温度0度到250度，每隔20度为一项，对照表中的条目不超过10条
转换关系：华氏温度 = 摄氏温度 * 9 / 5.0 + 32
"""

def main():
    print("摄氏温度\t华氏温度")
    print("-" * 25)

    celsius = 0
    count = 0

    while celsius <= 250 and count < 10:
        fahrenheit = celsius * 9 / 5.0 + 32
        print(f"{celsius}\t\t{fahrenheit:.1f}")
        celsius += 20
        count += 1


if __name__ == "__main__":
    main()
