"""
循环实战练习 — 全部20道题汇总
=================================
本文件包含所有20道循环实战练习的核心代码
每道题封装为一个独立函数，通过菜单选择运行
"""

import math


# ==================== 第1题：商品换购功能 ====================
def test_01():
    """嵌套if选择结构实现商品换购功能"""
    print("\n【第1题】商品换购功能")
    print("-" * 30)
    amount = float(input("请输入消费金额："))
    if amount >= 50:
        print("1.加1元换购矿泉水  2.加3元换购可乐  3.加5元换购薯片  4.不换购")
        choice = int(input("请选择(1-4)："))
        if choice == 1:
            print(f"换购矿泉水，总额：{amount + 1:.2f}元")
        elif choice == 2:
            print(f"换购可乐，总额：{amount + 3:.2f}元")
        elif choice == 3:
            print(f"换购薯片，总额：{amount + 5:.2f}元")
        else:
            print(f"不换购，总额：{amount:.2f}元")
    else:
        print("消费不足50元，无法换购")


# ==================== 第2题：考试成绩奖励 ====================
def test_02():
    """输入考试成绩显示奖励"""
    print("\n【第2题】考试成绩奖励")
    print("-" * 30)
    score = float(input("请输入考试成绩："))
    if score == 100:
        print("爸爸给他买辆车！")
    elif score >= 90:
        print("妈妈给他买MP4！")
    elif score >= 60:
        print("妈妈给他买本参考书！")
    else:
        print("什么都不买！")


# ==================== 第3题：温度对照表 ====================
def test_03():
    """摄氏温度与华氏温度对照表（while循环）"""
    print("\n【第3题】摄氏/华氏温度对照表")
    print("-" * 30)
    print("摄氏\t华氏")
    c, count = 0, 0
    while c <= 250 and count < 10:
        print(f"{c}\t{c * 9 / 5.0 + 32:.1f}")
        c += 20
        count += 1


# ==================== 第4题：100以内偶数之和 ====================
def test_04():
    """计算100以内偶数之和"""
    print("\n【第4题】100以内偶数之和")
    print("-" * 30)
    total = sum(range(2, 101, 2))
    print(f"结果：{total}")


# ==================== 第5题：小红年龄问题 ====================
def test_05():
    """小红12岁，父亲比她大20岁，几年后父亲年龄是小红2倍"""
    print("\n【第5题】小红年龄问题")
    print("-" * 30)
    xh, fa = 12, 32
    years = 0
    while fa + years != 2 * (xh + years):
        years += 1
    print(f"{years}年后，父亲年龄是小红的2倍")
    print(f"小红{xh + years}岁，父亲{fa + years}岁")


# ==================== 第6题：用户登录验证 ====================
def test_06():
    """用户登录验证，最多3次"""
    print("\n【第6题】用户登录验证（默认账号admin/123456）")
    print("-" * 30)
    for i in range(1, 4):
        user = input(f"第{i}次 - 用户名：")
        pwd = input("密码：")
        if user == "admin" and pwd == "123456":
            print("登录成功！")
            return
        print(f"错误！还剩{3-i}次")
    print("3次已用完，账号锁定！")


# ==================== 第7题：里程表对称数 ====================
def test_07():
    """里程表对称数95859，求2小时后新对称数和时速"""
    print("\n【第7题】里程表对称数")
    print("-" * 30)
    start = 95859
    n = start + 1
    while str(n).zfill(5) != str(n).zfill(5)[::-1]:
        n += 1
    print(f"新对称数：{n}")
    print(f"时速：{(n - start) / 2:.1f} km/h")


# ==================== 第8题：求n! ====================
def test_08():
    """求n!（3<=n<=15），含输入校验"""
    print("\n【第8题】求n!")
    print("-" * 30)
    while True:
        n = int(input("请输入n(3~15)："))
        if 3 <= n <= 15:
            break
        print("不满足条件，重新输入！")
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"{n}! = {result}")


# ==================== 第9题：三角形判断 ====================
def test_09():
    """输入三边判断能否构成三角形，能则求面积"""
    print("\n【第9题】三角形判断与面积")
    print("-" * 30)
    a = float(input("边长a："))
    b = float(input("边长b："))
    c = float(input("边长c："))
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"面积：{area:.2f}")
    else:
        print("不能构成三角形！")


# ==================== 第10题：5个数找最小 ====================
def test_10():
    """任意输入5个数找最小"""
    print("\n【第10题】5个数找最小")
    print("-" * 30)
    nums = [float(input(f"第{i+1}个数：")) for i in range(5)]
    print(f"最小数：{min(nums)}")


# ==================== 第11题：n个数(-1结束)找最大最小 ====================
def test_11():
    """输入n个数，-1结束，找最大最小"""
    print("\n【第11题】n个数找最大最小（-1结束）")
    print("-" * 30)
    nums = []
    while True:
        n = float(input("输入数字(-1结束)："))
        if n == -1:
            break
        nums.append(n)
    if nums:
        print(f"最大：{max(nums)}，最小：{min(nums)}")
    else:
        print("未输入任何数字")


# ==================== 第12题：猴子吃桃 ====================
def test_12():
    """猴子吃桃：第10天剩1个，每天吃一半多一个，求第一天总数"""
    print("\n【第12题】猴子吃桃")
    print("-" * 30)
    peach = 1
    for day in range(9, 0, -1):
        peach = (peach + 1) * 2
    print(f"第一天共摘了{peach}只桃子")


# ==================== 第13题：同构数 ====================
def test_13():
    """1~10000之间的同构数"""
    print("\n【第13题】1~10000之间的同构数")
    print("-" * 30)
    results = []
    for i in range(1, 10001):
        if str(i * i).endswith(str(i)):
            results.append((i, i * i))
    for n, sq in results:
        print(f"{n} -> {sq}")


# ==================== 第14题：水仙花数 ====================
def test_14():
    """100~999之间的水仙花数"""
    print("\n【第14题】100~999之间的水仙花数")
    print("-" * 30)
    for n in range(100, 1000):
        a, b, c = n // 100, n // 10 % 10, n % 10
        if a**3 + b**3 + c**3 == n:
            print(f"{n} = {a}^3 + {b}^3 + {c}^3")


# ==================== 第15题：素数 ====================
def test_15():
    """3~100之间的素数"""
    print("\n【第15题】3~100之间的素数")
    print("-" * 30)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [n for n in range(3, 101) if is_prime(n)]
    for i, p in enumerate(primes):
        print(f"{p:3d}", end="  " if (i + 1) % 10 else "\n")
    print(f"\n共{len(primes)}个")


# ==================== 第16题：奇数阶乘前10项和 ====================
def test_16():
    """1! + 3! + 5! + ... + (2n-1)! 前10项和"""
    print("\n【第16题】1!+3!+5!+...+19! 前10项和")
    print("-" * 30)

    def fact(n):
        r = 1
        for i in range(1, n + 1):
            r *= i
        return r

    total = sum(fact(2 * i - 1) for i in range(1, 11))
    print(f"结果：{total}")


# ==================== 第17题：累加序列求和 ====================
def test_17():
    """S = 1 + (1+2) + (1+2+3) + ... + (1+2+...+n)"""
    print("\n【第17题】S=1+(1+2)+(1+2+3)+...+(1+2+...+n)")
    print("-" * 30)
    n = int(input("请输入n："))
    total, cur = 0, 0
    for i in range(1, n + 1):
        cur += i
        total += cur
    print(f"S = {total}")


# ==================== 第18题：奇数累加级数 ====================
def test_18():
    """s = 1 + (1+3) + (1+3+5) + ... + (1+3+...+2n-1)"""
    print("\n【第18题】s=1+(1+3)+(1+3+5)+...")
    print("-" * 30)
    n = int(input("请输入n："))

    def term(k):
        return sum(2 * i - 1 for i in range(1, k + 1))

    total = sum(term(k) for k in range(1, n + 1))
    print(f"s = {total}")


# ==================== 第19题：枚举解方程 ====================
def test_19():
    """[□×(□3+□)]^2 = 8□□9 确定方框中数字"""
    print("\n【第19题】[□×(□3+□)]^2 = 8□□9")
    print("-" * 30)
    found = []
    for a in range(2, 100):  # 第一个数字不是1
        for b in range(10):
            for c in range(10):
                v = a * (b * 10 + 3 + c)
                sq = v * v
                s = str(sq)
                if len(s) == 5 and s[0] == '8' and s[-1] == '9':
                    found.append((a, b, c, v, sq))
                    print(f"[{a}×({b}3+{c})]^2 = {v}^2 = {sq}")

    if not found:
        # 尝试4位结果
        for a in range(2, 100):
            for b in range(10):
                for c in range(10):
                    v = a * (b * 10 + 3 + c)
                    sq = v * v
                    s = str(sq)
                    if len(s) in (4, 5) and s[0] == '8' and s[-1] == '9':
                        found.append((a, b, c, v, sq))

        if found:
            for a, b, c, v, sq in found:
                print(f"[{a}×({b}3+{c})]^2 = {v}^2 = {sq}")
        else:
            print("未找到解，请检查题目条件")


# ==================== 第20题：完备数 ====================
def test_20():
    """100以内的完备数（因子和等于本身）"""
    print("\n【第20题】100以内的完备数")
    print("-" * 30)
    for n in range(2, 101):
        factors = [i for i in range(1, n) if n % i == 0]
        if sum(factors) == n:
            print(f"{n} = {' + '.join(str(f) for f in factors)}")


# ==================== 主菜单 ====================
def main():
    tests = [
        test_01, test_02, test_03, test_04, test_05,
        test_06, test_07, test_08, test_09, test_10,
        test_11, test_12, test_13, test_14, test_15,
        test_16, test_17, test_18, test_19, test_20,
    ]

    while True:
        print("\n" + "=" * 40)
        print("循环实战练习 — 全部20道题汇总")
        print("=" * 40)
        print(" 1. 商品换购功能         11. n个数找最大最小")
        print(" 2. 考试成绩奖励         12. 猴子吃桃")
        print(" 3. 温度对照表(while)    13. 同构数(1~10000)")
        print(" 4. 100以内偶数之和      14. 水仙花数(100~999)")
        print(" 5. 小红年龄问题         15. 素数(3~100)")
        print(" 6. 用户登录验证         16. 奇数阶乘前10项和")
        print(" 7. 里程表对称数         17. 累加序列求和")
        print(" 8. 求n!(3~15)          18. 奇数累加级数")
        print(" 9. 三角形判断与面积     19. 枚举解方程")
        print("10. 5个数找最小         20. 完备数(<=100)")
        print(" 0. 退出")
        print("-" * 40)
        choice = input("请选择题目编号(1-20, 0退出)：")

        if choice == "0":
            print("再见！")
            break
        elif choice.isdigit() and 1 <= int(choice) <= 20:
            tests[int(choice) - 1]()
        else:
            print("无效选择，请重新输入！")


if __name__ == "__main__":
    main()
