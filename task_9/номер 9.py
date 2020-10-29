sum=0
for n in range(1, 101):
    for i in range(1, n+1):
        sum=sum + ((2 * i)-1)
    if sum == (n * n):
        print('ура!', i)
    elif sum != n*n:
        print('блин блинский', i)        
    sum=0
        
    
