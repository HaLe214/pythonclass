import string
### Reverse string
def reverse_string(inputstring: str):
    return ''.join(reversed(inputstring))


##
if __name__ == "__main__":
    inputstring = input("Please input the string to reverse:")
    print(reverse_string(inputstring))
