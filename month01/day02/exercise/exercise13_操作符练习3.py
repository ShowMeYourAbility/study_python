"""
练习：在终端中输入一个四位整数，计算每位相加和。
例如：录入1234，打印1+2+3+4结果
效果：
请输入四位整数：1234
结果是：10
"""
round_number = int(input("请输入四位整数："))
number_1 = round_number // 1000  # 1
number_2 = round_number % 10  # 4
number_3 = round_number % 100 // 10  # 3
number_4 = round_number % 1000 // 100  # 2
print(number_1 + number_2 + number_3 + number_4)