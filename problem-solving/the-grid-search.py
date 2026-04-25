# https://www.hackerrank.com/challenges/the-grid-search
#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P

def gridSearch(G: list, P: list) -> str:    # -> "YES" | "NO"
    is_present: str = "NO"

    # grid specs
    grid_w: int = len(G[0])
    grid_h: int = len(G)

    # patter specs
    pattern_w: int = len(P[0])
    pattern_h: int = len(P)
    
    # if pattern breaks, skip this number of fields
    step: int = 1
    first_char: str = P[0][0]
    for i in range(1, pattern_w):
        if P[0][i] == first_char:
            step = i
            break
    
    # iterating through grid
    for i in range(grid_h - pattern_h + 1):
        j = 0
        while j < grid_w - pattern_w + 1:
            if G[i][j] == P[0][0]:
                match = True
                for k in range(pattern_h):
                    if G[i+k][j:j+pattern_w] != P[k]:
                        match = False
                        break
            
                if match:
                    is_present = "YES"
                    return is_present
                #else:
                    #j += step
            
            j += 1

    return is_present



if __name__ == '__main__':
    G = ["7283455864", "6731158619", "8988242643", "3830589324", "2229505813", "5633845374", "6473530293", "7053106601", "0834282956", "4607924137"]
    P = ["9505", "3845", "3530"]
    print(gridSearch(G, P))