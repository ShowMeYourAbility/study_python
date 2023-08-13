"""
在终端中累加 0 1 2 3
在终端中累加 2 3 4 5 6
在终端中累加 1 3 5 7
在终端中累加 8 7 6 5 4
在终端中累加 -1 -2 -3 -4 -5
"""
# 在终端中累加 0 1 2 3
print("在终端中累加 0 1 2 3")
total_value = 0
for i in range(4):
    print(i)
    total_value += i
print("total_value:" + str(total_value))
# 在终端中累加 2 3 4 5 6
print("在终端中累加 2 3 4 5 6")
total_value = 0
for i in range(2, 7):
    print(i)
    total_value += i
print("total_value:" + str(total_value))
# 在终端中累加 1 3 5 7
print("在终端中累加 1 3 5 7")
total_value = 0
for i in range(1, 8, 2):
    print(i)
    total_value += i
print("total_value:" + str(total_value))
# 在终端中累加 8 7 6 5 4
print("在终端中累加 8 7 6 5 4")
total_value = 0
for i in range(8, 3, -1):
    print(i)
    total_value += i
print("total_value:" + str(total_value))
# 在终端中累加 -1 -2 -3 -4 -5
print("在终端中累加 -1 -2 -3 -4 -5")
total_value = 0
for i in range(-1, -6, -1):
    print(i)
    total_value += i
print("total_value:" + str(total_value))
