# https://www.hackerrank.com/challenges/service-lane
#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases

def serviceLane(n, cases, width):
    widths = ""
    for start, end in cases:
        max_w = float("inf")
        for i in range(start, end+1):
            max_w = min(width[i], max_w)
        widths += f"{max_w}\n"
    
    return widths



if __name__ == '__main__':
    print(serviceLane(n=8, cases=[[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]], width=[2, 3, 1, 2, 3, 2, 3, 3]))
