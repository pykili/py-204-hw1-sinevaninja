i=0
sum=0
N = int(input())
a = int(input())
while(a!=0):
    sum=sum+a
    a = int(input())
    i+=1
    if i==N:
        print("введено больше N чисел!")
        quit(1)
print(float(sum/i))
