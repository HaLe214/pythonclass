def anagram_number(number):
    str_num = str(number[::-1])
    if str_num == str(number):
        print("input and output is equal")
    else:
        print("input and output is not equal")

def roman_to_int(s):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i, c in enumerate(s):
        if (i + 1) == len(s) or roman_numerals[c] >= roman_numerals[s[i + 1]]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    return result

if __name__ == '__main__':
    print(roman_to_int("XXI"))