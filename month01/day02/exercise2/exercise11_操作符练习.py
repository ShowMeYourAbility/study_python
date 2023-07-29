"""
练习1：在终端中输入一个疫情确诊人数再录入一个治愈人数，打印治愈比例
格式：治愈比例为xx%
效果：
请输入确诊人数：500
请输入治愈人数：496
治愈比例为99.2%
"""
# 1.输入数据
number_of_confirmed_cases = input("请输入确诊人数：")
number_of_people_cured = input("请输入治愈人数：")
# 2.计算
number_of_confirmed_cases = int(number_of_confirmed_cases)
number_of_people_cured = int(number_of_people_cured)
cure_rate = number_of_people_cured * 100 / number_of_confirmed_cases
# 3.返回结果
print("治愈比例为" + str(cure_rate) + "%")
