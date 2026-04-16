# https://www.hackerrank.com/challenges/permutation-equation
#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.

def permutationEquation(p: str):
    
    # input parsing
    p_list = p.split("\n")
    n: int = int(str(p_list[0]).strip("\r "))
    seq: list = p_list[1].split(" ")
    seq = [int(num) for num in seq]

    # debug
    print(f"{n}: {seq}")

    # iterating for proper formula
    res_seq: list = []
    for i in range(1, n+1):
        for outer_i in range(n):
            if i == seq[outer_i]:
                outer = outer_i+1
                break
        for inner_i in range(n):
            if outer == seq[inner_i]:
                res_seq.append(inner_i+1)
                break
    
    return(res_seq)
        


if __name__ == '__main__':
    print(permutationEquation("5\r\n4 3 5 1 2"))
