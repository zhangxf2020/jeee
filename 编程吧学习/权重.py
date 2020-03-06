cloler = {'red':5,'yellow':100,'green':100,'blue':100}
clole = ['red','yellow','green','blue']
import random
num1,num2,num3,num4 = 0,0,0,0
# while True:
#     num1 += 1
#     if num1 ==1001:
#         print('总共出现了{}次'.format(num2))
#         break
#     s = random.choices(list(cloler.keys()),weights =list(cloler.values()),k=1)
#     if s[0] == 'red':
#         num2 +=1
#         print('第{}次出现了'.format(num1)+s[0])
#
# while True:
#     num4 +=1
#     if num4 == 1001:
#         print('总共出现了{}次'.format(num3))
#         break
#     num = random.randint(1,305)
#     if num<=5:
#         num3 +=1
#         print('第{}次出现了'.format(num4) + 'red')

xid1 = [i for i in range(1,256)]
xid2 = [100 for i in range(1,256)]
xid2[0] = 5
print(xid1,xid2)
for i in range(1000000):
    x = random.choices(xid1,weights=xid2,k=1)
    print(x)
    if x[0]==1:
        num1 +=1
print(num1)


