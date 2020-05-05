#Ex:1 without function
x = int(input("Enter the number: "))
y = 1
for i in range(1, x+1):
    y = y * i
print(y)

#Ex:2 with function
def fact(n):
    f = 1
    for i in range(1,n+1):
         f = f * i
    return f
x = int(input("enter your number: "))
result = fact(x)
print(result)
