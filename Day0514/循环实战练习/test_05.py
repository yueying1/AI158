"""
第5题：小红今年12岁，她父亲比她大20岁
计算出她父亲在几年后比她的年龄大1倍，那时他们两人的年龄各为多少？
"""

def main():
    xiao_hong = 12
    father = xiao_hong + 20  # 父亲比她大20岁

    years = 0
    while True:
        if father + years == 2 * (xiao_hong + years):
            break
        years += 1

    print(f"{years}年后，父亲的年龄是小红的2倍")
    print(f"那时小红{xiao_hong + years}岁，父亲{father + years}岁")


if __name__ == "__main__":
    main()
