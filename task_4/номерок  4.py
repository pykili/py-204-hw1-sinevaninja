kittens=['ID', 'FORM', 'LEMMA', 'ЧТО_ТО_ЕЩЁ']
for i in range(10):
    kittens[0],kittens[1],kittens[2],kittens[3]=input().split(" ")
    if '#' in kittens[0]:
        continue
    print(kittens)
        

