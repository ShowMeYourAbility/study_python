"""
一张纸的厚度是0.01毫米
请计算，对折多少次超过珠穆朗玛峰(8844.43米)
思路:
数据：厚度、高度、次数
算法：厚度*=2 次数+=1
"""
start = 0.01
target = 8844.43 * 1000
count = 0
while start <= target:
    count += 1
    start *= 2
print(count)
