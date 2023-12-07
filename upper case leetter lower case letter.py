x=("Welcome To LPU:")
lower=0
upper=0
space=0
for i in x:
    if (i.islower()):
        lower+=1
    elif(i.isupper()):
        upper += 1
    else:
        space+=1

print("No of uppercase:",upper)
print("No of lowercase:",lower)
print("No of space:",space)
