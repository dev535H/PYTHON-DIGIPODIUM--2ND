num=int(input("enter a number"))
original=num
sum=0
while num>0:
    digit=num %10
    sum=sum+digit**3
    num=num//10
if original==sum:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome1")