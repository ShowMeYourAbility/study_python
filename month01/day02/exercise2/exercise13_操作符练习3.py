"""
练习：在终端中输入一个四位整数，计算每位相加和。
例如：录入1234，打印1+2+3+4结果
效果：
请输入四位整数：1234
结果是：10
"""
# 1.输入数据
four_digit_integer = int(input("请输入四位整数："))
# 2.计算
thousands_place = four_digit_integer // 1000
four_digit_integer %= 1000
hundreds_place = four_digit_integer // 100
four_digit_integer %= 100
tens_place = four_digit_integer // 10
four_digit_integer %= 10
ones_place = four_digit_integer // 1

result = thousands_place + hundreds_place + tens_place + ones_place
# 3.返回结果
print("结果是：" + str(result))
