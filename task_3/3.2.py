alphabet="abcdefghijklmonpqrstuvwxyz"
alphabet1=alphabet.upper()
alfavit="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alfavit1=alfavit.upper ()
k=""
c=""
for i in range(10):
    a=input()
    c=c+a
b=sorted(c)

for i in b:
    for l in alphabet:
        if i==l:
            k=k+l
            break
    for l in alphabet1:
        if i==l:
            k=k+l
            break
    for l in alfavit:
        if i==l:
            k=k+l
            break
    for l in alfavit1:
        if i==l:
            k=k+l
            break
print(k)
