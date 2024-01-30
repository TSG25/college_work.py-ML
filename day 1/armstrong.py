num = int(input("enter the number:"))
lenght = len(str(num))
sum_arm=0
temp=num
while temp!=0:
    digit=temp%10
    sum_arm+= (digit)**lenght
    temp= temp//10
print(sum_arm)
if sum_arm==num:
    print(f"{num}is a arm strong number")
else:
    print(f"{num}is not armstrong number")