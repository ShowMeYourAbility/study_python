"""
根据心理年龄和实际年龄，打印智商
智商 = 心理年龄 *100 // 实际年龄
"""
xl = int(input("xl:"))
sj = int(input("sj"))
iq = xl * 100 // sj
if iq >= 140:
    print("tc")
elif iq >= 120:
    print("cch")
elif iq >= 110:
    print("ch")
else:
    print("低能")
