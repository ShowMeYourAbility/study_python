"""
打印出“凌”字的unicode编码，
将“凌”字的unicode编码转为字符后打印
（提示：如果不会的话，将上面的题目复制给poe，但要告诉poe用python实现）
"""
# 打印“凌”字的 Unicode 编码
unicode_code = ord('凌')
print("“凌”字的 Unicode 编码:", unicode_code)

# 将 Unicode 编码转为字符并打印
character = chr(unicode_code)
print("Unicode 编码", unicode_code, "对应的字符:", character)
