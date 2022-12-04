a=int(input("Enter the starting range: "))
b=int(input("Enter the ending range: "))
x=[]
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            x.append(i)
#print(x)
y=[]
for k in x:
    if k not in y:
        y.append(k)
    else:
        continue
print(y)