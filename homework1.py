import os
import configparser

f=open(r"C:\Desktop\log_files\201811123023.log","r")
flag=0
address=0
num=0
while flag==0:
    address=f.read('201811123023',address) #通过读取201811123023的地址下标，判断读了几次，即为打卡次数
    address=address+1
    num=num+1
    if address==0:
        flag=1#flag用作标志变量，作为结束循环的条件（后来发现是多此一举）
num=num-1
print(num)
    
