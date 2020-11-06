a = input()
c=""
for i in a:
    if i==" ":
        continue
    c=c+i
is_palindrom = c[::-1]==c
print(is_palindrom)
