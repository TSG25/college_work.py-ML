num = [1,5,6,18,21,24,13]
print(num)
for i in range(len(num)):
    if num[i]%2==0:
        for j in range(i+1,len(num)):
            if num[j]%2 !=0:
                num[i] = num[j]
                break        
    else:
        for j in range(i+1,len(num)):
            if num[j]%2==0:
                num[i]=num[j]
                break
print(num)
