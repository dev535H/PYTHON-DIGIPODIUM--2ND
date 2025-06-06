num=int(input("enter a number"))
if num<=1:
    print(f"{num} is not a prime number")
else:
    for i in range(2,num):
        if num%1==0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is prime number")