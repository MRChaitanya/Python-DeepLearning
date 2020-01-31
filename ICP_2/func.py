str = str(input("enter any string:"))
def string_alternative(str):
    str1 = str[::2]
    print(str1)
    return str1

string_alternative(str)