#顺序结构
A = int(input("输入A："))

print("A=",A)

#判断结构
if 3<0:
    print("错误")
elif 3>0:
    print("正确")

#循环结构
i =1
sum = 0
while i<A:
    sum+=i
    i +=1
print("%d结果是：%d"%(A,sum))

for i in range(A):
    sum +=i
print("%d,%d"%(A,sum))

#异常
