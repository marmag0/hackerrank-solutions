# https://www.hackerrank.com/challenges/cavity-map
#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.

def cavityMap(grid: list) -> list:
    if len(grid) >= 3:
        for i in range(1, len(grid)-1):
            j = 1
            while j < len(grid[i])-1: 
                if grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j]:
                    grid[i] = grid[i][0:j] + "X" + grid[i][j+1:]
                    j += 2
                else:
                    j += 1

    return grid



if __name__ == '__main__':
    print(cavityMap(grid=['1112', '1912', '1892', '1234']))