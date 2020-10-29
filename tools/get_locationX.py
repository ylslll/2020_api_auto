# _*_coding: utf-8_*_
# Created by yls on 2020/10/27 18:20

# IMAGE_VERIFICATION_MIN = 55.00
# IMAGE_VERIFICATION_MAX = 199.16666666666666

import math

def getLocationX(random):
    min = 55.00
    max = 199.16666666666666
    range = max - min

    locationX = round(range * random, 0)

    if locationX == 0:
        return min+1-10
    elif locationX == max:
        return max-1-10
    else:
        return locationX + min -1-10


if __name__ == "__main__":
    a = getLocationX(0.34013499680073966)
    print(a)