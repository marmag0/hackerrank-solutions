# Dana jest liczba osób N oraz tablica K, której elementy to posortowane indeksy osób zarażonych wirusem.
# Kazdego dnia zarażeni zarażają sąsiadujące osoby.
# Podaj ilość dni, po których każdy zostanie zarażony.

# N = 7, K = [3]

# Indeksy: 0 1 2 3 4 5 6
# Dzień 0: . . . X . . .
# Dzień 1: . . X X X . .
# Dzień 2: . X X X X X .
# Dzień 3: X X X X X X X

# Odpowiedź: 3 dni

def find_ifected_coverage(N: int, K: list) -> int | None:
    max_days: int = 0
    last_i = N - 1

    if len(K) == 1:
        max_days = max((K[0]), (last_i-K[0]))
    elif len(K) >= 2:
        for i in range(len(K)):
            if i == 0:
                l_days = K[i]
                r_days = (K[i+1] - K[i]) // 2
            elif i == len(K)-1:
                l_days = (K[i] - K[i-1]) // 2
                r_days = last_i - K[i]
            else:
                l_days = (K[i] - K[i-1]) // 2
                r_days = (K[i+1] - K[i]) // 2
            
            max_days = max(max_days, l_days, r_days)   

    else:
        return None

    return max_days



if __name__ == "__main__":
    print(find_ifected_coverage(7, [3]))
    print(find_ifected_coverage(10, [2, 7]))