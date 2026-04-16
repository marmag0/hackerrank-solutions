# https://www.hackerrank.com/challenges/halloween-sale
#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s

def howManyGames(p: int, d: int, m: int, s: int) -> int:
    bought: int = 0
    budget: int = s
    price: int = p

    while True:
        if budget >= price:
            budget -= price
            bought += 1
            if price > m:
                if price - d <= m:
                    price = m
                else:
                    price -=  d
        else:
            break

    return bought



if __name__ == '__main__':
    print(howManyGames(p=20, d=3, m=6, s=70))