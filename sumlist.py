a=[]
size = int(input("Enter the size of the list: "))
sum=0
for i in range(size):
    x=int(input())
    a.append(x)
    sum+=x
    
print(a)
print(sum)