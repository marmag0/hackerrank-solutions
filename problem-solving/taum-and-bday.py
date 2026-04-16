# https://www.hackerrank.com/challenges/taum-and-bday/
#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b - number of black gifts
#  2. INTEGER w - number of white gifts
#  3. INTEGER bc - cost of black gift
#  4. INTEGER wc - cost of white gift
#  5. INTEGER z - cost to convert one color to another

def taumBday(b, w, bc, wc, z):
    min_cost = 0
    diff = abs(bc-wc)
    if diff <= z or wc == bc:
        min_cost = b*bc + w*wc
    else:
        if bc < wc:
            min_cost = bc*b + (bc+z)*w 
        elif wc < bc:
            min_cost = wc*w + (wc+z)*b

    return(min_cost)



if __name__ == '__main__':
    print(taumBday(b=5, w=9, bc=2, wc=3, z=4))
    print(taumBday(b=3, w=6, bc=9, wc=1, z=1))