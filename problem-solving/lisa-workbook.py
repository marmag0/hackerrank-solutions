# https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true
#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr

def workbook(n: int, k: int, arr: list) -> int:
    s_pages: int = 0
    cur_page: int = 1
    
    # iterate for each chapter
    for i in range(n):
        for problem_no in range(1, arr[i]+1):
            if problem_no == cur_page:
                s_pages += 1
            if problem_no % k == 0:
                cur_page += 1
        if problem_no % k != 0:
            cur_page += 1

    return(s_pages)



if __name__ == '__main__':
    print(workbook(n=2, k=3, arr=[4, 2]))
