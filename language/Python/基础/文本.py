<<<<<<< HEAD
line = 'asdf fjdk; afed, fjek,asdf, foo，你好.yes'


import re

# print(re.split(r'[;,\s，。.]\s*',line))
# print(re.split(r'[;,\s，。.]',line))

fields=re.split(r'(;|,|\s)\s*',line)
print(fields)
=======
print("你好，世界"[0:2])

# 字符串格式化

print("你好,","世界","hello")

# 字符串运算，乘法
print("你好"*3)


>>>>>>> 1a0c6d66e3606d60229f5a0cab58b4f83be294d9
