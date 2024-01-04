#prime facctors of a value
#this part of code defines prime numbers from 2 to 51
list=[]
for a in range(2,51):
    list.append(a)
for i in range(2,51):
    for j in range(1,i):
        if i%j==0:
            if j!=i and j!=1:
                if i in list:
                    list.remove(i)
                elif i not in list:
                    continue
#part of the code which detects the prime factors of the value which entered by user
value=int(input("enter a value: "))
new_value=value
x=""
for prime in list:
    if value%prime==0:#gets the prime number which divides value without remaind
        control=0
        while value%prime==0:
            value=value/prime 
            control=control+1#counts exponent of pime value
            if value%prime!=0:
                d=f"{prime}**{control}."
                x=x+d
print(f"{new_value}=",x)