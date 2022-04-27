a=2
b=3
c=1

if a==b:
    if b==c:
        print("wszystkie są sobie równe")
    else:
        print("a oraz b są równe")
elif b==c:
    print("b oraz c są równe")
elif a==c:
    print("a oraz c są równe")
else:
    print("każda z tych cyfr jest inna")