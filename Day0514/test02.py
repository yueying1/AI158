grade = input('输入赵本山的考试成绩：')
grade = int(grade)

if grade == 100 :
    print('奖励为爸爸买的车')
elif 90 <= grade < 100:
    print('奖励为妈妈买的MP4')
elif 60 <= grade < 90:
    print('奖励为妈妈买的参考书')
else:
    print('没有奖励')
