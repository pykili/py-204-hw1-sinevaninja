kittens=['ID', 'FORM', 'LEMMA', 'ЧТО_ТО_ЕЩЁ']
for i in range(10):
    kittens[0],kittens[1],kittens[2],kittens[3]=input().split(" ")
    if kittens[1]==kittens[2] and kittens[1].find(kittens[2])==0:
        print('yay')
    else:
        print(kittens[1], kittens[2])
        

