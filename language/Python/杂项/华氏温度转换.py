"""
华氏温度=摄氏度*1.8+32
将华氏温度转成摄氏度
"""

f = float(input('请输入华氏温度： '))
c = (f-32)/1.8
print("%.1f华氏度= %.f摄氏度" % (f, c))
