k=""
c=""
for i in range(10):
    a=input()
    c=c+a
    b=sorted(set(c))

for i in b:
    if i==" ":
        continue
    k=k+" "+i
print(k)
