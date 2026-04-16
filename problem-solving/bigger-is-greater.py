# https://www.hackerrank.com/challenges/bigger-is-greater
#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.

def biggerIsGreater(w: str) -> str:
    w_list = list(w)

    i = len(w_list)-1
    while i >= 0:
        right_u = w_list[i:]
        right_s = sorted(w_list[i:], reverse=True)
        left = w_list[:i]

        if right_u != right_s:                
            for j in range(1, len(right_u)):
                if right_u[j] > right_u[0]:
                    swap_i = j
            
            right_u[0], right_u[swap_i] = right_u[swap_i], right_u[0]
            right_u = list(right_u[0]) + sorted(right_u[1:])
            final_list = left + right_u
            return "".join(final_list)

        i -= 1
    
    return "no answer"



if __name__ == '__main__':
    print(biggerIsGreater(w="fedcbabcd"))   # fedcbabdc
    print(biggerIsGreater(w="dkhc"))    # hcdk