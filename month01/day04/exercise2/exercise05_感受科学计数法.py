"""
“123e5”是数字的科学计算法表示方式，数字5表示把小数点向右挪5位
“12.3e-5”是数字的科学计算法表示方式，数字-5表示把小数点向左挪5位
执行感受一下结果
"""
num1 = 123e5
num2 = 12300000
print(num1 == num2)
num3 = 12.3e-5
num4 = 0.000123
print(num3 == num4)