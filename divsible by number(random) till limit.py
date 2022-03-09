import random
x=int(input('How many random numbers you want :'))
y=int(input('starting limit :'))
z=int(input('End limit:'))
v=int(input('Number you want to divide:'))
c=[]
for i in range(x):
    d=random.randint(y,z)
    c.append(d)
    if c[i] % v==0:
        print(c[i])
    
   
    