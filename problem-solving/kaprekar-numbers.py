# https://www.hackerrank.com/challenges/kaprekar-numbers
#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q

def kaprekarNumbers(p, q):
    k_nums = []
    for num in range(p, q+1):
        num_l = len(str(num))
        num_sq = num**2
        num_sq_l = len(str(num_sq))

        right = str(num_sq)[(num_sq_l-num_l):]
        if num_sq_l > 1:
            left = str(num_sq)[:(num_sq_l-num_l)]
        else:
            left = 0

        if int(left) + int(right) == num:
            k_nums.append(str(num))

    if len(k_nums) != 0:
        return " ".join(k_nums)
    else:
        return "INVALID RANGE"



if __name__ == '__main__':
    print(kaprekarNumbers(1, 100))