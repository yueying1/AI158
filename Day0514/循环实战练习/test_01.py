"""
第1题：嵌套if选择结构实现商品换购功能
综合运用嵌套if选择结构实现商品换购功能
"""

def main():
    print("=" * 40)
    print("欢迎参加商品换购活动")
    print("=" * 40)

    amount = float(input("请输入您的消费金额："))

    if amount >= 50:
        print("\n恭喜！消费满50元，可以参加换购活动！")
        print("1. 加1元换购矿泉水（原价2元）")
        print("2. 加3元换购可乐（原价5元）")
        print("3. 加5元换购薯片（原价8元）")
        print("4. 不换购")

        choice = int(input("请选择换购商品（1-4）："))

        if choice == 1:
            print(f"换购成功！消费总额：{amount + 1:.2f}元，获得矿泉水一瓶")
        elif choice == 2:
            print(f"换购成功！消费总额：{amount + 3:.2f}元，获得可乐一瓶")
        elif choice == 3:
            print(f"换购成功！消费总额：{amount + 5:.2f}元，获得薯片一包")
        elif choice == 4:
            print(f"不换购。消费总额：{amount:.2f}元")
        else:
            print("无效选择！")
    else:
        print(f"\n消费不足50元，无法参加换购活动。消费总额：{amount:.2f}元")


if __name__ == "__main__":
    main()
