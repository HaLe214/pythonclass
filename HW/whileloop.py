import string
from collections import Counter
import datetime

def printstar(n):
    star = "*"
    space = " "
    for num in range(n):
        spacenum = n - (num + 1)
        starnum = num + 1
        print ((spacenum * space) + (starnum * star))
    
    end_str = "\n"
    ## Hình 2
    for num in range(n):
        spacenum  =  n - (num + 1)
        starnum= num + 1
        if starnum == n:
            end_str =""
        print((spacenum * space) + (starnum * star), end = end_str)
        
    for num in range(n):
        starnum = n - num 
        spacenum  = n + 2
        if num == 0: spacenum = 0
        print(spacenum * space, (starnum * star).strip())
    
    # Hình 3
    for num in range(n):
        spacenum  = n - num + 1
        starnum= num + 1
        if starnum <= 2 or starnum == n:
            star_text = starnum * star
        else:
            star_text = star +  space * (starnum - 2) + star
        if starnum == n:
            end_str =""
        print(star_text.rstrip() , end = end_str)
        

    for num in range(n):
        starnum = n - num 
        spacenum  = n  + num
        if num == 0: spacenum = 0
        if starnum <= 2 or starnum == n:
            star_text = starnum * star
        else:
            star_text = star +  space * (starnum - 2) + star
        print(spacenum * space + star_text)


def count_number_inlist(inputlist):
    dict = Counter(inputlist)
    return dict

def unique_value_dict(list_dict):
    for dict in list_dict:
        listvalue = list(dict.values())
        output = []
        for x in listvalue:
            if x not in output:
                output.append(x)
        print(output)

def find_pair(list, sum):
    result = []
    for f in list:
        for s in list:
            if f + s == sum and f < s:
                result.append((f, s))
    print(result)
if __name__ == "__main__":
    list1 = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
    list_dict1 = [dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
    list_dict2 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    A = [3, 6, 7, 9, 11, 12] 
    B = 15
    print(find_pair(A, B))
