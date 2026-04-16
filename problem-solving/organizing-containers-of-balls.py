# https://www.hackerrank.com/challenges/organizing-containers-of-balls
#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.

def organizingContainers(container):
    outcomes: set = ("Possible", "Impossible")
    total_of_each_num: list = [0 for i in range(len(container))]

    for bucket in container:
        for i in range(len(bucket)):
            total_of_each_num[i] += bucket[i]

    # debug
    print(total_of_each_num)

    for bucket in container:
        bucket_size = sum(bucket)
        if bucket_size in total_of_each_num:
            total_of_each_num.remove(bucket_size)
        else:
            return outcomes[1]
    
    return outcomes[0]
            


if __name__ == '__main__':
    print(organizingContainers([[1, 3, 1], [2, 1, 2], [3, 3, 3]]))  # Impossible
    print(organizingContainers([[0, 2, 1], [1, 1, 1], [2, 0, 0]]))  # Possible