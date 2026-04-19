from math import ceil

# https://www.hackerrank.com/challenges/flatland-space-stations
#
# Complete the flatlandSpaceStations function below.

def flatlandSpaceStations(n: int, c: list) -> int:
    max_d: int = float("-inf")
    stations: list = sorted(c)
    l_stations = len(stations)

    if l_stations > 1:
        for i in range(l_stations):
            if i == 0:
                left_d = stations[i]
                right_d = ceil((stations[i+1] - stations[i] - 1) / 2)
            elif i == l_stations - 1:
                left_d = ceil((stations[i] - stations[i-1] - 1) / 2)
                right_d = n-1 - stations[i]
            else:
                left_d = ceil((stations[i] - stations[i-1] - 1) / 2)
                right_d = ceil((stations[i+1] - stations[i] - 1) / 2)
        
            max_d = max(max_d, left_d, right_d)

    else:   # l_stations == 1
        max_d = max((stations[0], n-1 - stations[0]))

    return max_d



if __name__ == '__main__':
    print(flatlandSpaceStations(n=90, c=[85, 44, 25, 67, 20, 83, 50, 88, 2, 32, 16]))