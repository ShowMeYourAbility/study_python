"""
在终端中循环录入5个成绩
最后打印平均成绩(总成绩除以人数)
"""
# 用for
# total_score = 0
# for i in range(5):
#     total_score += float(input("请输入第" + str(i + 1) + "个人成绩："))
# print(total_score / 5)

# 用while
total_score = 0
count = 0
while count < 5:
    total_score += float(input("请输入第" + str(count + 1) + "个人成绩："))
    count += 1
print("平均成绩："+str(total_score / 5))
