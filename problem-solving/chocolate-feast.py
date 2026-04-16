# https://www.hackerrank.com/challenges/chocolate-feast
#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m

def chocolateFeast(n: int, c: int, m: int) -> int:
    bars_eaten: int = 0
    wrappers: int = 0
    budget: int = n
    
    while budget >= c:
        bought = budget // c
        budget -= bought * c
        wrappers += bought
        
        free_bars = wrappers // m
        wrappers -= free_bars * m
        budget += c * free_bars

        bars_eaten += bought

    return bars_eaten
    


if __name__ == '__main__':
    print(chocolateFeast(n=10, c=2, m=5))