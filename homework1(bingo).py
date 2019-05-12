x='201811123023'
num=0

with open(r'C:\Users\PC\Desktop\log_files\201811123023.log',mode='r',encoding='utf8') as f:
    
    for line in f:
        list1=line.split(' ')
        str1=list1[1]
        list2=str1.split('：')
        str2=list2[1]
        list3=str2.split(',')
        str3=list3[0]
        if str3==x:
            num=num+1

print(num)
