a=[]
size = int(input("Enter the size of the list: "))
prod=1
for i in range(size):
    x=int(input())
    a.append(x)
    prod*=x
    
print(a)
print(prod)