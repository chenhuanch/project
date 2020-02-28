"""
第二种方案
"""

# f = open('file','w')

# f = open("file",'w',1) # 1 行缓冲,遇到\n会刷新缓冲区

f = open("file",'wb',10) # >1 指明缓冲区大小 (二进制方式)

while True:
    data = input(">>")
    if not data:
        break
    f.write(b"hello world")
    # f.flush() # 刷新缓冲区

f.close()