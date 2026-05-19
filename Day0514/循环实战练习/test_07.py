"""
第7题：里程表对称数问题
清晨里程表读数为95859（对称数），2小时后出现新的对称数
设里程表为5位数字，求汽车时速和新的对称数
"""

def is_palindrome(n):
    """判断一个5位数是否为对称数"""
    s = str(n).zfill(5)
    return s == s[::-1]


def main():
    start = 95859

    # 找大于95859的下一个对称数
    new_num = start + 1
    while not is_palindrome(new_num):
        new_num += 1

    speed = (new_num - start) / 2  # 2小时后的里程差除以时间

    print(f"初始里程表读数：{start}")
    print(f"2小时后的里程表读数：{new_num}")
    print(f"汽车的时速为：{speed:.1f} km/h")


if __name__ == "__main__":
    main()
