import string
from collections import Counter
import datetime

def count_bmi (h, w):
    bmi = w / (h * h)
    if  bmi < 17:
        print("Gầy độ II")
    elif   17 <= bmi < 18.5:
        print("Gầy độ I")
    elif    18.5 <= bmi < 25:
        print("Bình thường")

def leap_year (year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

def max_int(a, b, c):
    result = max(a, b, c)
    print(result)


def reverse_string(inputstring: str):
    return ''.join(reversed(inputstring))

def countdown_xmas(year):
    delta = datetime.datetime(year, 12, 25) - datetime.datetime.now()
    return delta

##
if __name__ == "__main__":
    #inputstring = input("Please input the string to reverse:")
    list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
    print(count_number_inlist(list))
