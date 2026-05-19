"""
第15题：输出3~100之间的全部素数
"""

def is_prime(n):
    """判断一个数是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    primes = [n for n in range(3, 101) if is_prime(n)]
    print("3~100之间的素数：")
    # 每行输出10个
    for i, p in enumerate(primes):
        print(f"{p:3d}", end="   ")
        if (i + 1) % 10 == 0:
            print()
    print(f"\n共{len(primes)}个素数")


if __name__ == "__main__":
    main()
