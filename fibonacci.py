n=int(input("enter a number"))
a=0
b=1
count=0
while(count<n):
    print(a,end="")#end will give the answer in horizontal
    c=a+b
    a=b
    b=c
    count+=1