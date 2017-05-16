try:
    f=open('C:/Users/Administrator/Desktop/sgs.txt','r',encoding='gbk')
    print(f.read())
finally:
    if f:
        f.close()

#推荐写法
with open('C:/Users/Administrator/Desktop/sgs.txt','r') as cf:
    for line in cf.readlines():
        print(line.strip())


file=open('C:/Users/Administrator/Desktop/sgs.txt','w')
file.write('my name is book:读书 /n sdaffsad')
file.close()

#推荐写法
with open('C:/Users/Administrator/Desktop/sgs.txt','w') as wf:
    wf.write('喔是中国人')