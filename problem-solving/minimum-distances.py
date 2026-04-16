# https://www.hackerrank.com/challenges/minimum-distances
#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

def minimumDistances(a: list) -> int:
    distances = dict()
    min_dist = float('inf')

    for i in range(len(a)):
        num = a[i]
        if num not in distances.keys():
            distances[num] = [i]
        else:
            distances[num] += [i]

    for key, values in distances.items():
        for i in range(len(values)-1):
            min_dist = min(min_dist, (values[i+1] - values[i]))
    
    if min_dist == float('inf'):
        return -1
    else:    
        return min_dist



if __name__ == '__main__':
    print(minimumDistances([7, 1, 3, 4, 1, 7])) # -> 3