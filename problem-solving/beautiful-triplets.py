# https://www.hackerrank.com/challenges/beautiful-triplets
#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr

def beautifulTriplets(d: int, arr: list) -> int:
    counter = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] - arr[i] != d:
                continue
            for k in range(len(arr)):
                if arr[k] - arr[j] != d:
                    continue
                counter += 1
    
    return counter



if __name__ == '__main__':
    print(beautifulTriplets(d=3, arr=[1, 2, 4, 5, 7, 8, 10])) # -> 3