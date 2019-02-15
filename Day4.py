# year=int(input('请输入年份'))
# if year%4==0 and year%100!=0 or year%400==0:
#     print('闰年')
# else:
#     print('不是闰年')
import random
lista=[random.randrange(20) for _ in range(20)]
stemp=0
for i in range(20):
    if i%2==0:
        for j in range(20):
            if j%2==0:
                if lista[i]>lista[j]:
                    stemp=lista[i]
                    lista[i]=lista[j]
                    lista[j]=stemp
        print(i,lista)
