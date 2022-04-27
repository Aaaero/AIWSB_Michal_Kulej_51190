x=30
a=0
for i in range(1,x+1):
    if x%i==0:
        a=a+1

if a==2:
    print("liczba jest pierwsza")
else:
    print("liczba jest zlozona")
