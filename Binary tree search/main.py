from tree import treeify
from tour import show_off, ElementInTree

wezly = []

while True:
    wezel = input("nowy wezeł (wpisz 0 by wyjść):\n").strip()
    try:
        wezel = int(wezel)
    except:
        wezel = 0
    if wezel == 0:
        break
    wezly.append(wezel)

tree = treeify(wezly)
show_off(tree)

print('Teraz czas na sprawdzenie, czy liczba jest w drzewie')
print('Podaj liczbę testów, a potem testy, a ci odpowiem YES lub NO')

ilosc_testow = int(input('Ile testów? ').strip())
tourer = ElementInTree(tree)
for _ in range(ilosc_testow):
    test = int(input('Jaką liczbę chcesz sprawdzić? ').strip())
    if tourer.is_in_tree(test):
        print('YES')
    else:
        print('NO')
