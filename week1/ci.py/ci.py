p=int(input("enter the priniciple amount:"))
r=(int(input("enter the rate:"))
n=(int("enter no. of times:"))
t=int(input("enter nuber of years:"))
a=p*(1+r/(100*n))**(n*t)
CI=a-p
print(round(CI,2))
