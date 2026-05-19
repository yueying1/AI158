"""
第12题：猴子吃桃问题
小猴子摘来一些桃。它吃掉了一半，觉得不过瘾，又吃掉了一只。
第二天，它也这样，先吃了剩下的一半，再多吃一只。第三天也如此。
第十天小猴子一看，就剩一个桃子了。
问小猴子那天共摘来多少只桃？
"""

def main():
    # 逆向递推：第10天剩1个
    # 每天开始时的桃子数 = (剩下的 + 1) * 2
    peach = 1  # 第10天剩1个
    day = 10

    while day > 1:
        peach = (peach + 1) * 2
        day -= 1

    print(f"小猴子第一天共摘了{peach}只桃子")

    # 验证正向过程
    total = peach
    for d in range(1, 11):
        eat = total / 2 + 1
        total = total - eat
        print(f"第{d}天：吃了{eat:.0f}只，剩下{total:.0f}只")


if __name__ == "__main__":
    main()
