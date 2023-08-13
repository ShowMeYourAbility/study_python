"""
在终端中循环录入多个个成绩，直到输入成绩为空
最后打印平均成绩(总成绩除以人数)
"""
total_score = 0
count = 0
while True:
    score = input("请输入第" + str(count + 1) + "个人的成绩：")
    if score == "":
        break
    count += 1
    total_score += float(score)

if count > 0:
    print(total_score / count)
else:
    print(0)
