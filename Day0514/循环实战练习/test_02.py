"""
第2题：输入赵本山的考试成绩，显示所获奖励
- 成绩==100分，爸爸给他买辆车
- 成绩>=90分，妈妈给他买MP4
- 90分>成绩>=60分，妈妈给他买本参考书
- 成绩<60分，什么都不买
"""

def main():
    score = float(input("请输入赵本山的考试成绩："))

    if score == 100:
        print("爸爸给他买辆车！")
    elif score >= 90:
        print("妈妈给他买MP4！")
    elif score >= 60:
        print("妈妈给他买本参考书！")
    else:
        print("什么都不买！")


if __name__ == "__main__":
    main()
