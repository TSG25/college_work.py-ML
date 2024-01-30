num1= int(input("enter the number1:"))
num2= int(input("enter the number2:"))
for i in range(num1,num2+1):
    count=1
    for j in range(1,i):
        if i%j==0:
            count+=1
    if count <=2:
        print(i)