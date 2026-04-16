# https://www.hackerrank.com/challenges/the-time-in-words
#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m

def timeInWords(h: int, m: int) -> str:
    
    time_str: str | None = None
    sep: str | None = None
    
    nums = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        21: "twenty one",
        22: "twenty two",
        23: "twenty three",
        24: "twenty four",
        25: "twenty five",
        26: "twenty six",
        27: "twenty seven",
        28: "twenty eight",
        29: "twenty nine",
        30: "half",
    }

    if m == 0:
        time_str = nums[h] + " " + "o' clock"
    elif m <= 30:
        if m % 15 == 0:
            sep = " past "
        else:
            if m == 1:
                sep = " minute past "    
            else:
                sep = " minutes past "
        time_str = nums[m] + sep + nums[h] 
    elif m > 30:
        h = h+1 % 12
        if m % 15 == 0:
            sep = " to "
        else:
            if m == 1:
                sep = " minute to "
            else:
                sep = " minutes to "
        time_str = nums[30-(m%30)] + sep + nums[h]
    
    return time_str



if __name__ == '__main__':
    print(timeInWords(h=1, m=1))