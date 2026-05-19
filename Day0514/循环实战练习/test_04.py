"""
第4题：计算100以内（包括100）的偶数之和
"""

def main():
    total = 0
    for i in range(2, 101, 2):
        total += i

    print(f"100以内偶数之和为：{total}")


if __name__ == "__main__":
    main()
