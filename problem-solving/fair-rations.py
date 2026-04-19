# https://www.hackerrank.com/challenges/fair-rations
#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.

def fairRations(B: list) -> str:
    min_loaves = 0

    if sum(B) % 2 == 0:
        for i in range(len(B)):
            if B[i] % 2 != 0:
                if i != len(B)-1:
                    B[i] += 1; B[i+1] += 1
                else:
                    B[i] += 1; B[i-1] += 1
                min_loaves += 2
        
        return str(min_loaves)
            
    else:
        return "NO"



if __name__ == '__main__':
    print(fairRations(B=[4, 5, 6 ,7]))