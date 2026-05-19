"""
第13题：找出1~10000之间的全部同构数
同构数指一个数出现在它的平方的右端。
如5的平方是25，5是25右端的数，5和25就是一对同构数。
"""

def main():
    results = []
    for i in range(1, 10001):
        square = i * i
        # 检查i是否在square的右端
        if str(square).endswith(str(i)):
            results.append((i, square))

    print("1~10000之间的同构数：")
    for num, sq in results:
        print(f"{num} 的平方是 {sq}，{num} 在 {sq} 的右端")


if __name__ == "__main__":
    main()
