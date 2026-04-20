# Dane są dwie tablice liczb całkowitych. Napisz funkcję, która
# dla podanych tablic zwraca tablicę tych elementów, które znajdują
# się w jednej z tablic ale nie w obydwu. Kolejność elementów nie ma
# znaczenia. Elementy w kazdej z tablic wejściowych nie powtarzają
# się.
#
# Przykład:
# Tablice: [1, 2, 3], [1, 4, 5] => [2, 3, 4, 5] lub dowolna
# permutacja

def xor_sum(tab1: list, tab2: list) -> list:
    target_tab = set(tab1)

    for num in tab2:
        if num in target_tab:
            target_tab.remove(num)
        else:
            target_tab.add(num)

    return list(target_tab)

if __name__ == "__main__":
    print(xor_sum([1, 2, 3], [1, 4, 5]))
    print(xor_sum([1, 3, 9], []))
    print(xor_sum([], [9, 10, 0]))
    print(xor_sum([], []))
    print(xor_sum([1, 3, 9], [1, 3, 9]))