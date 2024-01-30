num = int(input("enter the number:"))
factor = 0
for i in range(1,num+1):
    if (num%i==0):
        factor+=1
print(factor)
if factor%2==0:
    print(num,"is not a perfectsquare")
else:
    print(num,"is a perfect square")

