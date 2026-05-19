"""
第6题：用户登录验证，验证次数最多3次
"""

def main():
    correct_username = "admin"
    correct_password = "123456"

    for attempt in range(1, 4):
        print(f"\n第{attempt}次登录")
        username = input("请输入用户名：")
        password = input("请输入密码：")

        if username == correct_username and password == correct_password:
            print("登录成功！欢迎回来！")
            break
        else:
            remaining = 3 - attempt
            if remaining > 0:
                print(f"用户名或密码错误，还剩{remaining}次机会")
            else:
                print("3次机会已用完，账号已被锁定！")
    else:
        print("请稍后再试。")


if __name__ == "__main__":
    main()
