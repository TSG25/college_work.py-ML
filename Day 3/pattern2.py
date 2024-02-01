count=10
for i in range(1,5):
    for j in range(5,1,-i):
        print(count,end=" ")
        count-=1
    print("\n")