a=2
b=2

if a>0 and b>0:
    P=a*b
    print("Pole prostokąta wynosi: ",P)
else:
    print("Błędne dane")
    print("Boki prostokąta muszą być dodatnie")

print("W zadaniu jest błąd podstawa i wysokość nie mogą być takie same, więc wynik powinien być następujący")
if a>0 and b>a or b>0 and a>b:
    p=a*b
    print("Pole prostokąta wynosi: ",p)
else:
    print("Błędne dane")
    print("Boki prostokąta muszą być dodatnie")