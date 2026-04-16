import math

# https://www.hackerrank.com/challenges/encryption
#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def encryption(s: str) -> str:
    s = s.strip(" ")
    l = len(s)
    sqr_l = l**0.5

    # calculating grid dimensions
    col = math.ceil(sqr_l)
    if col * math.floor(sqr_l) >= l:
        row = math.floor(sqr_l)
    else:
        row = col
    
    # dividing string into grid
    grid = []
    for i in range(row):
        if col*(i+1) <= l:
            grid.append(s[col*i:col*(i+1)])
        else:
            grid.append(s[col*i:col*(i+1)] + " "*(col*(i+1)-l)) 
        print(grid[i])   # debug

    # saving enconded string
    s_enc = ""
    for i in range(len(grid[0])):
        for line in grid:
            if line[i] != " ":
                s_enc += line[i]
        s_enc += " "

    s_enc = s_enc.strip()
    return s_enc



if __name__ == "__main__":
    print(encryption(s="feedthedog"))