def f(n):
    if(n<=1):
        return n
    else:
        a=f(n-1)+f(n-2)
        return a
b=int(input("enter number:" ))
for i in range(b):
    print(f(i))
