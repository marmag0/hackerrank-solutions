# https://www.hackerrank.com/challenges/queens-attack-2
#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n - the number of rows and columns in the board
#  2. INTEGER k - the number of obstacles on the board
#  3. INTEGER r_q - the row number of the queen's position
#  4. INTEGER c_q - the column number of the queen's position
#  5. 2D_INTEGER_ARRAY obstacles

def queensAttack(n, k, r_q, c_q, obstacles):
    attacked: int = 0
    
    # converting obstacles to tuple for efficient retrieval
    obs_set: set = set(tuple(obstacles[i]) for i in range(k))
    print(obs_set)

    # iteration through attacked fields

    # vertical - up
    cur_q = [r_q, c_q]
    while cur_q[0] < n:
        cur_q[0] += 1
        if tuple(cur_q) in obs_set:
            break
        else:
            attacked += 1
    # vertical - down
    cur_q = [r_q, c_q]
    while cur_q[0] > 1:
        cur_q[0] -= 1
        if tuple(cur_q) in obs_set:
            break
        else:
            attacked += 1

    # horizontal - right
    cur_q = [r_q, c_q]
    while cur_q[1] < n:
        cur_q[1] += 1
        if tuple(cur_q) in obs_set:
            break
        else:
            attacked += 1
    # horizontal - left
    cur_q = [r_q, c_q]
    while cur_q[1] > 1:
        cur_q[1] -= 1
        if tuple(cur_q) in obs_set:
            break
        else:
            attacked += 1

    # diagonal - to top-right
    cur_q = [r_q, c_q]
    while cur_q[0] < n and cur_q[1] < n:
        cur_q[0] += 1
        cur_q[1] += 1
        if tuple(cur_q) in obs_set:
            break
        else:
            attacked += 1
    # diagonal - to top-left
    cur_q = [r_q, c_q]
    while cur_q[0] < n and cur_q[1] > 1:
        cur_q[0] += 1
        cur_q[1] -= 1
        if tuple(cur_q) in obs_set:
            break
        else:
            attacked += 1
    # diagonal - to bottom-left
    cur_q = [r_q, c_q]
    while cur_q[0] > 1 and cur_q[1] > 1:
        cur_q[0] -= 1
        cur_q[1] -= 1
        if tuple(cur_q) in obs_set:
            break
        else:
            attacked += 1
    # diagonal - to bottom-right
    cur_q = [r_q, c_q]
    while cur_q[0] > 1 and cur_q[1] < n:
        cur_q[0] -= 1
        cur_q[1] += 1
        if tuple(cur_q) in obs_set:
            break
        else:
            attacked += 1


    return attacked



if __name__ == "__main__":
    print(queensAttack(n=5, k=3, r_q=4, c_q=3, obstacles=[[5, 5], [4, 2], [2, 3]]))