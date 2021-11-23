from collections import Counter
## Đếm loại ký tự
def count_char_type(s):
    number, lower, upper = 0, 0 , 0
    for i in s:
        if i.isdigit(): number += 1 
        if i.islower(): lower += 1 
        if i.isupper(): upper += 1 
    return {"LETTERS":lower + upper, "CASE": {"UPPER CASE":upper, "LOWER CASE":lower}, "DIGITS":number} 

# Chỉ số thống kê mô tả
def mean(l):
    sum_in_list = 0
    for i in l:
        sum_in_list = sum_in_list + i

    avg = sum_in_list/len(l)
    return avg

def median(l):
    s_list = sorted(l)
    len_data = len(s_list)
    middle_position = len_data // 2
    if len_data % 2 == 0:
        median_value = (s_list[middle_position -1] + s_list[middle_position])/2
    else:
        median_value  = s_list[middle_position] 
    return median_value

def mode(l):
    counter = 0
    num = l[0]
     
    for i in l:
        curr_frequency = l.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num


if __name__ == "__main__":
    s = "Hello World! 123"
    A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10] 
    print(mode(A))
