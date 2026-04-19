# https://www.hackerrank.com/challenges/manasa-and-stones
#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b

def stones(n: int, a: int, b: int) -> list:
    possible_vals: set = set()
    for i in range(n):
        possible_vals.add(a*i + b*(n-1-i))

    return sorted(possible_vals)



if __name__ == '__main__':
    print(stones(n=3, a=1, b=2))