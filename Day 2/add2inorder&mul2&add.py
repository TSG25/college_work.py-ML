x=[3,6,8,21,5,7,24,31,0,61]
add=0
mul=0
sum_all=0
new_list2=[]
new_list3=[]
for i in range(len(x)-1):
    add= (x[i]+x[i+1])
    new_list2.append(add)
for j in range(len(new_list2)-1):
    mul= new_list2[j]*new_list2[j+1]
    new_list3.append(mul)
for k in new_list3:
    sum_all+=k
print(new_list2)
print(new_list3)
print(sum_all)