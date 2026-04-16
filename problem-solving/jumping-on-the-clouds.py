# https://www.hackerrank.com/challenges/jumping-on-the-clouds
#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.

def jumpingOnClouds(c: list):
    visited = [0, ]
    n = len(c)-1
    i = 0

    while i < n:
        if n-i >= 2:
            if c[i+2] == 0:
                visited.append(i+2)
                i+=2
            elif c[i+1] == 0:
                visited.append(i+1)
                i+=1
        else:
            visited.append(i+1)
            i+=1

    total_jumps = len(visited)-1

    return total_jumps



if __name__ == "__main__":
    print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0, 0]))