"""
用两种方法实现（使用continue和不使用continue）：
累加10 -- 60之间，个位不是3/5/8的整数和
"""

sum_value = 0
for i in range(10, 61):
    remainder = i % 10
    if remainder != 3 and remainder != 5 and remainder != 8:
        sum_value += i
print(sum_value)

sum_value = 0
for i in range(10, 61):
    remainder = i % 10
    if remainder == 3 or remainder == 5 or remainder == 8:
        continue
    sum_value += i
print(sum_value)
