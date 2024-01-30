def arm_strong(num):
    stng_num = str(num)
    lenght = len(stng_num)
    sum_arm=0
    for digit in stng_num:
        sum_arm+= int(digit)**lenght
    return sum_arm
num = int(input("enter the number"))
print(arm_strong(num))