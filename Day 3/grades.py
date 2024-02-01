def grades(a):
    if a>=90:
        print("O")
    elif a>=80:
        print("A+")
    elif a>=70:
        print("A")
    elif a>=60:
        print("B")
    elif a>=50:
        print("c")
    else:
        print("fail")
for i in range(10):
    i = int(input("enter the grades:"))
    grades(i)