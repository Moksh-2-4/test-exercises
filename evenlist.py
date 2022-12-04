a=[]
b=[]
size=int(input("Enter the size of the list: "))
for i in range(size):
    x=int(input("Enter list element"))
    a.append(x)
    if x%2==0:
        b.append(x)
    else:
        continue
print(f"The list is {a}")
print(f"The list after having only even numbers is {b}")